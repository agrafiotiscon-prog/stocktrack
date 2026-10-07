"""Optional current-price lookups, to compare today's price with what insiders paid.

Uses Yahoo Finance's public chart endpoint (no API key). It is unofficial and
can change or rate-limit at any time, so every failure just yields None.
"""

from __future__ import annotations

import json
import logging
import urllib.parse
import urllib.request
from dataclasses import dataclass

log = logging.getLogger(__name__)

CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{}?range=1d&interval=1d"


@dataclass
class Quote:
    ticker: str
    price: float
    high_52w: float | None
    low_52w: float | None

    def change_from(self, paid: float | None) -> float | None:
        if not paid:
            return None
        return self.price / paid - 1

    @property
    def range_position(self) -> float | None:
        """Where the price sits in its 52-week range: 0 = at the low, 1 = at the high."""
        if self.high_52w is None or self.low_52w is None or self.high_52w <= self.low_52w:
            return None
        return (self.price - self.low_52w) / (self.high_52w - self.low_52w)


class PriceService:
    def __init__(self, timeout: float = 10.0) -> None:
        self.timeout = timeout
        self._cache: dict[str, Quote | None] = {}

    def quote(self, ticker: str) -> Quote | None:
        ticker = ticker.strip().upper()
        if not ticker:
            return None
        if ticker not in self._cache:
            self._cache[ticker] = self._fetch(ticker)
        return self._cache[ticker]

    def _fetch(self, ticker: str) -> Quote | None:
        # Yahoo uses '-' for share classes (BRK-B), EDGAR uses '.' (BRK.B)
        symbol = urllib.parse.quote(ticker.replace(".", "-"))
        req = urllib.request.Request(CHART_URL.format(symbol), headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.load(resp)
            meta = data["chart"]["result"][0]["meta"]
            return Quote(
                ticker=ticker,
                price=float(meta["regularMarketPrice"]),
                high_52w=meta.get("fiftyTwoWeekHigh"),
                low_52w=meta.get("fiftyTwoWeekLow"),
            )
        except Exception as e:  # network, HTTP, JSON shape: prices are best-effort
            log.debug("no quote for %s: %s", ticker, e)
            return None
