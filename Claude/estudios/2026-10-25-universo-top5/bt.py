"""Claude's rule backtests on Kraken daily candles. Signals at close t, fills at open t+1.

Stops: gap below stop fills at open; otherwise at stop. Market exits pay slippage; all pay fee.
Results in R = net pnl per unit / initial risk per unit (incl. round-trip costs).
Reproduce: `lab collect --enrich` each asset (and BTC/USD) into private/claude/data/<asset>.json, then run from repo root.
"""
import json
import math
import statistics as st
import sys

FEE, SLIP = 0.0040, 0.0015
C = FEE + SLIP
ASSETS = ["aave", "ada", "aixbt", "algo", "apt"]
ELIGIBLE = ["aave", "ada", "algo", "apt"]


def load(a, interval=1440):
    return json.load(open(f"private/claude/data/{a}.json"))["candles"][str(interval)]


def sma(x, n, i):
    return sum(x[i - n + 1 : i + 1]) / n if i >= n - 1 else None


def atr_series(b, n=14):
    tr = [b[0]["high"] - b[0]["low"]]
    for i in range(1, len(b)):
        pc = b[i - 1]["close"]
        tr.append(max(b[i]["high"] - b[i]["low"], abs(b[i]["high"] - pc), abs(b[i]["low"] - pc)))
    out = [None] * len(b)
    a = sum(tr[1 : n + 1]) / n
    out[n] = a
    for i in range(n + 1, len(b)):
        a = (a * (n - 1) + tr[i]) / n
        out[i] = a
    return out


def rsi_series(c, n):
    out = [None] * len(c)
    g = l = 0.0
    for i in range(1, n + 1):
        d = c[i] - c[i - 1]
        g += max(d, 0)
        l += max(-d, 0)
    g /= n
    l /= n
    out[n] = 100 if l == 0 else 100 - 100 / (1 + g / l)
    for i in range(n + 1, len(c)):
        d = c[i] - c[i - 1]
        g = (g * (n - 1) + max(d, 0)) / n
        l = (l * (n - 1) + max(-d, 0)) / n
        out[i] = 100 if l == 0 else 100 - 100 / (1 + g / l)
    return out


def btc_regime(n=100):
    b = load("btc")
    c = [x["close"] for x in b]
    return {x["timestamp"]: (sma(c, n, i) is not None and c[i] > sma(c, n, i)) for i, x in enumerate(b)}


def trade_r(entry_open, stop, exit_px_gross, market_exit=True):
    e = entry_open * (1 + SLIP)
    x = exit_px_gross * (1 - SLIP) if market_exit else exit_px_gross
    risk = e - stop + (e + stop) * C
    pnl = x * (1 - FEE) - e * (1 + FEE)
    return pnl / risk, e, risk


def run(asset, rule, params, regime=None):
    b = load(asset)
    c = [x["close"] for x in b]
    atr = atr_series(b)
    rsi3 = rsi_series(c, 3)
    trades = []
    i = 210
    while i < len(b) - 1:
        sig = False
        if rule == "H1":
            hh = max(x["high"] for x in b[i - params["entry_n"] : i])
            ok_reg = regime is None or regime.get(b[i]["timestamp"], False)
            sig = c[i] > hh and ok_reg
        elif rule == "H2":
            s = sma(c, params["trend_n"], i)
            sig = s is not None and c[i] > s and rsi3[i] < params["rsi_th"]
        if not sig:
            i += 1
            continue
        j = i + 1
        eo = b[j]["open"]
        stop = eo - params["atr_k"] * atr[i]
        e_eff = eo * (1 + SLIP)
        risk_unit = e_eff - stop + (e_eff + stop) * C
        target = e_eff + params.get("rr", 0) * risk_unit + (e_eff) * 2 * C if rule == "H2" else None
        exit_px = None
        market = True
        k = j
        while k < len(b):
            bar = b[k]
            if bar["open"] <= stop and k > j:
                exit_px, reason = bar["open"], "gap_stop"
                break
            if bar["low"] <= stop:
                exit_px, reason = stop, "stop"
                break
            if target and bar["high"] >= target:
                exit_px, reason, market = target, "target", False
                break
            if rule == "H1":
                ll = min(x["low"] for x in b[k - params["exit_n"] : k])
                if bar["close"] < ll and k + 1 < len(b):
                    exit_px, reason = b[k + 1]["open"], "trail"
                    k += 1
                    break
            if rule == "H2" and k - j + 1 >= params["max_days"] and k + 1 < len(b):
                exit_px, reason = b[k + 1]["open"], "time"
                k += 1
                break
            k += 1
        if exit_px is None:
            exit_px, reason, k = b[-1]["close"], "open_at_end", len(b) - 1
        r, _, _ = trade_r(eo, stop, exit_px, market)
        trades.append({"asset": asset, "entry": b[j]["timestamp"][:10], "exit": b[k]["timestamp"][:10],
                       "days": k - j + 1, "r": r, "reason": reason, "stop_pct": 1 - stop / eo})
        i = k + 1
    return trades


def stats(tr, label):
    if not tr:
        print(f"{label}: 0 trades")
        return
    rs = [t["r"] for t in tr]
    tr_sorted = sorted(tr, key=lambda t: t["exit"])
    eq = peak = mdd = 0.0
    for t in tr_sorted:
        eq += t["r"]
        peak = max(peak, eq)
        mdd = min(mdd, eq - peak)
    best = max(rs)
    wo = (sum(rs) - best) / (len(rs) - 1) if len(rs) > 1 else float("nan")
    half = sorted(tr, key=lambda t: t["entry"])
    mid = len(half) // 2
    h1 = st.mean([t["r"] for t in half[:mid]]) if mid else float("nan")
    h2 = st.mean([t["r"] for t in half[mid:]])
    wins = [r for r in rs if r > 0]
    pf = sum(wins) / -sum(r for r in rs if r < 0) if any(r < 0 for r in rs) else math.inf
    print(f"{label}: n={len(rs)} expR={st.mean(rs):+.3f} medR={st.median(rs):+.2f} win={len(wins)/len(rs):.0%} "
          f"PF={pf:.2f} sumR={sum(rs):+.1f} mddR={mdd:.1f} exp_wo_best={wo:+.3f} halves={h1:+.3f}/{h2:+.3f} "
          f"avg_days={st.mean(t['days'] for t in tr):.1f} avg_stop={st.mean(t['stop_pct'] for t in tr):.1%}")


if __name__ == "__main__":
    reg = btc_regime()
    H1 = {"entry_n": 20, "exit_n": 10, "atr_k": 2.5}
    H2 = {"trend_n": 100, "rsi_th": 20, "atr_k": 2.0, "rr": 2.5, "max_days": 10}
    out = {}
    for rule, p, rg in [("H1", H1, reg), ("H1_noregime", H1, None), ("H2", H2, None)]:
        allt = []
        for a in ASSETS:
            t = run(a, rule.split("_")[0], p, rg)
            out.setdefault(rule, []).extend(t)
            stats(t, f"  {rule} {a}")
            if a in ELIGIBLE:
                allt += t
        stats(allt, f"{rule} POOLED eligible")
        print()
    if "-v" in sys.argv:
        for t in sorted(out["H1"], key=lambda t: t["entry"]):
            print(t)
    json.dump(out, open("private/claude/out/bt_trades.json", "w"), indent=1)
