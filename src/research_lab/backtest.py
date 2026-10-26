from __future__ import annotations

import numpy as np
import pandas as pd


def simulate(df, fast=20, slow=50, fee_bps=40, slippage_bps=15, initial_equity=1.0):
    """Long/flat EMA baseline. Signal at close[t-1], fill at open[t], cash-funded.

    Fractions, trades and mark-to-market are tracked in units of initial equity.
    This baseline has no stop orders and is NOT a Kraken daily-loss simulation.
    """
    if fast <= 0 or slow <= fast or len(df) < slow + 2:
        raise ValueError("Invalid EMA windows or insufficient candles")
    if not 0 <= fee_bps < 10000 or not 0 <= slippage_bps < 10000:
        raise ValueError("Costs must be between 0 and 10000 bps (exclusive)")
    f = df.close.ewm(span=fast, adjust=False, min_periods=slow).mean()
    s = df.close.ewm(span=slow, adjust=False, min_periods=slow).mean()
    signal = (f > s).shift(1, fill_value=False)
    cash, units, entry_cost = initial_equity, 0.0, 0.0
    fee, slip = fee_bps / 10000, slippage_bps / 10000
    equity, pnl, entries = [], [], 0
    for i, row in enumerate(df.itertuples()):
        if units and (not signal.iloc[i] or i == len(df) - 1):
            # At final bar liquidate at close; other exits execute at open.
            price = (row.close if i == len(df) - 1 else row.open) * (1 - slip)
            cash = units * price * (1 - fee)
            pnl.append(cash / entry_cost - 1)
            units = 0.0
        if signal.iloc[i] and not units and i < len(df) - 1:
            price = row.open * (1 + slip)
            entry_cost = cash
            units, cash = cash / (price * (1 + fee)), 0.0
            entries += 1
        equity.append(cash + units * row.close)
    curve = pd.Series(equity, index=df.index)
    returns = curve.pct_change().fillna(0)
    return {
        "total_return": float(curve.iloc[-1] / initial_equity - 1),
        "max_drawdown": float((curve / curve.cummax() - 1).min()),
        "closed_trades": len(pnl),
        "entries": entries,
        "win_rate": float(np.mean(np.array(pnl) > 0)) if pnl else None,
        "mean_trade_return": float(np.mean(pnl)) if pnl else None,
        "curve": curve,
        "returns": returns,
    }


def moving_block_bootstrap(returns, samples=500, block=12, seed=42):
    r = np.asarray(returns, dtype=float)
    if len(r) < block * 2:
        return None
    rng = np.random.default_rng(seed)
    totals = []
    for _ in range(samples):
        starts = rng.integers(0, len(r) - block + 1, size=int(np.ceil(len(r) / block)))
        sample = np.concatenate([r[i : i + block] for i in starts])[: len(r)]
        totals.append(float(np.prod(1 + sample) - 1))
    return {
        "p05": float(np.quantile(totals, 0.05)),
        "p50": float(np.median(totals)),
        "p95": float(np.quantile(totals, 0.95)),
        "samples": samples,
        "block_bars": block,
        "seed": seed,
        "warning": "Resampling uncertainty, not a calibrated profit probability",
    }


def walk_forward(df, train_bars=300, test_bars=100, fee_bps=40, slippage_bps=15):
    if train_bars < 102 or test_bars < 20 or len(df) < train_bars + test_bars:
        raise ValueError("Need train>=102, test>=20 and at least one full out-of-sample fold")
    if not df.index.is_unique or not df.index.is_monotonic_increasing:
        raise ValueError("Unordered or duplicate bars")
    candidates = [(10, 30), (20, 50), (20, 80), (50, 100)]
    folds, oos_returns = [], []
    for start in range(train_bars, len(df) - test_bars + 1, test_bars):
        train = df.iloc[start - train_bars : start]
        scores = [
            (simulate(train, f, s, fee_bps, slippage_bps)["total_return"], f, s)
            for f, s in candidates
        ]
        _, fast, slow = max(scores)
        # Warm indicators on training history, then trade the untouched test window.
        combined = df.iloc[start - train_bars : start + test_bars]
        full_f = combined.close.ewm(span=fast, adjust=False).mean()
        full_s = combined.close.ewm(span=slow, adjust=False).mean()
        test = df.iloc[start : start + test_bars]
        desired = (full_f > full_s).shift(1, fill_value=False).reindex(test.index)
        stats = _simulate_with_signal(test, desired, fee_bps, slippage_bps)
        oos_returns.extend(stats.pop("returns"))
        folds.append(
            {
                "train_start": train.index[0].isoformat(),
                "train_end": train.index[-1].isoformat(),
                "test_start": test.index[0].isoformat(),
                "test_end": test.index[-1].isoformat(),
                "fast": fast,
                "slow": slow,
                **stats,
            }
        )
    returns = np.array(oos_returns)
    wealth = np.cumprod(1 + returns)
    first_open = float(df.open.iloc[train_bars])
    last_index = train_bars + len(returns) - 1
    last_close = float(df.close.iloc[last_index])
    fee, slip = fee_bps / 10000, slippage_bps / 10000
    buy_hold = last_close * (1 - slip) * (1 - fee) / (first_open * (1 + slip) * (1 + fee)) - 1
    return {
        "strategy": "EMA long/flat research baseline",
        "folds": folds,
        "candidate_count": len(candidates),
        "oos_bars": len(returns),
        "oos_total_return": float(wealth[-1] - 1),
        "oos_max_drawdown": float(np.min(wealth / np.maximum.accumulate(np.r_[1, wealth])[1:] - 1)),
        "closed_trades": sum(f["closed_trades"] for f in folds),
        "benchmarks": {"cash_return": 0.0, "buy_hold_oos_return_after_costs": buy_hold},
        "bootstrap_total_return": moving_block_bootstrap(returns),
        "costs": {"fee_bps_per_side": fee_bps, "slippage_bps_per_side": slippage_bps},
        "limitations": [
            "No daily loss or stop simulation; never proves MDL compliance",
            "Sequential OOS windows; parameters selected on prior training only",
            "No funding, market impact, queue or intrabar path model",
            "Cash reset to flat at each fold; includes liquidation costs",
            "Four strategy trials; short samples and selection bias remain",
            "Run an untouched final holdout and paper trading before live use",
        ],
    }


def _simulate_with_signal(df, signal, fee_bps, slippage_bps):
    cash, units, entry_cash = 1.0, 0.0, 0.0
    fee, slip = fee_bps / 10000, slippage_bps / 10000
    curve, pnl = [], []
    for i, row in enumerate(df.itertuples()):
        if units and (not signal.iloc[i] or i == len(df) - 1):
            price = row.close if i == len(df) - 1 else row.open
            cash = units * price * (1 - slip) * (1 - fee)
            pnl.append(cash / entry_cash - 1)
            units = 0.0
        if signal.iloc[i] and not units and i < len(df) - 1:
            entry_cash = cash
            units, cash = cash / (row.open * (1 + slip) * (1 + fee)), 0.0
        curve.append(cash + units * row.close)
    curve = np.r_[1.0, curve]
    returns = curve[1:] / curve[:-1] - 1
    return {
        "total_return": float(curve[-1] - 1),
        "closed_trades": len(pnl),
        "returns": returns.tolist(),
    }
