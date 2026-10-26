from datetime import UTC, datetime, timedelta

import pytest

from research_lab.demo import synthetic_dataset
from research_lab.io import digest
from research_lab.models import Account, Proposal, Review, RiskPolicy


@pytest.fixture
def case():
    now = datetime(2026, 1, 1, 12, tzinfo=UTC)
    data = synthetic_dataset(now).model_copy(deep=True)
    data.synthetic = False  # Test fixture only; never relabel real demo outputs.
    data.quote.ask = 100
    data.quote.bid = 99.99
    policy = RiskPolicy(policy_verified=True, initial_capital=10000, daily_loss_fraction=0.01)
    account = Account(
        account_id="test",
        currency="USD",
        as_of=now,
        day_start=now.replace(hour=0),
        verified=True,
        reconciled=True,
        day_start_equity=10000,
        equity=10000,
        peak_equity=10000,
        free_cash=10000,
    )
    evidence = [
        {
            "url": "https://example.org/" + dim,
            "title": "Fixture evidence",
            "retrieved_at": now,
            "dimension": dim,
            "claim": "Fixture claim for a unit test",
        }
        for dim in ("technical", "fundamental", "statistical")
    ]
    proposal = Proposal(
        plan_id="test-plan",
        created_at=now,
        expires_at=now + timedelta(minutes=30),
        symbol="DEMO/USD",
        entry=100,
        stop=95,
        target=120,
        quantity=1,
        dataset_sha256=digest(data),
        account_sha256=digest(account),
        policy_sha256=digest(policy),
        thesis="Fixture thesis with required detail",
        invalidation="Fixture invalidation with required detail",
        technical_summary="Fixture technical summary for test",
        fundamental_summary="Fixture fundamental summary for test",
        statistical_summary="Fixture statistical summary for test",
        evidence=evidence,
        limitations=["Test only"],
        research={
            "horizon": "Fixture horizon: several days",
            "scope": "Fixture scope covers technical, fundamental and statistical research.",
            "cutoff_at": now,
            "stopping_reason": "Fixture stopping rule: sufficient independent evidence and no critical gaps.",
            "sufficiency_rationale": "Fixture evidence covers the decision drivers; remaining uncertainty is bounded by risk controls.",
            "decision_with_available_information": True,
            "alternatives_considered": [
                "Stay in cash given no actionable setup",
                "Wait for further price confirmation",
            ],
            "strategy_coherence": "Fixture entry, stop, target, horizon and costs all correspond to the same documented strategy.",
            "execution_rules": "Fixture: execute only after approval, with protective stop and expiry.",
            "scenario_analysis": "Fixture: assess favorable, adverse and sideways conditions without invented probabilities.",
            "monitoring_plan": "Fixture: recheck market conditions and invalidate on adverse material evidence.",
            "gaps": [],
        },
    )
    reviews = [
        Review(
            reviewer=name,
            model="test-model",
            reviewed_at=now,
            proposal_sha256=digest(proposal),
            verdict="approve",
            rationale="Fixture independent rationale for this test only",
            independently_checked_sources=[evidence[0]["url"]],
            uncertainty_accepted=True,
            strategy_coherence_confirmed=True,
        )
        for name in ("codex", "claude")
    ]
    return now, data, policy, account, proposal, reviews
