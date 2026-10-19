"""Daily price histories for backtesting, and safe ticker resolution.

Prices come from Yahoo Finance's public chart endpoint (adjusted for splits and
dividends) and are cached on disk. Two data hazards are handled here:

* Ticker reuse: symbols get reassigned to new companies (BBBY today is not the
  Bed Bath & Beyond of 2020). A filing's ticker is only trusted if SEC's current
  CIK -> ticker map still assigns it to the same company; otherwise the
  company's current ticker is used, and if it has none it gets no prices.
* Survivorship: Yahoo has no history for delisted symbols. Those events get no
  prices, and coverage is reported so the bias is visible.
"""

from __future__ import annotations

import bisect
import concurrent.futures as cf
import datetime as dt
import gzip
import json
import logging
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from stocktrack.sec import HttpClient

log = logging.getLogger(__name__)

CHART_URL = ("https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
             "?period1={p1}&period2={p2}&interval=1d&events=split")
TICKERS_URL = "https://www.sec.gov/files/company_tickers_exchange.json"
HISTORY_START = dt.date(2005, 1, 1)
BENCHMARK = "SPY"


@dataclass
class PriceHistory:
    symbol: str
    dates: list[str]  # ISO dates of trading days, ascending
    open: list[float]  # split/dividend adjusted
    close: list[float]  # split/dividend adjusted
    dollar_volume_day: list[float]  # dollars traded that day
    raw_close: list[float]  # the price actually quoted that day (no split adjustment)

    def index_after(self, day: str) -> int | None:
        """Index of the first trading day strictly after `day`."""
        i = bisect.bisect_right(self.dates, day)
        return i if i < len(self.dates) else None

    def index_on_or_before(self, day: str) -> int | None:
        i = bisect.bisect_right(self.dates, day) - 1
        return i if i >= 0 else None

    def dollar_volume(self, i: int, days: int = 20) -> float:
        """Average daily dollar volume over the `days` sessions before index i."""
        vals = self.dollar_volume_day[max(0, i - days):i]
        return sum(vals) / len(vals) if vals else 0.0

    def to_json(self) -> dict:
        return {"symbol": self.symbol, "dates": self.dates, "open": self.open, "close": self.close,
                "dollar_volume_day": self.dollar_volume_day, "raw_close": self.raw_close}

    @classmethod
    def from_json(cls, d: dict) -> "PriceHistory":
        return cls(d["symbol"], d["dates"], d["open"], d["close"], d["dollar_volume_day"], d["raw_close"])


def parse_chart(symbol: str, data: dict) -> PriceHistory | None:
    """Turn a Yahoo chart response into an adjusted history, dropping incomplete bars."""
    result = (data.get("chart") or {}).get("result")
    if not result:
        return None
    r = result[0]
    stamps = r.get("timestamp") or []
    quote = (r.get("indicators") or {}).get("quote") or [{}]
    adj = ((r.get("indicators") or {}).get("adjclose") or [{}])[0].get("adjclose")
    q = quote[0]
    offset = (r.get("meta") or {}).get("gmtoffset") or 0

    def day_of(ts: int) -> str:
        return dt.datetime.fromtimestamp(ts + offset, dt.timezone.utc).date().isoformat()

    # Yahoo's open/close/volume are split-adjusted; adjclose also adjusts for dividends.
    splits = []
    for s in ((r.get("events") or {}).get("splits") or {}).values():
        try:
            ratio = float(s["numerator"]) / float(s["denominator"])
        except (KeyError, ValueError, ZeroDivisionError):
            continue
        if ratio > 0:
            splits.append((day_of(int(s["date"])), ratio))

    opens, closes, vols = q.get("open") or [], q.get("close") or [], q.get("volume") or []
    rows: dict[str, tuple[float, float, float, float]] = {}
    for k, ts in enumerate(stamps):
        try:
            o, c, a = opens[k], closes[k], (adj[k] if adj else closes[k])
            v = vols[k] or 0
        except IndexError:
            continue
        if not o or not c or not a or o <= 0 or c <= 0 or a <= 0:
            continue
        day = day_of(ts)
        later_splits = 1.0
        for split_day, ratio in splits:
            if split_day > day:
                later_splits *= ratio
        # last bar for a date wins
        rows[day] = (o * a / c, a, c * float(v), c * later_splits)
    if not rows:
        return None
    days = sorted(rows)
    return PriceHistory(
        symbol=symbol,
        dates=days,
        open=[rows[d][0] for d in days],
        close=[rows[d][1] for d in days],
        dollar_volume_day=[rows[d][2] for d in days],
        raw_close=[rows[d][3] for d in days],
    )


def yahoo_symbol(ticker: str) -> str:
    return ticker.strip().upper().replace(".", "-").replace("/", "-")


class PriceStore:
    """Disk-cached Yahoo daily histories."""

    def __init__(self, cache_dir: str | Path, max_age_days: float = 1.0, workers: int = 8) -> None:
        self.dir = Path(cache_dir).expanduser()
        self.dir.mkdir(parents=True, exist_ok=True)
        self.max_age = max_age_days * 86400
        self.workers = workers
        self._mem: dict[str, PriceHistory | None] = {}

    def _path(self, symbol: str) -> Path:
        return self.dir / f"{urllib.parse.quote(symbol, safe='')}.json.gz"

    def _read_cache(self, symbol: str) -> tuple[bool, PriceHistory | None]:
        p = self._path(symbol)
        if not p.exists() or time.time() - p.stat().st_mtime > self.max_age:
            return False, None
        try:
            d = json.loads(gzip.decompress(p.read_bytes()))
        except (OSError, ValueError):
            return False, None
        return True, (PriceHistory.from_json(d) if d.get("dates") else None)

    def _write_cache(self, symbol: str, hist: PriceHistory | None) -> None:
        body = hist.to_json() if hist else {"symbol": symbol, "missing": True}
        tmp = self._path(symbol).with_suffix(".tmp")
        tmp.write_bytes(gzip.compress(json.dumps(body, separators=(",", ":")).encode()))
        tmp.replace(self._path(symbol))

    def _download(self, symbol: str, retries: int = 4) -> PriceHistory | None:
        p2 = int(time.time()) + 86400
        p1 = int(dt.datetime(HISTORY_START.year, HISTORY_START.month, HISTORY_START.day,
                             tzinfo=dt.timezone.utc).timestamp())
        url = CHART_URL.format(sym=urllib.parse.quote(symbol), p1=p1, p2=p2)
        delay = 2.0
        for attempt in range(retries + 1):
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    return parse_chart(symbol, json.load(resp))
            except urllib.error.HTTPError as e:
                if e.code in (400, 404, 422):
                    return None
                if attempt == retries:
                    raise
            except (urllib.error.URLError, TimeoutError, ConnectionError, ValueError):
                if attempt == retries:
                    raise
            time.sleep(delay)
            delay *= 2
        return None

    def load(self, symbol: str) -> PriceHistory | None:
        """Read a cached history whatever its age, without downloading or keeping it in memory."""
        p = self._path(yahoo_symbol(symbol))
        if not p.exists():
            return None
        try:
            d = json.loads(gzip.decompress(p.read_bytes()))
        except (OSError, ValueError):
            return None
        return PriceHistory.from_json(d) if d.get("dates") else None

    def get(self, symbol: str, refresh: bool = False) -> PriceHistory | None:
        symbol = yahoo_symbol(symbol)
        if symbol in self._mem and not refresh:
            return self._mem[symbol]
        hit, hist = (False, None) if refresh else self._read_cache(symbol)
        if not hit:
            hist = self._download(symbol)
            self._write_cache(symbol, hist)
        self._mem[symbol] = hist
        return hist

    def prefetch(self, symbols, progress=None) -> dict[str, int]:
        """Download every symbol not already fresh in the cache, in parallel."""
        todo = sorted({yahoo_symbol(s) for s in symbols if s})
        todo = [s for s in todo if not self._read_cache(s)[0]]
        stats = {"downloaded": 0, "missing": 0, "failed": 0}

        def one(sym: str) -> str:
            try:
                hist = self._download(sym)
            except Exception as e:  # keep going; the symbol is retried next run
                log.warning("price download failed for %s: %s", sym, e)
                return "failed"
            self._write_cache(sym, hist)
            return "downloaded" if hist else "missing"

        with cf.ThreadPoolExecutor(self.workers) as ex:
            for i, outcome in enumerate(ex.map(one, todo), 1):
                stats[outcome] += 1
                if progress:
                    progress(i, len(todo))
        return stats


class TickerMap:
    """SEC's current CIK -> ticker assignments (company_tickers_exchange.json)."""

    def __init__(self, rows: list[list]) -> None:
        self.by_cik: dict[str, list[tuple[str, str]]] = {}
        self.cik_of: dict[str, str] = {}
        for cik, _name, ticker, exchange in rows:
            if not ticker:
                continue
            c, t = str(int(cik)), str(ticker).upper()
            self.by_cik.setdefault(c, []).append((t, exchange or ""))
            self.cik_of.setdefault(yahoo_symbol(t), c)

    @classmethod
    def load(cls, http: HttpClient, cache_dir: str | Path, max_age_days: float = 1.0) -> "TickerMap":
        path = Path(cache_dir).expanduser() / "company_tickers_exchange.json"
        if not path.exists() or time.time() - path.stat().st_mtime > max_age_days * 86400:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(http.get(TICKERS_URL))
        return cls(json.loads(path.read_text())["data"])

    def resolve(self, issuer_cik: str, filing_ticker: str) -> tuple[str | None, str]:
        """(symbol to price with, how it was resolved).

        `how` is one of: "filing" (ticker still belongs to this company), "current"
        (company now trades under another ticker), "reused" (the filing's ticker now
        belongs to someone else and the company has no ticker), "unlisted".
        """
        cik = str(int(issuer_cik)) if issuer_cik and issuer_cik.isdigit() else issuer_cik
        current = self.by_cik.get(cik, [])
        ft = yahoo_symbol(filing_ticker) if filing_ticker else ""
        if ft and any(yahoo_symbol(t) == ft for t, _ in current):
            return ft, "filing"
        if current:
            return yahoo_symbol(current[0][0]), "current"
        if ft and ft in self.cik_of:
            return None, "reused"
        return None, "unlisted"

    def exchange(self, issuer_cik: str) -> str:
        cur = self.by_cik.get(str(int(issuer_cik)) if issuer_cik.isdigit() else issuer_cik, [])
        return cur[0][1] if cur else ""
