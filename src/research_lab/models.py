from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, model_validator


class Model(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)


class Candle(Model):
    timestamp: AwareDatetime
    open: float = Field(gt=0)
    high: float = Field(gt=0)
    low: float = Field(gt=0)
    close: float = Field(gt=0)
    volume: float = Field(ge=0)

    @model_validator(mode="after")
    def geometry(self):
        if self.high < max(self.open, self.close, self.low):
            raise ValueError("high below OHLC")
        if self.low > min(self.open, self.close, self.high):
            raise ValueError("low above OHLC")
        return self


class Instrument(Model):
    symbol: str
    pair: str
    base: str
    quote: str
    status: str
    min_quantity: float = Field(gt=0)
    min_cost: float = Field(ge=0)
    quantity_decimals: int = Field(ge=0, le=18)
    price_decimals: int = Field(ge=0, le=18)
    tick_size: float = Field(gt=0)


class Quote(Model):
    as_of: AwareDatetime
    bid: float = Field(gt=0)
    ask: float = Field(gt=0)
    ask_depth_near_quote: float = Field(ge=0)

    @model_validator(mode="after")
    def ordered(self):
        if self.ask < self.bid:
            raise ValueError("crossed quote")
        return self


class Dataset(Model):
    schema_version: str = "1"
    created_at: AwareDatetime
    synthetic: bool = False
    instrument: Instrument
    quote: Quote
    candles: dict[int, list[Candle]] = Field(min_length=1)
    fundamentals: dict = Field(default_factory=dict)
    provenance: list[dict] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def valid_timeframes(self):
        supported = {1, 5, 15, 30, 60, 240, 1440, 10080, 21600}
        if not set(self.candles) <= supported or any(not rows for rows in self.candles.values()):
            raise ValueError("Unsupported interval or empty candles")
        return self


class Position(Model):
    # Every held asset and pending order must be represented. One currency throughout.
    symbol: str
    gross_notional: float = Field(ge=0)
    additional_stop_risk: float = Field(ge=0)
    protected: bool


class Account(Model):
    account_id: str
    currency: str
    as_of: AwareDatetime
    day_start: AwareDatetime
    verified: bool = False
    reconciled: bool = False
    day_start_equity: float = Field(gt=0)
    equity: float = Field(gt=0)
    peak_equity: float = Field(gt=0)
    free_cash: float = Field(ge=0)
    net_external_flows_today: float = 0
    daily_lockout: bool = False
    positions: list[Position] = Field(default_factory=list)

    @model_validator(mode="after")
    def consistent(self):
        if self.peak_equity < self.equity:
            raise ValueError("peak_equity must include current equity")
        if self.free_cash > self.equity:
            raise ValueError("spot free_cash cannot exceed equity")
        return self


class RiskPolicy(Model):
    account_mode: Literal["own_capital_spot"] = "own_capital_spot"
    quote_currency: str = "USD"
    policy_verified: bool = False
    initial_capital: float = Field(default=50000, gt=0)
    hard_daily_loss_fraction: float = Field(default=0.03, gt=0, le=0.03)
    hard_max_drawdown_fraction: float = Field(default=0.06, gt=0, le=0.06)
    min_bars: int = Field(default=250, ge=201)
    required_intervals: list[int] = Field(default_factory=lambda: [60, 240, 1440], min_length=1)
    daily_loss_fraction: float = Field(default=0.02, gt=0, lt=1)
    per_trade_fraction: float = Field(default=0.0025, gt=0, lt=1)
    max_total_stop_risk_fraction: float = Field(default=0.005, gt=0, lt=1)
    max_gross_exposure_fraction: float = Field(default=0.5, gt=0, le=1)
    max_asset_exposure_fraction: float = Field(default=0.2, gt=0, le=1)
    max_drawdown_fraction: float = Field(default=0.04, gt=0, lt=1)
    safety_buffer_fraction: float = Field(default=0.2, ge=0, lt=1)
    min_reward_risk: float = Field(default=2, gt=0)
    fee_bps_per_side: float = Field(default=40, ge=0, lt=10000)
    slippage_bps_per_side: float = Field(default=15, ge=0, lt=10000)
    max_spread_bps: float = Field(default=20, gt=0)
    max_entry_deviation_fraction: float = Field(default=0.01, gt=0, lt=1)
    max_depth_participation_fraction: float = Field(default=0.01, gt=0, le=1)
    max_account_age_seconds: int = Field(default=300, gt=0)
    max_market_age_seconds: int = Field(default=120, gt=0)
    max_review_age_seconds: int = Field(default=3600, gt=0)
    max_plan_lifetime_seconds: int = Field(default=3600, gt=0)
    daily_reset_utc: str = "00:00"

    @model_validator(mode="after")
    def reset(self):
        datetime.strptime(self.daily_reset_utc, "%H:%M")
        if self.per_trade_fraction > self.max_total_stop_risk_fraction:
            raise ValueError("per trade exceeds total risk cap")
        if self.daily_loss_fraction >= self.hard_daily_loss_fraction:
            raise ValueError("operational MDL must be strictly below hard MDL")
        if self.max_drawdown_fraction >= self.hard_max_drawdown_fraction:
            raise ValueError("operational MDD must be strictly below hard MDD")
        if not set(self.required_intervals) <= {1, 5, 15, 30, 60, 240, 1440, 10080, 21600}:
            raise ValueError("Unsupported required interval")
        return self


class Evidence(Model):
    url: str = Field(pattern=r"^https://[^\s]+$")
    title: str = Field(min_length=3)
    retrieved_at: AwareDatetime
    published_at: AwareDatetime | None = None
    dimension: Literal["technical", "fundamental", "statistical", "macro", "catalyst"]
    claim: str = Field(min_length=10)


class ResearchGap(Model):
    description: str = Field(min_length=15)
    severity: Literal["critical", "material", "minor"]
    impact: str = Field(min_length=20)
    mitigation: str = Field(min_length=20)
    accepted: bool


class ResearchConclusion(Model):
    horizon: str = Field(min_length=10)
    scope: str = Field(min_length=30)
    cutoff_at: AwareDatetime
    stopping_reason: str = Field(min_length=40)
    sufficiency_rationale: str = Field(min_length=60)
    decision_with_available_information: bool
    alternatives_considered: list[str] = Field(min_length=2)
    strategy_coherence: str = Field(min_length=60)
    execution_rules: str = Field(min_length=40)
    scenario_analysis: str = Field(min_length=40)
    monitoring_plan: str = Field(min_length=30)
    gaps: list[ResearchGap]


class Proposal(Model):
    schema_version: Literal["2"] = "2"
    plan_id: str = Field(min_length=3)
    created_at: AwareDatetime
    expires_at: AwareDatetime
    symbol: str
    side: Literal["buy"] = "buy"
    dataset_sha256: str = Field(pattern=r"^[a-f0-9]{64}$")
    account_sha256: str = Field(pattern=r"^[a-f0-9]{64}$")
    policy_sha256: str = Field(pattern=r"^[a-f0-9]{64}$")
    entry: float = Field(gt=0)
    stop: float = Field(gt=0)
    target: float = Field(gt=0)
    quantity: float = Field(gt=0)
    thesis: str = Field(min_length=20)
    invalidation: str = Field(min_length=20)
    technical_summary: str = Field(min_length=20)
    fundamental_summary: str = Field(min_length=20)
    statistical_summary: str = Field(min_length=20)
    evidence: list[Evidence] = Field(min_length=3)
    limitations: list[str] = Field(min_length=1)
    research: ResearchConclusion

    @model_validator(mode="after")
    def coherent(self):
        if not self.stop < self.entry < self.target:
            raise ValueError("buy requires stop < entry < target")
        if self.expires_at <= self.created_at:
            raise ValueError("invalid plan lifetime")
        dimensions = {e.dimension for e in self.evidence}
        if not {"technical", "fundamental", "statistical"} <= dimensions:
            raise ValueError("evidence must cover technical, fundamental and statistical")
        return self


class Review(Model):
    reviewer: Literal["codex", "claude"]
    model: str = Field(min_length=2)
    reviewed_at: AwareDatetime
    proposal_sha256: str = Field(pattern=r"^[a-f0-9]{64}$")
    verdict: Literal["approve", "reject", "abstain"]
    rationale: str = Field(min_length=30)
    independently_checked_sources: list[str] = Field(min_length=1)
    blockers: list[str] = Field(default_factory=list)
    uncertainty_accepted: bool = False
    strategy_coherence_confirmed: bool = False
