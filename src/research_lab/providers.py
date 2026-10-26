from __future__ import annotations

import os
import ssl
import time
from datetime import UTC, datetime
from urllib.parse import quote, urlparse

import httpx

from .io import digest, utcnow
from .models import Candle, Dataset, Instrument, Quote

ALLOWED_HOSTS = {"api.kraken.com", "api.coingecko.com", "api.llama.fi", "api.stlouisfed.org"}
INTERVALS = {1, 5, 15, 30, 60, 240, 1440, 10080, 21600}


class SourceError(RuntimeError):
    pass


class PublicClient:
    """GET-only allowlisted sources; keys never enter persisted request metadata."""

    def __init__(self, store, transport=None):
        self.store = store
        # Use the platform trust store (including locally managed CAs), never verify=False.
        self.client = httpx.Client(
            timeout=25,
            follow_redirects=False,
            transport=transport,
            verify=ssl.create_default_context(),
        )
        self.last_call = {}

    def close(self):
        self.client.close()

    def get(self, url, params=None, *, headers=None, ttl=60):
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS or parsed.query:
            raise SourceError("URL outside provider allowlist")
        if parsed.hostname == "api.kraken.com" and not parsed.path.startswith("/0/public/"):
            raise SourceError("Only public Kraken endpoints are supported")
        params = params or {}
        public_params = {k: v for k, v in params.items() if "key" not in k.lower()}
        request_key = digest({"url": url, "params": public_params})
        cached = self.store.cached(request_key, ttl)
        if cached:
            return cached
        for attempt in range(3):
            host = parsed.hostname
            spacing = 3.1 if host == "api.coingecko.com" else 1.1
            time.sleep(max(0, spacing - (time.monotonic() - self.last_call.get(host, 0))))
            self.last_call[host] = time.monotonic()
            try:
                response = self.client.get(url, params=params, headers=headers)
                if response.status_code == 429 or response.status_code >= 500:
                    retry = response.headers.get("Retry-After", "")
                    delay = float(retry) if retry.isdigit() else 2 ** (attempt + 1)
                    if attempt < 2:
                        time.sleep(min(delay, 30))
                        continue
                if response.status_code != 200:
                    raise SourceError(f"{host}: HTTP {response.status_code}")
                body = response.json()
                if isinstance(body, dict) and body.get("error"):
                    raise SourceError(f"{host}: provider returned an error")
                envelope = {
                    "url": url,
                    "params": public_params,
                    "fetched_at": utcnow().isoformat(),
                    "body_sha256": digest(body),
                    "body": body,
                }
                self.store.save_source(request_key, envelope)
                return envelope
            except (httpx.TransportError, ValueError):
                if attempt == 2:
                    raise SourceError(f"{host}: network or JSON failure (3 attempts)") from None
                time.sleep(2**attempt)
        raise SourceError(f"{parsed.hostname}: retry limit reached")


def normalize_ohlc(rows, interval, as_of):
    """Kraken always appends a mutable candle. Drop it, then verify bar close time."""
    if interval not in INTERVALS:
        raise ValueError("Unsupported Kraken interval")
    candles = []
    for row in rows[:-1]:
        stamp = datetime.fromtimestamp(int(row[0]), UTC)
        if stamp.timestamp() + interval * 60 > as_of.timestamp():
            continue
        candles.append(
            Candle(
                timestamp=stamp, open=row[1], high=row[2], low=row[3], close=row[4], volume=row[6]
            )
        )
    if not candles:
        raise SourceError("No closed candles returned")
    times = [c.timestamp for c in candles]
    if times != sorted(set(times)):
        raise SourceError("Duplicate or unordered Kraken candles")
    return candles


def collect(client, asset, intervals=(60, 240, 1440), enrich=False, fred_series=()):
    provenance, warnings = [], []

    def request(url, params=None, **kwargs):
        item = client.get(url, params, **kwargs)
        provenance.append({k: v for k, v in item.items() if k != "body"})
        return item

    root = "https://api.kraken.com/0/public/"
    pair = asset["kraken_pair"]
    meta = request(root + "AssetPairs", {"pair": pair}, ttl=3600)["body"]["result"]
    if len(meta) != 1:
        raise SourceError("Pair must resolve to exactly one instrument")
    pair_key, info = next(iter(meta.items()))
    quote_code = info["quote"]
    # Kraken fiat identifiers; other quotes must map explicitly (never guess FX rates).
    quote_code = {
        "ZUSD": "USD",
        "ZEUR": "EUR",
        "ZGBP": "GBP",
        "ZCAD": "CAD",
        "ZJPY": "JPY",
        "ZAUD": "AUD",
        "ZCHF": "CHF",
    }.get(quote_code, quote_code)
    instrument = Instrument(
        symbol=asset["symbol"],
        pair=pair_key,
        base=info["base"],
        quote=quote_code,
        status=info.get("status", "unknown"),
        min_quantity=info["ordermin"],
        min_cost=info.get("costmin", 0),
        quantity_decimals=info["lot_decimals"],
        price_decimals=info["pair_decimals"],
        tick_size=info.get("tick_size", 10 ** -info["pair_decimals"]),
    )
    candles = {}
    for interval in intervals:
        env = request(root + "OHLC", {"pair": pair, "interval": interval}, ttl=30)
        result = env["body"]["result"]
        rows = next(v for k, v in result.items() if k != "last")
        candles[interval] = normalize_ohlc(
            rows, interval, datetime.fromisoformat(env["fetched_at"])
        )
    env = request(root + "Depth", {"pair": pair, "count": 100}, ttl=5)
    book = next(iter(env["body"]["result"].values()))
    ask, bid = float(book["asks"][0][0]), float(book["bids"][0][0])
    depth = sum(float(p) * float(v) for p, v, *_ in book["asks"] if float(p) <= ask * 1.001)
    market_quote = Quote(as_of=env["fetched_at"], ask=ask, bid=bid, ask_depth_near_quote=depth)
    fundamentals = {}
    if enrich:
        sources = []
        if asset.get("coingecko_id"):
            key = os.getenv("COINGECKO_DEMO_API_KEY", "")
            if key:
                sources.append(
                    (
                        "coingecko",
                        "https://api.coingecko.com/api/v3/coins/markets",
                        {"vs_currency": "usd", "ids": asset["coingecko_id"]},
                        {"x-cg-demo-api-key": key},
                    )
                )
            else:
                warnings.append("CoinGecko omitted: COINGECKO_DEMO_API_KEY missing")
        if asset.get("defillama_chain"):
            chain = quote(asset["defillama_chain"], safe="")
            sources.append(
                (
                    "defillama_chain_tvl",
                    f"https://api.llama.fi/v2/historicalChainTvl/{chain}",
                    {},
                    {},
                )
            )
        if os.getenv("FRED_API_KEY"):
            for series in fred_series:
                sources.append(
                    (
                        f"fred_{series}",
                        "https://api.stlouisfed.org/fred/series/observations",
                        {
                            "series_id": series,
                            "api_key": os.environ["FRED_API_KEY"],
                            "file_type": "json",
                            "sort_order": "desc",
                            "limit": 30,
                        },
                        {},
                    )
                )
        elif fred_series:
            warnings.append("FRED omitted: FRED_API_KEY missing")
        for name, url, params, headers in sources:
            try:
                fundamentals[name] = request(url, params, headers=headers, ttl=3600)["body"]
            except SourceError as error:
                warnings.append(f"{name} unavailable: {error}")
    return Dataset(
        created_at=utcnow(),
        instrument=instrument,
        quote=market_quote,
        candles=candles,
        fundamentals=fundamentals,
        provenance=provenance,
        warnings=warnings,
    )
