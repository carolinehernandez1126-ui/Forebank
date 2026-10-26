"""Technical + positioning snapshot from Kraken (price/liquidity) and Binance futures (funding/OI)."""
import json
import math
import statistics as st
import sys
import time
import urllib.request
from datetime import UTC, datetime

UA = {"User-Agent": "forebank-claude"}


def get(u, tries=3):
    for k in range(tries):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30))
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(1.5 * (k + 1))
    raise err


def ohlc(pair, interval):
    res = get(f"https://api.kraken.com/0/public/OHLC?pair={pair}&interval={interval}")["result"]
    rows = next(v for k, v in res.items() if k != "last")[:-1]
    return [dict(t=r[0], o=float(r[1]), h=float(r[2]), l=float(r[3]), c=float(r[4]), v=float(r[6])) for r in rows]


def sma(x, n):
    return sum(x[-n:]) / n if len(x) >= n else math.nan


def ema(x, n):
    if len(x) < n:
        return math.nan
    k = 2 / (n + 1)
    e = sum(x[:n]) / n
    for v in x[n:]:
        e = v * k + e * (1 - k)
    return e


def rsi(c, n=14):
    if len(c) <= n:
        return math.nan
    g = sum(max(c[i] - c[i - 1], 0) for i in range(1, n + 1)) / n
    lo = sum(max(c[i - 1] - c[i], 0) for i in range(1, n + 1)) / n
    for i in range(n + 1, len(c)):
        d = c[i] - c[i - 1]
        g = (g * (n - 1) + max(d, 0)) / n
        lo = (lo * (n - 1) + max(-d, 0)) / n
    return 100 if lo == 0 else 100 - 100 / (1 + g / lo)


def atr(b, n=14):
    tr = [max(b[i]["h"] - b[i]["l"], abs(b[i]["h"] - b[i - 1]["c"]), abs(b[i]["l"] - b[i - 1]["c"])) for i in range(1, len(b))]
    a = sum(tr[:n]) / n
    for t in tr[n:]:
        a = (a * (n - 1) + t) / n
    return a


def swing_lows(b, k=3, lookback=120):
    seg = b[-lookback:]
    return [seg[i]["l"] for i in range(k, len(seg) - k) if seg[i]["l"] == min(x["l"] for x in seg[i - k : i + k + 1])]


def swing_highs(b, k=3, lookback=120):
    seg = b[-lookback:]
    return [seg[i]["h"] for i in range(k, len(seg) - k) if seg[i]["h"] == max(x["h"] for x in seg[i - k : i + k + 1])]


def snapshot(sym, pair, btc_d):
    d = ohlc(pair, 1440)
    h4 = ohlc(pair, 240)
    c = [x["c"] for x in d]
    c4 = [x["c"] for x in h4]
    px = c[-1]
    book = next(iter(get(f"https://api.kraken.com/0/public/Depth?pair={pair}&count=200")["result"].values()))
    ask, bid = float(book["asks"][0][0]), float(book["bids"][0][0])
    depth10 = sum(float(p) * float(v) for p, v, *_ in book["asks"] if float(p) <= ask * 1.001)
    vol30 = st.median(x["c"] * x["v"] for x in d[-30:])
    a = atr(d)
    lows = [v for v in swing_lows(d) if v < px]
    highs = [v for v in swing_highs(d) if v > px]
    bc = {x["t"]: x["c"] for x in btc_d}
    common = [x for x in d if x["t"] in bc]
    rs30 = (common[-1]["c"] / common[-31]["c"]) / (bc[common[-1]["t"]] / bc[common[-31]["t"]]) - 1 if len(common) > 31 else math.nan
    out = {
        "sym": sym, "pair": pair, "bars": len(d), "price": px,
        "spread_bps": (ask - bid) / ((ask + bid) / 2) * 1e4, "depth10": depth10, "vol30_usd": vol30,
        "r7": px / c[-8] - 1, "r30": px / c[-31] - 1 if len(c) > 31 else math.nan,
        "r90": px / c[-91] - 1 if len(c) > 91 else math.nan,
        "vs_sma20": px / sma(c, 20) - 1, "vs_sma50": px / sma(c, 50) - 1, "vs_sma200": px / sma(c, 200) - 1 if len(c) >= 200 else math.nan,
        "rsi_d": rsi(c), "rsi_4h": rsi(c4), "ema20_4h_vs_50": ema(c4, 20) / ema(c4, 50) - 1,
        "atr_pct": a / px, "hi_2y": max(x["h"] for x in d), "dd_from_hi": px / max(x["h"] for x in d) - 1,
        "low_60d": min(x["l"] for x in d[-60:]), "high_60d": max(x["h"] for x in d[-60:]),
        "support": max(lows) if lows else min(x["l"] for x in d[-120:]),
        "support2": sorted(lows)[-2] if len(lows) > 1 else math.nan,
        "resistance": min(highs) if highs else math.nan,
        "vol_7_vs_30": st.mean(x["v"] for x in d[-7:]) / st.mean(x["v"] for x in d[-30:]),
        "rs_btc_30": rs30,
    }
    try:
        fp = get(f"https://fapi.binance.com/fapi/v1/premiumIndex?symbol={sym}USDT")
        oi = get(f"https://fapi.binance.com/futures/data/openInterestHist?symbol={sym}USDT&period=1d&limit=8")
        fh = get(f"https://fapi.binance.com/fapi/v1/fundingRate?symbol={sym}USDT&limit=21")
        out["funding_now_8h"] = float(fp["lastFundingRate"])
        out["funding_7d_avg_8h"] = st.mean(float(x["fundingRate"]) for x in fh)
        out["oi_7d_chg"] = float(oi[-1]["sumOpenInterestValue"]) / float(oi[0]["sumOpenInterestValue"]) - 1
        out["oi_usd"] = float(oi[-1]["sumOpenInterestValue"])
    except Exception:  # noqa: BLE001
        out["funding_now_8h"] = None
    return out


if __name__ == "__main__":
    pairs = json.loads(sys.argv[1])
    btc_d = ohlc("XBTUSD", 1440)
    res = {}
    for sym, pair in pairs.items():
        try:
            res[sym] = snapshot(sym, pair, btc_d)
        except Exception as e:  # noqa: BLE001
            res[sym] = {"sym": sym, "error": str(e)}
        time.sleep(0.5)
    json.dump({"as_of": datetime.now(UTC).isoformat(), "data": res}, open(sys.argv[2], "w"), indent=1)
    print("written", sys.argv[2])
