from __future__ import annotations

import numpy as np
import pandas as pd

from .io import digest, utcnow


def frame(candles):
    result = pd.DataFrame([c.model_dump() for c in candles])
    result["timestamp"] = pd.to_datetime(result.timestamp, utc=True)
    return result.set_index("timestamp")


def indicators(df):
    out = df.copy()
    c, h, low, v = out.close, out.high, out.low, out.volume
    for period in (20, 50, 200):
        out[f"sma_{period}"] = c.rolling(period).mean()
        out[f"ema_{period}"] = c.ewm(span=period, adjust=False, min_periods=period).mean()
    delta = c.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / 14, adjust=False, min_periods=14).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / 14, adjust=False, min_periods=14).mean()
    out["rsi_14"] = 100 - 100 / (1 + gain / loss.replace(0, np.nan))
    out.loc[(loss == 0) & (gain > 0), "rsi_14"] = 100
    out.loc[(loss == 0) & (gain == 0), "rsi_14"] = 50
    out["macd"] = c.ewm(span=12, adjust=False).mean() - c.ewm(span=26, adjust=False).mean()
    out["macd_signal"] = out.macd.ewm(span=9, adjust=False).mean()
    out["macd_histogram"] = out.macd - out.macd_signal
    prev = c.shift()
    tr = pd.concat([h - low, (h - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)
    out["atr_14"] = tr.ewm(alpha=1 / 14, adjust=False, min_periods=14).mean()
    plus = h.diff()
    minus = -low.diff()
    plus_dm = plus.where((plus > minus) & (plus > 0), 0)
    minus_dm = minus.where((minus > plus) & (minus > 0), 0)
    plus_di = 100 * plus_dm.ewm(alpha=1 / 14, adjust=False).mean() / out.atr_14
    minus_di = 100 * minus_dm.ewm(alpha=1 / 14, adjust=False).mean() / out.atr_14
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    out["adx_14"] = dx.ewm(alpha=1 / 14, adjust=False, min_periods=14).mean()
    std = c.rolling(20).std(ddof=0)
    out["bollinger_upper"] = out.sma_20 + 2 * std
    out["bollinger_lower"] = out.sma_20 - 2 * std
    out["donchian_high_20"] = h.rolling(20).max()
    out["donchian_low_20"] = low.rolling(20).min()
    out["obv"] = (np.sign(c.diff()).fillna(0) * v).cumsum()
    typical = (h + low + c) / 3
    out["vwap_rolling_20"] = (typical * v).rolling(20).sum() / v.rolling(20).sum().replace(
        0, np.nan
    )
    # UTC daily session VWAP; 1d bars provide no intraday VWAP information.
    groups = out.index.floor("D")
    out["vwap_session_utc"] = (typical * v).groupby(groups).cumsum() / v.groupby(
        groups
    ).cumsum().replace(0, np.nan)
    out["volume_zscore_20"] = (v - v.rolling(20).mean()) / v.rolling(20).std().replace(0, np.nan)
    return out


def finite(value):
    return float(value) if pd.notna(value) and np.isfinite(value) else None


def quality(candles, interval, now=None, min_bars=250):
    now = now or utcnow()
    df = frame(candles)
    diffs = df.index.to_series().diff().dropna().dt.total_seconds()
    expected = interval * 60
    reasons = []
    if len(df) < min_bars:
        reasons.append(f"insufficient_bars:{len(df)}<{min_bars}")
    if not df.index.is_unique or not df.index.is_monotonic_increasing:
        reasons.append("unordered_or_duplicate_timestamps")
    if any(diffs != expected):
        reasons.append("gaps_or_irregular_intervals")
    age = now.timestamp() - (df.index[-1].timestamp() + expected)
    if age < 0:
        reasons.append("unclosed_or_future_candle")
    if age > expected * 1.5:
        reasons.append("stale_candles")
    return {
        "passed": not reasons,
        "reasons": reasons,
        "bars": len(df),
        "last_close_age_seconds": age,
        "first_open": df.index[0].isoformat(),
        "last_open": df.index[-1].isoformat(),
    }


def statistics(df, interval):
    returns = df.close.pct_change().dropna()
    periods = 365.25 * 24 * 60 / interval
    q05 = returns.quantile(0.05)
    wealth = df.close / df.close.iloc[0]
    return {
        "observations": len(returns),
        "annualized_volatility": finite(returns.std() * np.sqrt(periods)),
        "historical_var_95_per_bar": finite(max(0, -q05)),
        "historical_cvar_95_per_bar": finite(max(0, -returns[returns <= q05].mean())),
        "max_drawdown": finite((wealth / wealth.cummax() - 1).min()),
        "return_skew": finite(returns.skew()),
        "excess_kurtosis": finite(returns.kurt()),
        "return_autocorrelation_lag1": finite(returns.autocorr(1)),
        "return_zscore_50": finite(
            (returns.iloc[-1] - returns.tail(50).mean()) / returns.tail(50).std()
        ),
    }


def dossier(dataset, now=None, min_bars=250):
    now = now or utcnow()
    result = {
        "schema_version": "1",
        "dataset_sha256": digest(dataset),
        "as_of": now.isoformat(),
        "symbol": dataset.instrument.symbol,
        "synthetic": dataset.synthetic,
        "status": "RESEARCH_ONLY",
        "timeframes": {},
        "fundamentals": dataset.fundamentals,
        "provenance": dataset.provenance,
        "warnings": list(dataset.warnings),
    }
    for interval, candles in dataset.candles.items():
        df = frame(candles)
        enriched = indicators(df)
        latest = {k: finite(v) for k, v in enriched.iloc[-1].items()}
        trend = (
            "up"
            if latest["ema_50"] and latest["ema_200"] and latest["ema_50"] > latest["ema_200"]
            else "down_or_unknown"
        )
        result["timeframes"][interval] = {
            "quality": quality(candles, interval, now, min_bars),
            "latest": latest,
            "trend": trend,
            "statistics": statistics(df, interval),
        }
    if not dataset.fundamentals:
        result["warnings"].append(
            "No fundamental sources collected; manual primary-source research required"
        )
    result["warnings"].append(
        "Indicators are correlated features, not independent votes or profit forecasts"
    )
    return result


def portfolio_correlations(datasets, interval=60):
    series = {}
    for data in datasets:
        if interval not in data.candles:
            raise ValueError(f"Missing {interval}m for {data.instrument.symbol}")
        series[data.instrument.symbol] = frame(data.candles[interval]).close.pct_change()
    aligned = pd.concat(series, axis=1).dropna()
    if len(aligned) < 30:
        raise ValueError("At least 30 common returns required")
    return {
        "interval_minutes": interval,
        "common_observations": len(aligned),
        "correlation": aligned.corr().to_dict(),
        "warning": "Descriptive only. Risk engine assumes simultaneous losses; no diversification credit.",
    }


def markdown_report(report):
    lines = [
        f"# Research: {report['symbol']}",
        "",
        f"Status: **{report['status']}**",
        f"Dataset SHA256: `{report['dataset_sha256']}`",
        f"As of: {report['as_of']}",
        "",
        "Synthetic data: " + str(report["synthetic"]),
        "",
    ]
    for interval, item in report["timeframes"].items():
        lines += [
            f"## {interval} minutes",
            "",
            f"Quality: {item['quality']}",
            "",
            "| Metric | Value |",
            "|---|---:|",
        ]
        for key, value in {**item["latest"], **item["statistics"]}.items():
            lines.append(f"| {key} | {value} |")
        lines.append("")
    lines += ["## Missing data and limitations", ""] + [f"- {w}" for w in report["warnings"]]
    lines += [
        "",
        "Full fundamental payloads and provenance: companion JSON dossier.",
        "No trade recommendation is generated by this report.",
        "",
    ]
    return "\n".join(lines)
