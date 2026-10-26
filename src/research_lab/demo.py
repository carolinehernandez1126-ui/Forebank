from datetime import UTC, datetime, timedelta

import numpy as np

from .models import Candle, Dataset, Instrument, Quote


def synthetic_dataset(now=None, bars=720):
    now = now or datetime(2026, 1, 1, 12, tzinfo=UTC)
    rng = np.random.default_rng(42)
    candles = {}
    for interval in (60, 240, 1440):
        end = int(now.timestamp()) // (interval * 60) * interval * 60
        prices = 100 * np.exp(np.cumsum(rng.normal(0.0003, 0.008, bars + 1)))
        rows = []
        for i in range(bars):
            o, c = prices[i], prices[i + 1]
            rows.append(
                Candle(
                    timestamp=datetime.fromtimestamp(end - (bars - i) * interval * 60, UTC),
                    open=o,
                    close=c,
                    high=max(o, c) * 1.005,
                    low=min(o, c) * 0.995,
                    volume=float(rng.uniform(10, 100)),
                )
            )
        candles[interval] = rows
    ask = candles[60][-1].close
    return Dataset(
        created_at=now,
        synthetic=True,
        instrument=Instrument(
            symbol="DEMO/USD",
            pair="DEMOUSD",
            base="DEMO",
            quote="USD",
            status="online",
            min_quantity=0.001,
            min_cost=1,
            quantity_decimals=6,
            price_decimals=2,
            tick_size=0.01,
        ),
        quote=Quote(as_of=now, bid=ask * 0.9998, ask=ask, ask_depth_near_quote=1000000),
        candles=candles,
        warnings=["SYNTHETIC: seed=42; never use to trade"],
        provenance=[
            {
                "provider": "synthetic",
                "seed": 42,
                "fetched_at": (now - timedelta(seconds=1)).isoformat(),
            }
        ],
    )
