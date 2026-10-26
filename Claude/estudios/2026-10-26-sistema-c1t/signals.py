"""Forebank C1T v1 — daily signal sheet from Kraken public daily candles (run after 00:00 UTC).

Usage (repo root):  python signals.py --equity 50000 [--positions positions.json]
positions.json: [{"asset": "btc", "qty": 0.01, "entry": 80000, "unit_risk": 9000, "stop": 71000}]
Prints: regime, entries for today's open (stop, quantity), stop updates and exits for open positions.
No orders are sent. Spot long-only. Signals use only closed daily candles.
"""
import argparse
import json
import urllib.request

from engine import C, C1T, Pos, Series, risk_trail

PAIRS = {"aave": "AAVEUSD", "ada": "ADAUSD", "algo": "ALGOUSD", "apt": "APTUSD", "arb": "ARBUSD",
         "aster": "ASTERUSD", "atom": "ATOMUSD", "avax": "AVAXUSD", "bch": "BCHUSD", "bnb": "BNBUSD",
         "bonk": "BONKUSD", "btc": "XBTUSD", "doge": "XDGUSD"}
RISK_PER_TRADE, MAX_OPEN_RISK, ASSET_CAP, GROSS_CAP = 0.0020, 0.005, 0.20, 0.50


def kraken_daily(pair):
    url = f"https://api.kraken.com/0/public/OHLC?pair={pair}&interval=1440"
    body = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "forebank-c1t"}), timeout=30))
    rows = next(v for k, v in body["result"].items() if k != "last")[:-1]  # drop the still-open candle
    from datetime import UTC, datetime
    return [{"timestamp": datetime.fromtimestamp(r[0], UTC).strftime("%Y-%m-%dT%H:%M:%SZ"), "open": float(r[1]),
             "high": float(r[2]), "low": float(r[3]), "close": float(r[4]), "volume": float(r[6])} for r in rows]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--equity", type=float, required=True)
    ap.add_argument("--positions", default=None)
    args = ap.parse_args()
    S = {a: Series(a, kraken_daily(p)) for a, p in PAIRS.items()}
    btc, strat = S["btc"], C1T()
    held = {p["asset"]: p for p in json.load(open(args.positions))} if args.positions else {}
    j = len(btc.d) - 1
    print(f"Last closed day {btc.d[j]} | BTC {btc.c[j]:.1f} vs SMA200 {btc.sma200[j]:.1f} -> regime {'ON' if btc.c[j] > btc.sma200[j] else 'OFF'}")
    open_risk = 0.0
    for a, h in held.items():
        s = S[a]
        i = len(s.d) - 1
        p = Pos(a, h["qty"], h["entry"], "", h["stop"], h["unit_risk"])
        exit_ = strat.after_close(s, i, p, btc, s.d[i])
        open_risk += max(0, h["qty"] * (s.c[i] - p.stop)) + h["qty"] * (s.c[i] + p.stop) * C
        print(f"HOLD {a}: close {s.c[i]:.6g} -> new stop {p.stop:.6g}" + ("  ** EXIT at open (close < 20d low) **" if exit_ else ""))
    cands = []
    for a, s in S.items():
        i = len(s.d) - 1
        if a in held or i < strat.warmup:
            continue
        if strat.entry(s, i, btc, s.d[i]):
            cands.append((s.ret90[i], a, i))
    if not cands:
        print("No entry signals today.")
    for _, a, i in sorted(cands, reverse=True):
        s = S[a]
        ref = s.c[i]
        stop = strat.init_stop(s, i, ref)
        unit = ref - stop + (ref + stop) * C
        qty = min(args.equity * RISK_PER_TRADE / unit, (args.equity * MAX_OPEN_RISK - open_risk) / unit,
                  args.equity * ASSET_CAP / ref)
        if qty <= 0:
            print(f"SIGNAL {a}: skipped, open-risk budget exhausted")
            continue
        open_risk += qty * unit
        print(f"BUY {a} ({PAIRS[a]}) at today's open ~{ref:.6g}: qty {qty:.6g} (~{qty * ref:,.0f} USD), "
              f"stop {stop:.6g} ({1 - stop / ref:.1%}), risk {qty * unit:,.0f} USD. Recompute stop from actual fill: "
              f"stop = fill - 3 x ATR20 ({s.atr20[i]:.6g}).")


if __name__ == "__main__":
    main()
