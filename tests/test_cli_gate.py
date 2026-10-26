from datetime import timedelta

import research_lab.decision
import research_lab.risk
from research_lab.cli import parser, run
from research_lab.io import digest, read_json, write_json
from research_lab.store import Store


def inputs(tmp_path, case):
    now, data, policy, account, proposal, reviews = case
    config = tmp_path / "lab.toml"
    config.write_text(
        "[risk]\npolicy_verified = true\ninitial_capital = 10000\ndaily_loss_fraction = 0.01\n[research]\n"
    )
    write_json(tmp_path / "dataset.json", data)
    write_json(tmp_path / "account.json", account)
    write_json(tmp_path / "proposal.json", proposal)
    return [
        "--config",
        str(config),
        "--db",
        str(tmp_path / "lab.sqlite"),
        "risk-check",
        "--dataset",
        str(tmp_path / "dataset.json"),
        "--account",
        str(tmp_path / "account.json"),
        "--proposal",
        str(tmp_path / "proposal.json"),
        "--output",
        str(tmp_path / "risk.json"),
    ]


def test_daily_breach_stays_blocked_after_equity_recovers(tmp_path, case, monkeypatch):
    monkeypatch.setattr(research_lab.risk, "utcnow", lambda: case[0])
    _, _, _, account, proposal, _ = case
    account.equity = account.free_cash = 9900
    proposal.account_sha256 = digest(account)
    args = parser().parse_args(inputs(tmp_path, case))
    assert run(args) == 2
    account.equity = account.free_cash = 10000
    proposal.account_sha256 = digest(account)
    write_json(tmp_path / "account.json", account)
    write_json(tmp_path / "proposal.json", proposal)
    assert run(args) == 2
    assert "account_lockout_persisted_in_journal" in read_json(tmp_path / "risk.json")["reasons"]
    store = Store(tmp_path / "lab.sqlite")
    try:
        assert len([e for e in store.events() if e["kind"] == "risk_lock"]) == 1
    finally:
        store.close()


def test_max_drawdown_latch_survives_daily_reset(tmp_path, case, monkeypatch):
    monkeypatch.setattr(research_lab.risk, "utcnow", lambda: case[0])
    _, _, _, account, proposal, _ = case
    account.peak_equity = 12000
    proposal.account_sha256 = digest(account)
    args = parser().parse_args(inputs(tmp_path, case))
    assert run(args) == 2
    store = Store(tmp_path / "lab.sqlite")
    try:
        events = store.events()
        assert any(e["kind"] == "drawdown_lock" for e in events)
    finally:
        store.close()
    # Simulate a new day with recovered equity. A drawdown breach cannot be auto-reset.
    tomorrow = case[0] + timedelta(days=1)
    monkeypatch.setattr(research_lab.risk, "utcnow", lambda: tomorrow)
    account.day_start += timedelta(days=1)
    account.as_of = tomorrow
    account.equity = account.free_cash = account.peak_equity = 12000
    proposal.account_sha256 = digest(account)
    write_json(tmp_path / "account.json", account)
    write_json(tmp_path / "proposal.json", proposal)
    assert run(args) == 2
    assert "account_lockout_persisted_in_journal" in read_json(tmp_path / "risk.json")["reasons"]
