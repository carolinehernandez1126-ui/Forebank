"""Replay recorded Codex reference/Q runs from ZIPs; does not write result files."""

import argparse
import ast
import json
import math
from pathlib import Path
from zipfile import ZipFile

from verificar_paquete import verify

from research_lab.analytics import frame
from research_lab.models import Dataset

BASE = Path(__file__).resolve().parent


def read(z, name):
    return json.loads(z.read(name).decode("utf-8-sig"))


def functions(z, name, chosen):
    # Compile only imports and named functions from inspected, hash-verified own code.
    # Discard all top-level scripts, networking, writes and __main__ blocks.
    tree = ast.parse(z.read(name).decode("utf-8-sig"))
    nodes = [
        v
        for v in tree.body
        if isinstance(v, (ast.Import, ast.ImportFrom))
        or isinstance(v, ast.FunctionDef)
        and v.name in chosen
    ]
    ns = {"__name__": "frozen_replay"}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), name, "exec"), ns)
    return ns


def compare(got, expected, metrics, context):
    for key in metrics:
        x = got[key]
        y = expected[key]
        if x is None or y is None:
            assert x is y, (context, key, x, y)
        elif isinstance(x, (int, float)):
            assert math.isclose(x, y, rel_tol=1e-8, abs_tol=1e-9), (context, key, x, y)
        else:
            assert x == y, (context, key)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--asset", help="One ticker, e.g. BTC. Default: all68 spot assets.")
    args = ap.parse_args()
    verify()
    count_ref = 0
    count_q = 0
    count_p1 = 0
    idx = json.loads((BASE / "INDICE_RESULTADOS.json").read_text(encoding="utf-8"))
    with (
        ZipFile(BASE / "01_codex_snapshots.zip") as data,
        ZipFile(BASE / "02_codex_analisis.zip") as results,
    ):
        ref = functions(
            results,
            "codex/private/strategy_study.py",
            {"prepared", "simulate_strategy", "buy_hold", "self_tests"},
        )
        q = functions(
            results, "codex/private/diagnostic_twenty.py", {"features", "simulate", "boundaries"}
        )
        q2 = functions(
            results,
            "codex/private/diagnostic_second_five.py",
            {"floor_tick", "features", "simulate"},
        )
        for row in idx["primary_rows"]:
            if "dataset_member" not in row or args.asset and row["asset"] != args.asset.upper():
                continue
            n = row["asset"]
            d = Dataset.model_validate(read(data, row["dataset_member"]))
            b = read(results, row["reference_results_member"])[n]
            x = ref["prepared"](frame(d.candles[1440]))
            split = len(x) - 120
            for kind in ["T", "R"]:
                for part, start, end in [
                    ("full_eligible", 200, len(x)),
                    ("development", 200, split),
                    ("holdout", split, len(x)),
                ]:
                    expected = b["strategies"][kind].get(part)
                    if expected is None:
                        continue
                    got = ref["simulate_strategy"](x, kind, start, end)
                    compare(
                        got,
                        expected,
                        [
                            "trades",
                            "return",
                            "max_drawdown",
                            "mean_R",
                            "profit_factor",
                            "forced_final_exits",
                        ],
                        n + "/" + kind + "/" + part,
                    )
                    count_ref += 1
                if "holdout_double_costs" in b["strategies"][kind]:
                    got = ref["simulate_strategy"](x, kind, split, len(x), 80, 30)
                    compare(
                        got,
                        b["strategies"][kind]["holdout_double_costs"],
                        ["trades", "return", "max_drawdown", "mean_R", "profit_factor"],
                        n + "/" + kind + "/stress",
                    )
                    count_ref += 1
            parent = row["reference_results_member"].rsplit("/", 1)[0]
            diag_name = parent + "/pilot-specific-diagnostic.json"
            if diag_name in results.namelist():
                recorded = read(results, diag_name)
                if n in recorded:
                    eng = q2 if row["group"] == "second" else q
                    features = (
                        eng["features"](d, n) if row["group"] == "second" else eng["features"](d)
                    )
                    for part in ["base", "double_costs"]:
                        got = (
                            eng["simulate"](
                                features, n, ((0.004, 0.0015) if part == "base" else (0.008, 0.003))
                            )
                            if row["group"] == "second"
                            else eng["simulate"](features, 0.0055 if part == "base" else 0.011)
                        )
                        expected = recorded[n][part]
                        compare(
                            got, expected, ["trades", "return", "max_drawdown"], n + "/Q/" + part
                        )
                        count_q += 1
            print(n, "replay PASS", flush=True)
        # P1 is a prospective assessment, not a fabricated backtest. Recompute its ratios.
        p1 = read(results, "codex/outputs/pilot-v2-20261026/assessment.json")
        for n, v in p1["assets"].items():
            if args.asset and n != args.asset.upper():
                continue
            E = v["ask"]
            S = v["stop_p1"]
            T = v["target_p1"]
            C = 0.0055
            unit = E - S + (E + S) * C
            if unit > 0:
                assert math.isclose((T - E - (T + E) * C) / unit, v["rr_at_ask"], abs_tol=1e-9)
            count_p1 += 1
    print(
        json.dumps(
            {
                "status": "PASS",
                "reference_segments_replayed": count_ref,
                "pilot_Q_cases_replayed": count_q,
                "P1_assessments_checked": count_p1,
                "network_used": False,
                "claude_runs_replayed": False,
                "note": "Authorized sanitized Claude research is supplied separately; this runner replays Codex only, not Claude strategies.",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
