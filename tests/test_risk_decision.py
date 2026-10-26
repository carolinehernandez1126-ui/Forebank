from datetime import timedelta

import pytest
from pydantic import ValidationError

from research_lab.decision import decide
from research_lab.io import digest
from research_lab.models import Position, Proposal
from research_lab.risk import assess, trading_day


def checked(case):
    now, data, policy, account, proposal, reviews = case
    return assess(proposal, account, policy, data, now)


def test_valid_case_requires_all_controls_and_both_reviews(case):
    now, data, policy, account, proposal, reviews = case
    assert checked(case)["passed"]
    result = decide(proposal, reviews, account, policy, data, now)
    assert result["status"] == "READY_FOR_MANUAL_EXECUTION"
    assert result["expires_at"] == (now + timedelta(seconds=120)).isoformat()


@pytest.mark.parametrize(
    "which", ["missing", "duplicate", "reject", "abstain", "blocker", "hash", "stale", "future"]
)
def test_no_consensus_is_wait(case, which):
    now, data, policy, account, proposal, reviews = case
    if which == "missing":
        reviews = reviews[:1]
    elif which == "duplicate":
        reviews = [reviews[0], reviews[0]]
    elif which in {"reject", "abstain"}:
        reviews[1].verdict = which
    elif which == "blocker":
        reviews[1].blockers = ["Unverified catalyst"]
    elif which == "hash":
        reviews[1].proposal_sha256 = "0" * 64
    elif which == "stale":
        reviews[1].reviewed_at = now - timedelta(hours=2)
    else:
        reviews[1].reviewed_at = now + timedelta(seconds=1)
    assert decide(proposal, reviews, account, policy, data, now)["status"] == "WAIT"


@pytest.mark.parametrize(
    "issue,expected",
    [
        ("policy", "policy_unverified"),
        ("account", "account_unverified_or_unreconciled"),
        ("stale", "account_stale_or_future"),
        ("market", "market_stale_or_future"),
        ("synthetic", "synthetic_data"),
        ("currency", "currency_mismatch_no_implicit_fx"),
        ("lockout", "daily_lockout_latched"),
        ("day", "wrong_daily_baseline"),
        ("daily", "daily_loss_breached"),
        ("drawdown", "max_drawdown_breached"),
        ("qty", "quantity_exceeds_safe_budget"),
        ("rr", "net_reward_risk_too_low"),
        ("stop", "unprotected_position_or_order"),
        ("tick", "price_tick_invalid"),
        ("depth", "quantity_exceeds_safe_budget"),
        ("gap", "candle_quality:60:gaps_or_irregular_intervals"),
    ],
)
def test_fail_closed_controls(case, issue, expected):
    now, data, policy, account, proposal, reviews = case
    if issue == "policy":
        policy.policy_verified = False
    elif issue == "account":
        account.verified = False
    elif issue == "stale":
        account.as_of -= timedelta(minutes=6)
    elif issue == "market":
        data.quote.as_of -= timedelta(minutes=3)
    elif issue == "synthetic":
        data.synthetic = True
    elif issue == "currency":
        account.currency = "EUR"
    elif issue == "lockout":
        account.daily_lockout = True
    elif issue == "day":
        account.day_start -= timedelta(days=1)
    elif issue == "daily":
        account.equity, account.free_cash = 9900, 9900
    elif issue == "drawdown":
        account.peak_equity = 12000
    elif issue == "qty":
        proposal.quantity = 100
    elif issue == "rr":
        proposal.target = 102
    elif issue == "stop":
        account.positions = [
            Position(
                symbol="BTC/USD", gross_notional=100, additional_stop_risk=100, protected=False
            )
        ]
    elif issue == "tick":
        proposal.entry = 100.001
    elif issue == "depth":
        data.quote.ask_depth_near_quote = 1
    elif issue == "gap":
        del data.candles[60][200]
    # Rebind to test the control itself, not just the hash protections.
    proposal.account_sha256, proposal.dataset_sha256 = digest(account), digest(data)
    proposal.policy_sha256 = digest(policy)
    result = checked(case)
    assert not result["passed"]
    assert expected in result["reasons"]


def test_open_and_pending_risk_reserves_daily_headroom(case):
    now, data, policy, account, proposal, _ = case
    account.equity = account.free_cash = 9950
    account.positions = [
        Position(symbol="BTC/USD", gross_notional=1000, additional_stop_risk=25, protected=True)
    ]
    proposal.account_sha256 = digest(account)
    result = checked(case)
    # Daily room=50; reserve=20; existing risk=25; only 5 remains (< 6.0725 unit loss).
    assert result["budget"]["available_new_risk"] == 5
    assert "quantity_exceeds_safe_budget" in result["reasons"]


def test_deposit_does_not_hide_daily_loss(case):
    _, _, _, account, proposal, _ = case
    account.equity = account.free_cash = 10900
    account.peak_equity = 11000
    account.net_external_flows_today = 1000
    proposal.account_sha256 = digest(account)
    assert "daily_loss_breached" in checked(case)["reasons"]


def test_changing_plan_invalidates_both_reviews(case):
    now, data, policy, account, proposal, reviews = case
    proposal.quantity = 0.5
    assert all(
        "proposal_hash_mismatch" in r
        for r in decide(proposal, reviews, account, policy, data, now)["reasons"]
    )


def test_daily_reset_exact_boundary(case):
    now = case[0].replace(hour=0, minute=29)
    assert trading_day(now, "00:30").day == 31
    assert trading_day(now + timedelta(minutes=1), "00:30").day == 1


def test_nan_and_short_proposals_are_rejected(case):
    proposal = case[4].model_dump()
    proposal["entry"] = float("nan")
    with pytest.raises(ValidationError):
        Proposal.model_validate(proposal)
    proposal["entry"] = 100
    proposal["side"] = "sell"
    with pytest.raises(ValidationError):
        Proposal.model_validate(proposal)


def test_required_timeframes_cannot_be_dropped(case):
    _, data, _, _, proposal, _ = case
    del data.candles[1440]
    proposal.dataset_sha256 = digest(data)
    assert "required_timeframes_missing" in checked(case)["reasons"]


def test_history_requirement_is_bound_to_policy(case):
    now, data, policy, account, proposal, _ = case
    policy.min_bars = 800
    proposal.policy_sha256 = digest(policy)
    result = assess(proposal, account, policy, data, now, min_bars=1)
    assert any("insufficient_bars" in r for r in result["reasons"])


def test_decision_expires_when_either_review_expires(case):
    now, data, policy, account, proposal, reviews = case
    policy.max_review_age_seconds = 1
    proposal.policy_sha256 = digest(policy)
    for review in reviews:
        review.proposal_sha256 = digest(proposal)
    result = decide(proposal, reviews, account, policy, data, now)
    assert result["status"] == "READY_FOR_MANUAL_EXECUTION"
    assert result["expires_at"] == (now + timedelta(seconds=1)).isoformat()


def test_quote_at_exact_expiry_is_already_stale(case):
    _, data, policy, _, proposal, _ = case
    data.quote.as_of -= timedelta(seconds=policy.max_market_age_seconds)
    proposal.dataset_sha256 = digest(data)
    assert "market_stale_or_future" in checked(case)["reasons"]
