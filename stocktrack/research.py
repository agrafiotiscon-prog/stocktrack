"""Research pipeline: load history, fetch prices, backtest, forward-test ledger, vault.

Local state (not committed): ~/.stocktrack/research.db and ~/.stocktrack/cache/.
Committed state: data/ (backtest summaries, the forward-test ledger) and vault/.
"""

from __future__ import annotations

import logging
import os
from pathlib import Path

from stocktrack.bulk import download_datasets, quarter_events
from stocktrack.history import BENCHMARK, PriceStore, TickerMap
from stocktrack.researchdb import ResearchDB
from stocktrack.sec import HttpClient

log = logging.getLogger(__name__)

HOME = Path(os.environ.get("STOCKTRACK_HOME", Path.home() / ".stocktrack"))
CACHE = HOME / "cache"


def research_db() -> ResearchDB:
    return ResearchDB(os.environ.get("STOCKTRACK_RESEARCH_DB", HOME / "research.db"))


def price_store(max_age_days: float = 7.0) -> PriceStore:
    return PriceStore(CACHE / "prices", max_age_days=max_age_days)


def load_history(http: HttpClient, db: ResearchDB, refresh_latest: bool = True, echo=print) -> int:
    """Download any missing quarterly datasets and load their purchases into the research DB.

    The newest quarter is re-downloaded and re-loaded (SEC revises it), older ones only once.
    """
    paths = download_datasets(http, CACHE / "sec-bulk", refresh_latest=refresh_latest)
    added = 0
    for i, path in enumerate(paths):
        latest = i == len(paths) - 1
        if db.is_loaded(path.name) and not (latest and refresh_latest):
            continue
        events = quarter_events(path)
        db.add_events(events, source="bulk", loaded_name=path.name)
        added += len(events)
        echo(f"{path.name}: {len(events)} purchase filings")
    return added


def fetch_prices(http: HttpClient, db: ResearchDB, store: PriceStore, echo=print) -> dict:
    """Prefetch price histories for every company in the research DB that is still listed."""
    tickers = TickerMap.load(http, CACHE)
    symbols = {BENCHMARK}
    how_counts: dict[str, int] = {}
    for e in db.events():
        sym, how = tickers.resolve(e.issuer_cik, e.ticker)
        how_counts[how] = how_counts.get(how, 0) + 1
        if sym:
            symbols.add(sym)
    echo(f"{len(symbols)} symbols to price; event ticker resolution: {how_counts}")

    def progress(i: int, n: int) -> None:
        if i % 250 == 0 or i == n:
            echo(f"  prices {i}/{n}")

    stats = store.prefetch(symbols, progress=progress)
    echo(f"prices: {stats}")
    return stats
