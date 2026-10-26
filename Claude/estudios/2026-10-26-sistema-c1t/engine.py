"""Claude's daily portfolio simulator for Forebank (spot long-only).

Causal: signals at close of day t, orders at open of t+1. Stops: gap below -> open, else stop price.
Costs: FEE + SLIP per side. Equity is marked to market daily; intraday worst uses each position's low.
Trades are reported in R = net pnl / (qty * initial unit risk incl. round-trip costs).
"""
from __future__ import annotations

import json
import math
import random
import statistics as st
from dataclasses import dataclass, field
from datetime import date

FEE, SLIP = 0.0040, 0.0015
C = FEE + SLIP


def load_long(sym):
    return json.load(open(f"private/claude/long/{sym}.json"))["candles"]


def load_kraken(sym):
    return json.load(open(f"private/claude/data/{sym}.json"))["candles"]["1440"]


def wilder_atr(h, l, c, n):
    out = [math.nan] * len(c)
    if len(c) <= n:
        return out
    tr = [h[0] - l[0]] + [max(h[i] - l[i], abs(h[i] - c[i - 1]), abs(l[i] - c[i - 1])) for i in range(1, len(c))]
    a = sum(tr[1 : n + 1]) / n
    out[n] = a
    for i in range(n + 1, len(c)):
        a = (a * (n - 1) + tr[i]) / n
        out[i] = a
    return out


def rolling(f, x, n, lag=0):
    """f over x[i-n-lag+1 .. i-lag]; lag=1 means prior n bars excluding today."""
    out = [math.nan] * len(x)
    for i in range(n + lag - 1, len(x)):
        out[i] = f(x[i - n - lag + 1 : i - lag + 1])
    return out


def rsi(c, n):
    out = [math.nan] * len(c)
    if len(c) <= n:
        return out
    g = sum(max(c[i] - c[i - 1], 0) for i in range(1, n + 1)) / n
    lo = sum(max(c[i - 1] - c[i], 0) for i in range(1, n + 1)) / n
    out[n] = 100 if lo == 0 else 100 - 100 / (1 + g / lo)
    for i in range(n + 1, len(c)):
        d = c[i] - c[i - 1]
        g = (g * (n - 1) + max(d, 0)) / n
        lo = (lo * (n - 1) + max(-d, 0)) / n
        out[i] = 100 if lo == 0 else 100 - 100 / (1 + g / lo)
    return out


class Series:
    def __init__(self, name, candles):
        self.name = name
        self.d = [x["timestamp"][:10] for x in candles]
        self.idx = {d: i for i, d in enumerate(self.d)}
        self.o = [x["open"] for x in candles]
        self.h = [x["high"] for x in candles]
        self.l = [x["low"] for x in candles]
        self.c = [x["close"] for x in candles]
        self.qv = [x.get("quote_volume", x["close"] * x["volume"]) for x in candles]
        self.atr14 = wilder_atr(self.h, self.l, self.c, 14)
        self.atr20 = wilder_atr(self.h, self.l, self.c, 20)
        mean = lambda v: sum(v) / len(v)
        self.sma100 = rolling(mean, self.c, 100)
        self.sma200 = rolling(mean, self.c, 200)
        self.hh20 = rolling(max, self.h, 20, 1)
        self.hh50 = rolling(max, self.h, 50, 1)
        self.ll10 = rolling(min, self.l, 10, 1)
        self.ll20 = rolling(min, self.l, 20, 1)
        self.rsi3 = rsi(self.c, 3)
        self.ret90 = [self.c[i] / self.c[i - 90] - 1 if i >= 90 else math.nan for i in range(len(self.c))]


@dataclass
class Pos:
    asset: str
    qty: float
    entry: float
    entry_date: str
    stop: float
    unit_risk: float
    target: float | None = None
    bars: int = 0
    exit_next_open: bool = False
    max_close: float = 0.0


@dataclass
class Result:
    trades: list = field(default_factory=list)
    equity: list = field(default_factory=list)  # (date, close_equity, intraday_worst, day_start)


# ---------------- strategies ----------------
class Strategy:
    name = "base"
    warmup = 210

    def entry(self, s: Series, i: int, btc: Series, day: str) -> bool:
        raise NotImplementedError

    def init_stop(self, s, i, e):
        raise NotImplementedError

    def target(self, s, i, e, unit_risk):
        return None

    def after_close(self, s, i, p: Pos, btc, day):
        """Return True to exit at next open. May tighten p.stop."""
        return False


def btc_above(btc, day, field_name):
    j = btc.idx.get(day)
    if j is None:
        return False
    v = getattr(btc, field_name)[j]
    return not math.isnan(v) and btc.c[j] > v


class H1(Strategy):
    name = "H1"

    def entry(self, s, i, btc, day):
        return s.c[i] > s.hh20[i] and btc_above(btc, day, "sma100")

    def init_stop(self, s, i, e):
        return e - 2.5 * s.atr14[i]

    def after_close(self, s, i, p, btc, day):
        return s.c[i] < s.ll10[i]


class H2(Strategy):
    name = "H2"

    def entry(self, s, i, btc, day):
        return s.c[i] > s.sma100[i] and s.rsi3[i] < 20

    def init_stop(self, s, i, e):
        return e - 2.0 * s.atr14[i]

    def target(self, s, i, e, unit_risk):
        return e + 2.5 * unit_risk + 2 * C * e

    def after_close(self, s, i, p, btc, day):
        return p.bars >= 10


class C1(Strategy):
    name = "C1"

    def entry(self, s, i, btc, day):
        return s.c[i] > s.hh50[i] and btc_above(btc, day, "sma200")

    def init_stop(self, s, i, e):
        return e - 3.0 * s.atr20[i]

    def after_close(self, s, i, p, btc, day):
        return s.c[i] < s.ll20[i]


class C2(Strategy):
    name = "C2"

    def _ok(self, s, i, btc, day):
        return s.ret90[i] > 0 and s.c[i] > s.sma100[i] and btc_above(btc, day, "sma200")

    def entry(self, s, i, btc, day):
        return date.fromisoformat(day).weekday() == 6 and self._ok(s, i, btc, day)

    def init_stop(self, s, i, e):
        return e - 3.0 * s.atr20[i]

    def after_close(self, s, i, p, btc, day):
        p.max_close = max(p.max_close, s.c[i])
        p.stop = max(p.stop, p.max_close - 3.0 * s.atr20[i])
        if date.fromisoformat(day).weekday() == 6 and not self._ok(s, i, btc, day):
            return True
        return False


STRATS = {"H1": H1, "H2": H2, "C1": C1, "C2": C2}


# ---------------- simulator ----------------
def simulate(strat: Strategy, series: dict[str, Series], btc: Series, start: str, end: str,
             equity0=50_000.0, risk_frac=0.0025, max_open_risk=0.005, asset_cap=0.20, gross_cap=0.50,
             unconstrained=False):
    days = sorted({d for s in series.values() for d in s.d if start <= d <= end})
    cash = equity0
    pos: dict[str, Pos] = {}
    pending: list[tuple[str, int]] = []
    res = Result()
    last_close = {}

    def mtm():
        return cash + sum(p.qty * last_close.get(a, p.entry) for a, p in pos.items())

    def close_pos(a, px, day, reason):
        nonlocal cash
        p = pos.pop(a)
        cash += p.qty * px * (1 - FEE)
        pnl = p.qty * (px * (1 - FEE) - p.entry * (1 + FEE))
        res.trades.append({"asset": a, "entry": p.entry_date, "exit": day, "r": pnl / (p.qty * p.unit_risk),
                           "pnl": pnl, "reason": reason, "bars": p.bars})

    for day in days:
        day_start = mtm()
        # 1) scheduled exits at open
        for a in list(pos):
            s = series[a]
            i = s.idx.get(day)
            if i is not None and pos[a].exit_next_open:
                close_pos(a, s.o[i] * (1 - SLIP), day, "signal_exit")
        # 2) entries at open
        eq = mtm()
        open_risk = sum(max(0.0, p.qty * (last_close.get(a, p.entry) - p.stop)) + p.qty * (last_close.get(a, p.entry) + p.stop) * C
                        for a, p in pos.items())
        gross = sum(p.qty * last_close.get(a, p.entry) for a, p in pos.items())
        for a, isig in pending:
            s = series[a]
            i = s.idx.get(day)
            if i is None or a in pos or i != isig + 1:
                continue
            e = s.o[i] * (1 + SLIP)
            stop = strat.init_stop(s, isig, s.o[i])
            if not (stop < e) or stop <= 0:
                continue
            unit = e - stop + (e + stop) * C
            if unconstrained:
                qty = 1000.0 / unit
            else:
                qty = min(eq * risk_frac / unit, (eq * max_open_risk - open_risk) / unit,
                          eq * asset_cap / e, (eq * gross_cap - gross) / e, cash / (e * (1 + FEE)))
                if qty * e < 25:  # ignore dust
                    continue
            cash -= qty * e * (1 + FEE)
            p = Pos(a, qty, e, day, stop, unit, strat.target(s, isig, e, unit), max_close=e)
            pos[a] = p
            open_risk += qty * unit
            gross += qty * e
        pending = []
        # 3) intraday stops / targets
        worst = cash
        for a in list(pos):
            s = series[a]
            i = s.idx.get(day)
            p = pos[a]
            if i is None:
                worst += p.qty * last_close.get(a, p.entry)
                continue
            if s.o[i] <= p.stop and p.entry_date != day:
                worst += p.qty * s.o[i] * (1 - SLIP) * (1 - FEE)
                close_pos(a, s.o[i] * (1 - SLIP), day, "gap_stop")
            elif s.l[i] <= p.stop:
                worst += p.qty * p.stop * (1 - SLIP) * (1 - FEE)
                close_pos(a, p.stop * (1 - SLIP), day, "stop")
            elif p.target and s.h[i] >= p.target:
                worst += p.qty * min(s.l[i], p.target)
                close_pos(a, p.target, day, "target")
            else:
                worst += p.qty * s.l[i]
        # 4) close: mark, exit rules, new signals
        for a, s in series.items():
            i = s.idx.get(day)
            if i is not None:
                last_close[a] = s.c[i]
        for a in list(pos):
            s = series[a]
            i = s.idx.get(day)
            if i is None:
                continue
            p = pos[a]
            p.bars += 1
            if strat.after_close(s, i, p, btc, day):
                p.exit_next_open = True
        cands = []
        for a, s in series.items():
            i = s.idx.get(day)
            if i is None or a in pos or i < strat.warmup or i + 1 >= len(s.d):
                continue
            if any(math.isnan(v) for v in (s.atr14[i], s.atr20[i], s.sma100[i], s.hh50[i])):
                continue
            if strat.entry(s, i, btc, day):
                cands.append((s.ret90[i] if not math.isnan(s.ret90[i]) else -9, a, i))
        pending = [(a, i) for _, a, i in sorted(cands, reverse=True)]
        res.equity.append((day, mtm(), worst + 0.0, day_start))
    for a in list(pos):  # mark open trades at end
        close_pos(a, last_close[a], days[-1], "open_at_end")
    return res


# ---------------- stats ----------------
def trade_stats(trades):
    if not trades:
        return {"n": 0}
    rs = [t["r"] for t in trades]
    srt = sorted(trades, key=lambda t: t["entry"])
    mid = len(srt) // 2
    eq = pk = mdd = 0.0
    for t in sorted(trades, key=lambda t: t["exit"]):
        eq += t["r"]
        pk = max(pk, eq)
        mdd = min(mdd, eq - pk)
    neg = -sum(r for r in rs if r < 0)
    return {"n": len(rs), "exp": st.mean(rs), "med": st.median(rs), "win": sum(r > 0 for r in rs) / len(rs),
            "pf": (sum(r for r in rs if r > 0) / neg) if neg else math.inf,
            "exp_wo_best": (sum(rs) - max(rs)) / (len(rs) - 1) if len(rs) > 1 else math.nan,
            "h1": st.mean(t["r"] for t in srt[:mid]) if mid else math.nan,
            "h2": st.mean(t["r"] for t in srt[mid:]), "mddR": mdd, "sumR": sum(rs)}


def passes(s):
    return (s["n"] >= 20 and s["exp"] > 0 and s["exp_wo_best"] > 0 and s["h1"] > 0 and s["h2"] > 0
            and s["mddR"] > -8)


def equity_stats(eqs):
    e = [x[1] for x in eqs]
    pk = e[0]
    mdd = 0.0
    worst_day = 0.0
    for d, close, worst, start in eqs:
        pk = max(pk, close)
        mdd = min(mdd, close / pk - 1, worst / pk - 1)
        worst_day = min(worst_day, worst / start - 1, close / start - 1)
    yrs = len(e) / 365
    cagr = (e[-1] / e[0]) ** (1 / yrs) - 1 if yrs > 0 else math.nan
    rets = [e[i] / e[i - 1] - 1 for i in range(1, len(e))]
    sharpe = st.mean(rets) / st.stdev(rets) * math.sqrt(365) if len(rets) > 2 and st.stdev(rets) > 0 else math.nan
    return {"final": e[-1], "cagr": cagr, "mdd": mdd, "worst_day": worst_day, "sharpe": sharpe, "days": len(e)}


def block_bootstrap_mdd(eqs, n_sims=2000, block=20, horizon=None, seed=7):
    e = [x[1] for x in eqs]
    rets = [e[i] / e[i - 1] - 1 for i in range(1, len(e))]
    horizon = horizon or len(rets)
    rng = random.Random(seed)
    out = []
    for _ in range(n_sims):
        path = []
        while len(path) < horizon:
            j = rng.randrange(0, len(rets) - block)
            path += rets[j : j + block]
        v = pk = 1.0
        mdd = 0.0
        for r in path[:horizon]:
            v *= 1 + r
            pk = max(pk, v)
            mdd = min(mdd, v / pk - 1)
        out.append(mdd)
    out.sort()
    return {"p50": out[len(out) // 2], "p95": out[int(0.05 * len(out))], "p99": out[int(0.01 * len(out))]}


def risk_trail(s, i, p: Pos):
    """Raise stop so that loss from today's close to stop (incl. costs) never exceeds the initial 1R."""
    c = s.c[i]
    level = (c * (1 + C) - p.unit_risk) / (1 - C)
    p.stop = max(p.stop, level)


class C1T(C1):
    name = "C1T"

    def after_close(self, s, i, p, btc, day):
        risk_trail(s, i, p)
        return super().after_close(s, i, p, btc, day)


class H1T(H1):
    name = "H1T"

    def after_close(self, s, i, p, btc, day):
        risk_trail(s, i, p)
        return super().after_close(s, i, p, btc, day)


STRATS.update({"C1T": C1T, "H1T": H1T})
