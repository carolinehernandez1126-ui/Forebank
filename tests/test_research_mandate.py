from datetime import timedelta

import pytest
from pydantic import ValidationError

import research_lab.decision
import research_lab.risk
from research_lab.cli import parser, run
from research_lab.decision import decide
from research_lab.io import digest, policy, read_json, write_json
from research_lab.models import Proposal, ResearchGap, RiskPolicy
from research_lab.risk import assess, budget
from research_lab.summary import trading_summary


def rebind(case):
    _, data, p, account, proposal, reviews = case
    proposal.dataset_sha256 = digest(data)
    proposal.policy_sha256 = digest(p)
    proposal.account_sha256 = digest(account)
    for review in reviews:
        review.proposal_sha256 = digest(proposal)


def test_fifty_thousand_policy_has_two_distinct_safety_layers(case):
    _, data, _, account, _, _ = case
    p = policy()
    account.day_start_equity = account.equity = account.peak_equity = account.free_cash = 50000
    b = budget(account, p, "DEMO/USD", 100, 95, data)
    assert p.initial_capital == 50000
    assert b["hard_daily_floor"] == 48500
    assert b["daily_floor"] == 49000
    assert b["hard_drawdown_floor"] == 47000
    assert b["drawdown_floor"] == 48000
    assert b["daily_reserve"] == 200
    assert b["available_new_risk"] == 125
    assert p.max_total_stop_risk_fraction * account.equity == 250


@pytest.mark.parametrize(
    "field,value",
    [
        ("daily_loss_fraction", 0.03),
        ("daily_loss_fraction", 0.04),
        ("max_drawdown_fraction", 0.06),
        ("max_drawdown_fraction", 0.07),
    ],
)
def test_operational_limits_cannot_consume_hard_ceiling(field, value):
    values = RiskPolicy().model_dump()
    values[field] = value
    with pytest.raises(ValidationError, match="strictly below"):
        RiskPolicy.model_validate(values)


@pytest.mark.parametrize(
    "field,value", [("hard_daily_loss_fraction", 0.031), ("hard_max_drawdown_fraction", 0.061)]
)
def test_config_cannot_raise_the_owners_absolute_ceiling(field, value):
    values = RiskPolicy().model_dump()
    values[field] = value
    with pytest.raises(ValidationError):
        RiskPolicy.model_validate(values)


def test_daily_operating_stop_triggers_before_hard_limit(case):
    now, data, p, account, proposal, _ = case
    p.daily_loss_fraction = 0.02
    p.initial_capital = 50000
    account.day_start_equity = account.peak_equity = 50000
    account.equity = account.free_cash = 49000
    rebind(case)
    result = assess(proposal, account, p, data, now)
    assert "daily_loss_breached" in result["reasons"]
    assert "hard_daily_loss_breached" not in result["reasons"]


def test_drawdown_operating_stop_triggers_before_hard_limit(case):
    now, data, p, account, proposal, _ = case
    p.initial_capital = 50000
    account.day_start_equity = account.equity = account.free_cash = 48000
    account.peak_equity = 50000
    rebind(case)
    result = assess(proposal, account, p, data, now)
    assert "max_drawdown_breached" in result["reasons"]
    assert "hard_max_drawdown_breached" not in result["reasons"]


def test_drawdown_floor_does_not_fall_below_initial_capital_reference(case):
    _, data, p, account, _, _ = case
    p.initial_capital = 50000
    account.equity = account.free_cash = account.peak_equity = account.day_start_equity = 49000
    assert budget(account, p, "DEMO/USD", 100, 95, data)["drawdown_floor"] == 48000


@pytest.mark.parametrize(
    "severity,accepted,ready",
    [
        ("material", True, True),
        ("material", False, False),
        ("critical", True, False),
        ("critical", False, False),
        ("minor", False, True),
    ],
)
def test_accepted_incomplete_information_can_be_actionable(case, severity, accepted, ready):
    now, data, p, account, proposal, reviews = case
    proposal.research.gaps = [
        ResearchGap(
            description="Holder concentration breakdown is incomplete",
            severity=severity,
            impact="Concentration could amplify adverse price jumps and exit slippage.",
            mitigation="Limit position size and re-evaluate on new evidence; do not invent missing data.",
            accepted=accepted,
        )
    ]
    rebind(case)
    result = decide(proposal, reviews, account, p, data, now)
    assert (result["status"] == "READY_FOR_MANUAL_EXECUTION") == ready
    if ready:
        assert result["research_assessment"]["total_gaps"] == 1


@pytest.mark.parametrize("flag", ["uncertainty_accepted", "strategy_coherence_confirmed"])
def test_both_reviewers_must_assess_uncertainty_and_coherence(case, flag):
    now, data, p, account, proposal, reviews = case
    setattr(reviews[1], flag, False)
    assert decide(proposal, reviews, account, p, data, now)["status"] == "WAIT"


def test_missing_research_cannot_be_replaced_by_long_thesis(case):
    values = case[4].model_dump()
    del values["research"]
    with pytest.raises(ValidationError):
        Proposal.model_validate(values)


def test_research_cutoff_cannot_be_after_frozen_plan(case):
    now, data, p, account, proposal, reviews = case
    proposal.research.cutoff_at = now + timedelta(seconds=1)
    rebind(case)
    assert (
        "research_cutoff_after_proposal"
        in decide(proposal, reviews, account, p, data, now)["reasons"]
    )


def test_report_preserves_reasoning_alternatives_sources_and_risk(case):
    now, data, p, account, proposal, reviews = case
    decision = decide(proposal, reviews, account, p, data, now)
    report = trading_summary(proposal, reviews, decision)
    for text in (
        proposal.technical_summary,
        proposal.fundamental_summary,
        proposal.statistical_summary,
        proposal.research.stopping_reason,
        proposal.research.strategy_coherence,
        proposal.research.alternatives_considered[0],
        proposal.evidence[0].url,
        reviews[1].rationale,
        "Floor MDL operativo",
        "Floor MDD máximo",
        "READY_FOR_MANUAL_EXECUTION",
    ):
        assert text in report


def test_decide_cli_writes_a_detailed_memo_even_when_waiting(tmp_path, case, monkeypatch):
    monkeypatch.setattr(research_lab.risk, "utcnow", lambda: case[0])
    monkeypatch.setattr(research_lab.decision, "utcnow", lambda: case[0])
    _, data, _, account, proposal, reviews = case
    reviews[1].verdict = "reject"
    config = tmp_path / "lab.toml"
    config.write_text(
        "[risk]\npolicy_verified=true\ninitial_capital=10000\ndaily_loss_fraction=0.01\n[research]\n"
    )
    for name, value in [
        ("dataset", data),
        ("account", account),
        ("proposal", proposal),
        ("codex", reviews[0]),
        ("claude", reviews[1]),
    ]:
        write_json(tmp_path / f"{name}.json", value)
    args = parser().parse_args(
        [
            "--config",
            str(config),
            "--db",
            str(tmp_path / "lab.sqlite"),
            "decide",
            "--proposal",
            str(tmp_path / "proposal.json"),
            "--dataset",
            str(tmp_path / "dataset.json"),
            "--account",
            str(tmp_path / "account.json"),
            "--reviews",
            str(tmp_path / "codex.json"),
            str(tmp_path / "claude.json"),
            "--output",
            str(tmp_path / "decision.json"),
        ]
    )
    assert run(args) == 2
    assert read_json(tmp_path / "decision.json")["status"] == "WAIT"
    memo = (tmp_path / "decision.md").read_text(encoding="utf-8")
    assert "WAIT" in memo and "claude" in memo and proposal.thesis in memo
