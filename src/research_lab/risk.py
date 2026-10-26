from __future__ import annotations

from datetime import UTC, timedelta
from decimal import ROUND_DOWN, Decimal

from .analytics import quality
from .io import digest, utcnow


def trading_day(now, reset="00:00"):
    hour, minute = map(int, reset.split(":"))
    start = now.astimezone(UTC).replace(hour=hour, minute=minute, second=0, microsecond=0)
    return start if now >= start else start - timedelta(days=1)


def fresh(stamp, now, max_seconds):
    return 0 <= (now - stamp).total_seconds() < max_seconds


def round_quantity(quantity, decimals):
    step = Decimal(1).scaleb(-decimals)
    return float(Decimal(str(max(0, quantity))).quantize(step, rounding=ROUND_DOWN))


def tick_aligned(price, tick):
    return Decimal(str(price)) % Decimal(str(tick)) == 0


def budget(account, policy, symbol, entry, stop, dataset):
    cost_rate = (policy.fee_bps_per_side + policy.slippage_bps_per_side) / 10000
    unit_loss = entry - stop + (entry + stop) * cost_rate
    floor = account.day_start_equity * (1 - policy.daily_loss_fraction)
    hard_daily_floor = account.day_start_equity * (1 - policy.hard_daily_loss_fraction)
    reserve = account.day_start_equity * policy.daily_loss_fraction * policy.safety_buffer_fraction
    adjusted_equity = account.equity - account.net_external_flows_today
    used_risk = sum(p.additional_stop_risk for p in account.positions)
    gross = sum(p.gross_notional for p in account.positions)
    asset_gross = sum(p.gross_notional for p in account.positions if p.symbol == symbol)
    drawdown_reference = max(policy.initial_capital, account.peak_equity)
    drawdown_floor = drawdown_reference * (1 - policy.max_drawdown_fraction)
    hard_drawdown_floor = drawdown_reference * (1 - policy.hard_max_drawdown_fraction)
    available = min(
        account.equity * policy.per_trade_fraction,
        adjusted_equity - floor - reserve - used_risk,
        account.equity * policy.max_total_stop_risk_fraction - used_risk,
        account.equity - drawdown_floor - reserve - used_risk,
        adjusted_equity - hard_daily_floor - reserve - used_risk,
        account.equity - hard_drawdown_floor - reserve - used_risk,
    )
    exposure_room = min(
        account.equity * policy.max_gross_exposure_fraction - gross,
        account.equity * policy.max_asset_exposure_fraction - asset_gross,
    )
    depth_room = dataset.quote.ask_depth_near_quote * policy.max_depth_participation_fraction
    max_quantity = max(
        0,
        min(
            available / unit_loss if unit_loss > 0 else 0,
            exposure_room / entry,
            account.free_cash / (entry * (1 + cost_rate)),
            depth_room / entry,
        ),
    )
    return {
        "unit_loss_with_costs": unit_loss,
        "available_new_risk": max(0, available),
        "daily_floor": floor,
        "hard_daily_floor": hard_daily_floor,
        "drawdown_reference": drawdown_reference,
        "drawdown_floor": drawdown_floor,
        "hard_drawdown_floor": hard_drawdown_floor,
        "operational_daily_loss_fraction": policy.daily_loss_fraction,
        "hard_daily_loss_fraction": policy.hard_daily_loss_fraction,
        "operational_drawdown_fraction": policy.max_drawdown_fraction,
        "hard_drawdown_fraction": policy.hard_max_drawdown_fraction,
        "daily_operating_headroom": adjusted_equity - floor,
        "drawdown_operating_headroom": account.equity - drawdown_floor,
        "daily_reserve": reserve,
        "adjusted_equity": adjusted_equity,
        "open_and_pending_stop_risk": used_risk,
        "gross_exposure": gross,
        "asset_exposure": asset_gross,
        "max_quantity": round_quantity(max_quantity, dataset.instrument.quantity_decimals),
    }


def assess(proposal, account, policy, dataset, now=None, min_bars=250):
    now = now or utcnow()
    min_bars = max(min_bars, policy.min_bars)
    reasons = []

    def require(condition, reason):
        if not condition:
            reasons.append(reason)

    require(policy.policy_verified, "policy_unverified")
    require(account.verified and account.reconciled, "account_unverified_or_unreconciled")
    require(not account.daily_lockout, "daily_lockout_latched")
    require(fresh(account.as_of, now, policy.max_account_age_seconds), "account_stale_or_future")
    require(account.day_start == trading_day(now, policy.daily_reset_utc), "wrong_daily_baseline")
    require(account.as_of >= account.day_start, "account_precedes_daily_baseline")
    require(
        fresh(dataset.quote.as_of, now, policy.max_market_age_seconds), "market_stale_or_future"
    )
    require(not dataset.synthetic, "synthetic_data")
    require(dataset.created_at <= now, "dataset_created_in_future")
    require(dataset.instrument.status == "online", "instrument_not_online")
    require(
        account.currency == policy.quote_currency == dataset.instrument.quote,
        "currency_mismatch_no_implicit_fx",
    )
    require(proposal.symbol == dataset.instrument.symbol, "symbol_mismatch")
    require(proposal.dataset_sha256 == digest(dataset), "dataset_hash_mismatch")
    require(proposal.account_sha256 == digest(account), "account_hash_mismatch")
    require(proposal.policy_sha256 == digest(policy), "policy_hash_mismatch")
    require(proposal.created_at <= now < proposal.expires_at, "plan_expired_or_future")
    require(
        (proposal.expires_at - proposal.created_at).total_seconds()
        <= policy.max_plan_lifetime_seconds,
        "plan_lifetime_too_long",
    )
    for evidence in proposal.evidence:
        require(fresh(evidence.retrieved_at, now, 7 * 86400), "evidence_stale_or_future")
        if evidence.published_at:
            require(
                evidence.published_at <= evidence.retrieved_at, "evidence_publication_in_future"
            )
    require(bool(dataset.candles), "no_candles")
    require(set(policy.required_intervals) <= set(dataset.candles), "required_timeframes_missing")
    for interval, candles in dataset.candles.items():
        if not candles:
            require(False, f"empty_candles:{interval}")
            continue
        q = quality(candles, interval, now, min_bars)
        require(q["passed"], f"candle_quality:{interval}:{','.join(q['reasons'])}")
    require(all(p.protected for p in account.positions), "unprotected_position_or_order")
    mid = (dataset.quote.ask + dataset.quote.bid) / 2
    spread_bps = (dataset.quote.ask - dataset.quote.bid) / mid * 10000
    require(spread_bps <= policy.max_spread_bps, "spread_exceeds_limit")
    require(
        abs(proposal.entry / dataset.quote.ask - 1) <= policy.max_entry_deviation_fraction,
        "entry_too_far_from_current_ask",
    )
    instrument = dataset.instrument
    require(
        all(
            tick_aligned(p, instrument.tick_size)
            for p in (proposal.entry, proposal.stop, proposal.target)
        ),
        "price_tick_invalid",
    )
    require(
        Decimal(str(proposal.quantity))
        == Decimal(str(round_quantity(proposal.quantity, instrument.quantity_decimals))),
        "quantity_precision_invalid",
    )
    require(proposal.quantity >= instrument.min_quantity, "below_min_quantity")
    require(proposal.quantity * proposal.entry >= instrument.min_cost, "below_min_cost")
    b = budget(account, policy, proposal.symbol, proposal.entry, proposal.stop, dataset)
    require(b["adjusted_equity"] > b["daily_floor"], "daily_loss_breached")
    require(
        account.equity > b["drawdown_floor"],
        "max_drawdown_breached",
    )
    require(b["adjusted_equity"] > b["hard_daily_floor"], "hard_daily_loss_breached")
    require(account.equity > b["hard_drawdown_floor"], "hard_max_drawdown_breached")
    require(b["available_new_risk"] > 0, "no_risk_budget")
    require(proposal.quantity <= b["max_quantity"], "quantity_exceeds_safe_budget")
    rate = (policy.fee_bps_per_side + policy.slippage_bps_per_side) / 10000
    net_reward = proposal.target - proposal.entry - (proposal.target + proposal.entry) * rate
    rr = net_reward / b["unit_loss_with_costs"]
    require(rr >= policy.min_reward_risk, "net_reward_risk_too_low")
    return {
        "passed": not reasons,
        "reasons": sorted(set(reasons)),
        "checked_at": now.isoformat(),
        "proposal_sha256": digest(proposal),
        "risk_amount": proposal.quantity * b["unit_loss_with_costs"],
        "net_reward_risk": rr,
        "spread_bps": spread_bps,
        "budget": b,
        "notice": "Pre-trade estimate only. Gaps and manual execution can exceed modeled loss.",
    }
