from datetime import timedelta

import httpx
import numpy as np
import pytest

from research_lab.analytics import dossier, frame, indicators, portfolio_correlations
from research_lab.backtest import simulate, walk_forward
from research_lab.cli import import_csv, parser, run
from research_lab.io import digest, read_json, write_json
from research_lab.providers import PublicClient, SourceError, normalize_ohlc
from research_lab.store import Store


def test_drop_mutable_last_candle_even_if_timestamp_looks_closed(case):
    now = case[0]
    rows = [
        [int((now - timedelta(hours=i)).timestamp()), 10, 11, 9, 10, 10, 1, 2] for i in (3, 2, 1)
    ]
    closed = normalize_ohlc(rows, 60, now)
    assert len(closed) == 2
    assert closed[-1].timestamp == now - timedelta(hours=2)


def test_cache_keeps_original_timestamp_and_redacts_key(tmp_path):
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(200, json={"observations": []})

    store = Store(tmp_path / "lab.sqlite")
    client = PublicClient(store, transport=httpx.MockTransport(handler))
    try:
        first = client.get(
            "https://api.stlouisfed.org/fred/series/observations",
            {"api_key": "do-not-persist", "series_id": "DFF"},
        )
        second = client.get(
            "https://api.stlouisfed.org/fred/series/observations",
            {"api_key": "do-not-persist", "series_id": "DFF"},
        )
        assert len(calls) == 1
        assert first == second
        assert "do-not-persist" not in str(first)
        assert "api_key" not in first["params"]
    finally:
        client.close()
        store.close()


@pytest.mark.parametrize(
    "url",
    [
        "http://api.kraken.com/0/public/OHLC",
        "https://evil.org/data",
        "https://api.kraken.com/0/private/AddOrder",
    ],
)
def test_client_does_not_send_private_or_unknown_requests(tmp_path, url):
    store = Store(tmp_path / "lab.sqlite")
    client = PublicClient(store)
    try:
        with pytest.raises(SourceError):
            client.get(url)
    finally:
        client.close()
        store.close()


def test_indicators_use_only_past_bars_and_handle_flat_prices(case):
    df = frame(case[1].candles[60])
    full = indicators(df)
    past = indicators(df.iloc[:400])
    np.testing.assert_allclose(full.iloc[399], past.iloc[-1], equal_nan=True)
    flat = df.copy()
    flat.loc[:, ["open", "high", "low", "close"]] = 100
    assert indicators(flat).rsi_14.iloc[-1] == 50


def test_walk_forward_test_windows_do_not_overlap(case):
    df = frame(case[1].candles[60])
    out = walk_forward(df)
    assert len(out["folds"]) == 4
    assert out["oos_bars"] == 400
    for i, fold in enumerate(out["folds"]):
        assert fold["train_end"] < fold["test_start"]
        if i:
            assert out["folds"][i - 1]["test_end"] < fold["test_start"]
    assert out == walk_forward(df)  # Seeded bootstrap, deterministic research.


def test_future_test_data_cannot_change_first_fold_parameters(case):
    df = frame(case[1].candles[60])
    original = walk_forward(df)
    changed = df.copy()
    changed.iloc[300:, changed.columns.get_loc("close")] *= 3
    altered = walk_forward(changed)
    assert (original["folds"][0]["fast"], original["folds"][0]["slow"]) == (
        altered["folds"][0]["fast"],
        altered["folds"][0]["slow"],
    )


def test_backtest_costs_reduce_equity(case):
    df = frame(case[1].candles[60])
    free = simulate(df, fee_bps=0, slippage_bps=0)
    cost = simulate(df)
    assert cost["total_return"] < free["total_return"]
    assert cost["closed_trades"] == cost["entries"]


def test_dossier_and_correlation_are_serializable(case, tmp_path):
    data = case[1]
    report = dossier(data, now=case[0])
    assert report["status"] == "RESEARCH_ONLY"
    assert report["dataset_sha256"] == digest(data)
    write_json(tmp_path / "report.json", report)
    assert read_json(tmp_path / "report.json")["symbol"] == "DEMO/USD"
    other = data.model_copy(deep=True)
    other.instrument.symbol = "OTHER/USD"
    correlation = portfolio_correlations([data, other])
    assert correlation["correlation"]["DEMO/USD"]["OTHER/USD"] == pytest.approx(1)


def test_import_does_not_forward_fill_or_accept_duplicates(tmp_path, case):
    path = tmp_path / "data.csv"
    row = f"{int((case[0] - timedelta(hours=1)).timestamp())},100,101,99,100,4,2\n"
    path.write_text(row + row)
    with pytest.raises(ValueError, match="unique"):
        import_csv(path, 60, case[0])


def test_offline_demo_cli_is_reproducible(tmp_path):
    args = parser().parse_args(["demo", "--output-dir", str(tmp_path / "demo")])
    assert run(args) == 0
    one = read_json(tmp_path / "demo/dossier.json")
    assert one["synthetic"] is True
    assert run(args) == 0
    assert one == read_json(tmp_path / "demo/dossier.json")


def test_provider_rate_limit_retries_are_bounded(tmp_path, monkeypatch):
    calls = []
    monkeypatch.setattr("research_lab.providers.time.sleep", lambda _: None)

    def handler(request):
        calls.append(request)
        return httpx.Response(429, headers={"Retry-After": "1"})

    store = Store(tmp_path / "lab.sqlite")
    client = PublicClient(store, transport=httpx.MockTransport(handler))
    try:
        with pytest.raises(SourceError, match="429"):
            client.get("https://api.kraken.com/0/public/Time")
        assert len(calls) == 3
    finally:
        client.close()
        store.close()
