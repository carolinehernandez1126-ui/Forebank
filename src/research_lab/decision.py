from __future__ import annotations

from datetime import timedelta

from .io import digest, utcnow
from .risk import assess, fresh, trading_day


def decide(proposal, reviews, account, policy, dataset, now=None, min_bars=250):
    now = now or utcnow()
    risk = assess(proposal, account, policy, dataset, now, min_bars)
    reasons = list(risk["reasons"])
    research = proposal.research
    if not research.decision_with_available_information:
        reasons.append("research_not_sufficient_for_decision")
    if research.cutoff_at > proposal.created_at:
        reasons.append("research_cutoff_after_proposal")
    for index, gap in enumerate(research.gaps):
        if gap.severity == "critical":
            reasons.append(f"critical_research_gap:{index}")
        elif gap.severity == "material" and not gap.accepted:
            reasons.append(f"unaccepted_material_research_gap:{index}")
    if sorted(r.reviewer for r in reviews) != ["claude", "codex"]:
        reasons.append("exactly_one_codex_and_one_claude_review_required")
    evidence_urls = {e.url for e in proposal.evidence}
    for review in reviews:
        prefix = review.reviewer + ":"
        if review.proposal_sha256 != digest(proposal):
            reasons.append(prefix + "proposal_hash_mismatch")
        if review.verdict != "approve" or review.blockers:
            reasons.append(prefix + "not_approved_or_has_blockers")
        if not review.uncertainty_accepted:
            reasons.append(prefix + "uncertainty_not_accepted")
        if not review.strategy_coherence_confirmed:
            reasons.append(prefix + "strategy_coherence_not_confirmed")
        if not fresh(review.reviewed_at, now, policy.max_review_age_seconds):
            reasons.append(prefix + "stale_or_future_review")
        if review.reviewed_at < proposal.created_at:
            reasons.append(prefix + "review_predates_proposal")
        if not evidence_urls.intersection(review.independently_checked_sources):
            reasons.append(prefix + "no_proposal_source_checked")
    expiry_candidates = [
        proposal.expires_at,
        account.as_of + timedelta(seconds=policy.max_account_age_seconds),
        dataset.quote.as_of + timedelta(seconds=policy.max_market_age_seconds),
        trading_day(now, policy.daily_reset_utc) + timedelta(days=1),
    ]
    expiry_candidates.extend(
        r.reviewed_at + timedelta(seconds=policy.max_review_age_seconds) for r in reviews
    )
    expiry_candidates.extend(e.retrieved_at + timedelta(days=7) for e in proposal.evidence)
    return {
        "schema_version": "2",
        "status": "WAIT" if reasons else "READY_FOR_MANUAL_EXECUTION",
        "checked_at": now.isoformat(),
        "expires_at": min(expiry_candidates).isoformat(),
        "proposal_sha256": digest(proposal),
        "reviews_sha256": [digest(r) for r in reviews],
        "reasons": sorted(set(reasons)),
        "risk": risk,
        "research_assessment": {
            "cutoff_at": research.cutoff_at.isoformat(),
            "stopping_reason": research.stopping_reason,
            "sufficiency_rationale": research.sufficiency_rationale,
            "accepted_gaps": sum(g.accepted for g in research.gaps),
            "total_gaps": len(research.gaps),
        },
        "identity_assurance": "Self-attested review files. GitHub review permissions must verify authorship.",
        "execution": "Human rechecks live account/market and manually enters order + protective stop.",
    }
