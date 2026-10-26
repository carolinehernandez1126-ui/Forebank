from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv
from pydantic import ValidationError

from .analytics import dossier, frame, markdown_report, portfolio_correlations, quality
from .backtest import walk_forward
from .decision import decide
from .demo import synthetic_dataset
from .io import assets, digest, policy, read_json, settings, utcnow, write_json
from .models import Account, Candle, Dataset, Proposal, Review, RiskPolicy
from .providers import INTERVALS, PublicClient, SourceError, collect
from .risk import assess
from .store import Store
from .summary import trading_summary


def load(model, path):
    return model.model_validate(read_json(path))


def parser():
    p = argparse.ArgumentParser(
        description="Kraken Research Lab: public data, risk and two-AI review"
    )
    p.add_argument("--config", default="config/lab.toml")
    p.add_argument("--db", default="data/lab.sqlite")
    sub = p.add_subparsers(dest="command", required=True)
    c = sub.add_parser("collect", help="Fetch public Kraken snapshots and optional fundamentals")
    c.add_argument("--asset", required=True, help="Configured symbol, e.g. BTC/USD")
    c.add_argument("--assets-file", default="config/assets.toml")
    c.add_argument("--enrich", action="store_true")
    c.add_argument("--output", required=True)
    c = sub.add_parser("analyze", help="Generate JSON dossier + Markdown report")
    c.add_argument("--dataset", required=True)
    c.add_argument("--output", required=True, help="JSON output path; also writes .md")
    c = sub.add_parser("backtest", help="Chronological EMA baseline; no trade authorization")
    c.add_argument("--dataset", required=True)
    c.add_argument("--interval", type=int, default=60)
    c.add_argument("--train-bars", type=int, default=300)
    c.add_argument("--test-bars", type=int, default=100)
    c.add_argument("--output", required=True)
    c = sub.add_parser("correlations", help="Aligned return correlations for multiple snapshots")
    c.add_argument("--datasets", nargs="+", required=True)
    c.add_argument("--interval", type=int, default=60)
    c.add_argument("--output", required=True)
    c = sub.add_parser("import-csv", help="Import Kraken historical OHLCVT into existing dataset")
    c.add_argument("--dataset", required=True)
    c.add_argument("--csv", required=True)
    c.add_argument("--interval", type=int, required=True)
    c.add_argument("--source-url", required=True)
    c.add_argument("--output", required=True)
    c = sub.add_parser("draft", help="Create intentionally incomplete proposal; never an AI review")
    c.add_argument("--dataset", required=True)
    c.add_argument("--account", required=True)
    c.add_argument("--plan-id", required=True)
    c.add_argument("--output", required=True)
    c = sub.add_parser(
        "review-template", help="Create abstain review for the actual reviewer to edit"
    )
    c.add_argument("--proposal", required=True)
    c.add_argument("--reviewer", choices=["codex", "claude"], required=True)
    c.add_argument("--output", required=True)
    for name in ("risk-check", "decide"):
        c = sub.add_parser(name)
        c.add_argument("--proposal", required=True)
        c.add_argument("--dataset", required=True)
        c.add_argument("--account", required=True)
        c.add_argument("--output", required=True)
        if name == "decide":
            c.add_argument("--reviews", nargs="+", required=True)
    c = sub.add_parser("demo", help="Fully offline reproducible synthetic reports")
    c.add_argument("--output-dir", default="outputs/demo")
    c = sub.add_parser("schemas", help="Export JSON contracts for AI agents")
    c.add_argument("--output-dir", default="schemas")
    c = sub.add_parser("journal", help="Export private audit events")
    c.add_argument("--output", required=True)
    return p


def import_csv(path, interval, now):
    if interval not in INTERVALS:
        raise ValueError("Unsupported interval")
    candles = []
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        for i, row in enumerate(csv.reader(handle)):
            if not row:
                continue
            if i == 0 and row[0].lower() == "timestamp":
                continue
            if len(row) != 7:
                raise ValueError("Expected Kraken CSV: timestamp,open,high,low,close,volume,trades")
            stamp = datetime.fromtimestamp(int(row[0]), UTC)
            if stamp.timestamp() + interval * 60 > now.timestamp():
                continue
            candles.append(
                Candle(
                    timestamp=stamp,
                    open=row[1],
                    high=row[2],
                    low=row[3],
                    close=row[4],
                    volume=row[5],
                )
            )
    if not candles:
        raise ValueError("No closed candles in CSV")
    times = [c.timestamp for c in candles]
    if times != sorted(set(times)):
        raise ValueError("CSV timestamps must be unique and sorted; no silent reordering")
    return candles


def run(args):
    load_dotenv(override=False)
    cmd = args.command
    if cmd == "schemas":
        for model in (Dataset, Account, Proposal, Review, RiskPolicy):
            write_json(
                Path(args.output_dir) / (model.__name__.lower() + ".schema.json"),
                model.model_json_schema(),
            )
        return 0
    if cmd == "demo":
        folder = Path(args.output_dir)
        data = synthetic_dataset()
        write_json(folder / "dataset.json", data)
        report = dossier(data, now=data.created_at)
        write_json(folder / "dossier.json", report)
        (folder / "dossier.md").write_text(markdown_report(report), encoding="utf-8")
        test = walk_forward(frame(data.candles[60]))
        test["synthetic"] = True
        write_json(folder / "backtest.json", test)
        print(f"SYNTHETIC research written to {folder}; not eligible for execution")
        return 0
    cfg, risk_policy = settings(args.config), policy(args.config)
    min_bars = risk_policy.min_bars
    if cmd == "collect":
        matches = [a for a in assets(args.assets_file) if a["symbol"] == args.asset]
        if len(matches) != 1:
            raise ValueError("Asset must match one configured symbol")
        store = Store(args.db)
        client = PublicClient(store)
        try:
            data = collect(
                client,
                matches[0],
                cfg["research"]["intervals"],
                args.enrich,
                cfg["research"]["fred_series"],
            )
            write_json(args.output, data)
            store.audit("collection", {"dataset_sha256": digest(data), "symbol": args.asset})
        finally:
            client.close()
            store.close()
    elif cmd == "analyze":
        data = load(Dataset, args.dataset)
        report = dossier(data, min_bars=min_bars)
        write_json(args.output, report)
        Path(args.output).with_suffix(".md").write_text(markdown_report(report), encoding="utf-8")
    elif cmd == "backtest":
        data = load(Dataset, args.dataset)
        candles = data.candles[args.interval]
        ref = candles[-1].timestamp + timedelta(minutes=args.interval)
        checks = quality(candles, args.interval, now=ref, min_bars=args.train_bars + args.test_bars)
        if not checks["passed"]:
            raise ValueError(f"Backtest data quality failed: {checks['reasons']}")
        result = walk_forward(
            frame(candles),
            args.train_bars,
            args.test_bars,
            risk_policy.fee_bps_per_side,
            risk_policy.slippage_bps_per_side,
        )
        result.update(dataset_sha256=digest(data), synthetic=data.synthetic, status="RESEARCH_ONLY")
        write_json(args.output, result)
    elif cmd == "correlations":
        write_json(
            args.output,
            portfolio_correlations([load(Dataset, p) for p in args.datasets], args.interval),
        )
    elif cmd == "import-csv":
        data = load(Dataset, args.dataset)
        data.candles[args.interval] = import_csv(args.csv, args.interval, utcnow())
        data.provenance.append(
            {
                "url": args.source_url,
                "fetched_at": utcnow().isoformat(),
                "file_sha256": hashlib.sha256(Path(args.csv).read_bytes()).hexdigest(),
                "note": "Local import; user must verify asset, interval and original download",
            }
        )
        write_json(args.output, data)
    elif cmd == "draft":
        data, account = load(Dataset, args.dataset), load(Account, args.account)
        now = utcnow()
        write_json(
            args.output,
            {
                "schema_version": "2",
                "plan_id": args.plan_id,
                "created_at": now.isoformat(),
                "expires_at": (
                    now + timedelta(seconds=risk_policy.max_plan_lifetime_seconds)
                ).isoformat(),
                "symbol": data.instrument.symbol,
                "side": "buy",
                "dataset_sha256": digest(data),
                "account_sha256": digest(account),
                "policy_sha256": digest(risk_policy),
                "entry": 0,
                "stop": 0,
                "target": 0,
                "quantity": 0,
                "thesis": "",
                "invalidation": "",
                "technical_summary": "",
                "fundamental_summary": "",
                "statistical_summary": "",
                "evidence": [],
                "limitations": ["INCOMPLETE DRAFT: requires independent research"],
                "research": {
                    "horizon": "",
                    "scope": "",
                    "cutoff_at": now.isoformat(),
                    "stopping_reason": "",
                    "sufficiency_rationale": "",
                    "decision_with_available_information": False,
                    "alternatives_considered": [],
                    "strategy_coherence": "",
                    "execution_rules": "",
                    "scenario_analysis": "",
                    "monitoring_plan": "",
                    "gaps": [],
                },
            },
        )
    elif cmd == "review-template":
        proposal = load(Proposal, args.proposal)
        write_json(
            args.output,
            {
                "reviewer": args.reviewer,
                "model": "FILL_ACTUAL_MODEL",
                "reviewed_at": utcnow().isoformat(),
                "proposal_sha256": digest(proposal),
                "verdict": "abstain",
                "rationale": "Pending independent review of analysis and sources.",
                "independently_checked_sources": ["PENDING"],
                "blockers": ["Independent review not performed"],
                "uncertainty_accepted": False,
                "strategy_coherence_confirmed": False,
            },
        )
    elif cmd in ("risk-check", "decide"):
        proposal = load(Proposal, args.proposal)
        account, data = load(Account, args.account), load(Dataset, args.dataset)
        store = Store(args.db)
        try:
            # A breach observed by this lab persists for the trading day, even after equity recovers.
            locked = any(
                e["kind"] in {"risk_lock", "drawdown_lock"}
                and e["payload"]["account_id"] == account.account_id
                and (
                    e["kind"] == "drawdown_lock"
                    or e["payload"]["day_start"] == account.day_start.isoformat()
                )
                for e in store.events()
            )
            # Do not mutate the hashed account; append lockout outcome below instead.
            if cmd == "decide":
                reviews = [load(Review, p) for p in args.reviews]
                result = decide(
                    proposal,
                    reviews,
                    account,
                    risk_policy,
                    data,
                    min_bars=min_bars,
                )
                risk = result["risk"]
            else:
                result = risk = assess(proposal, account, risk_policy, data, min_bars=min_bars)
            if "daily_loss_breached" in risk["reasons"]:
                store.audit(
                    "risk_lock",
                    {"account_id": account.account_id, "day_start": account.day_start.isoformat()},
                )
            if "max_drawdown_breached" in risk["reasons"]:
                store.audit(
                    "drawdown_lock",
                    {"account_id": account.account_id, "day_start": account.day_start.isoformat()},
                )
            if locked:
                risk["passed"] = False
                risk["reasons"].append("account_lockout_persisted_in_journal")
                if cmd == "decide":
                    result["status"] = "WAIT"
                    result["reasons"].append("account_lockout_persisted_in_journal")
            write_json(args.output, result)
            if cmd == "decide":
                Path(args.output).with_suffix(".md").write_text(
                    trading_summary(proposal, reviews, result), encoding="utf-8"
                )
            store.audit(cmd, result)
            print(
                result.get("status", "PASS" if result["passed"] else "BLOCKED")
                if cmd == "risk-check"
                else result["status"]
            )
            return 0 if risk["passed"] and (cmd != "decide" or result["status"] != "WAIT") else 2
        finally:
            store.close()
    elif cmd == "journal":
        store = Store(args.db)
        try:
            write_json(args.output, store.events())
        finally:
            store.close()
    print(f"Written: {args.output}")
    return 0


def main():
    try:
        code = run(parser().parse_args())
    except (ValidationError, ValueError, SourceError, OSError, KeyError, IndexError) as error:
        # Validation errors deliberately omit input values, which may contain private account data.
        if isinstance(error, ValidationError):
            detail = [{"loc": e["loc"], "msg": e["msg"]} for e in error.errors()]
            print(json.dumps({"status": "INVALID_INPUT", "errors": detail}), file=sys.stderr)
        else:
            print(f"ERROR: {error}", file=sys.stderr)
        code = 1
    raise SystemExit(code)
