"""Ingest Form 4 filings from EDGAR and rank the insider buys they contain."""

from __future__ import annotations

import datetime as dt
import logging
import urllib.error
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Callable, Iterable

from stocktrack.db import Database
from stocktrack.feeds import (
    FORM4_TYPES,
    FORM4_TYPES_WITH_AMENDMENTS,
    FilingRef,
    daily_index_url,
    latest_feed_url,
    parse_atom,
    parse_daily_index,
)
from stocktrack.form4 import Form4ParseError, parse_submission
from stocktrack.prices import Quote
from stocktrack.sec import HttpClient
from stocktrack.signals import (
    CLUSTER_WINDOW_DAYS,
    BuyEvent,
    Score,
    build_buy,
    cluster_size,
    dedupe_purchases,
    score_buy,
)

log = logging.getLogger(__name__)


@dataclass
class Signal:
    buy: BuyEvent
    score: Score
    quote: Quote | None = None


@dataclass
class Cluster:
    issuer_cik: str
    issuer_name: str
    ticker: str
    buys: list[BuyEvent]  # oldest first, repeat reports of one purchase removed

    @property
    def insiders(self) -> list[BuyEvent]:
        """One (the largest) buy per distinct insider."""
        best: dict[str, BuyEvent] = {}
        for b in self.buys:
            if b.owner_cik not in best or b.value > best[b.owner_cik].value:
                best[b.owner_cik] = b
        return sorted(best.values(), key=lambda b: b.value, reverse=True)

    @property
    def total_value(self) -> float:
        return sum(b.value for b in self.buys)

    @property
    def first_date(self) -> str:
        return min(b.last_date for b in self.buys)

    @property
    def last_date(self) -> str:
        return max(b.last_date for b in self.buys)


@dataclass
class IngestResult:
    filings: int = 0
    buys: list[BuyEvent] = field(default_factory=list)
    errors: int = 0


def shift(day: str, days: int) -> str:
    return (dt.date.fromisoformat(day) + dt.timedelta(days=days)).isoformat()


class Tracker:
    def __init__(
        self,
        db: Database,
        client: HttpClient | None = None,
        include_amendments: bool = False,
        window_days: int = CLUSTER_WINDOW_DAYS,
    ) -> None:
        self.db = db
        self.client = client
        self.form_types = FORM4_TYPES_WITH_AMENDMENTS if include_amendments else FORM4_TYPES
        self.window_days = window_days

    def _http(self) -> HttpClient:
        if self.client is None:
            raise RuntimeError("this operation needs network access; create Tracker with an HttpClient")
        return self.client

    # --- finding filings -------------------------------------------------

    def latest_refs(self, max_pages: int = 10, page_size: int = 100) -> list[FilingRef]:
        """Unprocessed Form 4s from the live feed, paging back until we reach known ones."""
        refs: list[FilingRef] = []
        queued: set[str] = set()
        for page in range(max_pages):
            page_refs = parse_atom(self._http().get(latest_feed_url(page * page_size, page_size)), self.form_types)
            if not page_refs:
                break
            unseen = [r for r in page_refs if not self.db.seen(r.accession)]
            # A filing is listed under both issuer and owner, possibly across a page break.
            new = [r for r in unseen if r.accession not in queued]
            refs.extend(new)
            queued.update(r.accession for r in new)
            if len(unseen) < len(page_refs):
                break  # caught up with what earlier scans processed
        return refs

    def day_refs(self, day: dt.date) -> list[FilingRef] | None:
        """Form 4s filed on a given day, or None if EDGAR has no index for it (weekend,
        holiday, or today before the evening index is published)."""
        try:
            text = self._http().get_text(daily_index_url(day))
        except urllib.error.HTTPError as e:
            if e.code in (403, 404):
                return None
            raise
        return parse_daily_index(text, self.form_types)

    # --- processing -------------------------------------------------------

    def ingest(
        self,
        refs: Iterable[FilingRef],
        progress: Callable[[int, int], None] | None = None,
    ) -> IngestResult:
        """Download and parse each unseen filing, storing any insider buy it contains."""
        todo = [r for r in refs if not self.db.seen(r.accession)]
        result = IngestResult()
        for i, ref in enumerate(todo, 1):
            if progress:
                progress(i, len(todo))
            try:
                text = self._http().get_text(ref.submission_url)
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    self.db.record_filing(ref.accession, ref.form_type, ref.cik, None, "HTTP 404")
                else:
                    log.warning("skipping %s for now: HTTP %s", ref.accession, e.code)
                result.errors += 1
                continue
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                log.warning("skipping %s for now: %s", ref.accession, e)
                result.errors += 1
                continue
            try:
                buy = build_buy(parse_submission(text, ref.accession))
                error = None
            except Form4ParseError as e:
                log.warning("could not parse %s: %s", ref.accession, e)
                buy, error = None, str(e)
                result.errors += 1
            self.db.record_filing(ref.accession, ref.form_type, ref.cik, buy, error)
            result.filings += 1
            if buy is not None:
                result.buys.append(buy)
        return result

    def scan_latest(self, max_pages: int = 10, progress=None) -> IngestResult:
        return self.ingest(self.latest_refs(max_pages=max_pages), progress)

    def backfill(self, days: int, end: dt.date | None = None, progress=None, on_day=None) -> IngestResult:
        """Ingest the daily indexes for the last `days` calendar days (ending at `end`)."""
        end = end or dt.date.today()
        total = IngestResult()
        for offset in range(days - 1, -1, -1):
            day = end - dt.timedelta(days=offset)
            if day.weekday() >= 5:
                continue
            refs = self.day_refs(day)
            if on_day:
                on_day(day, refs)
            if not refs:
                continue
            r = self.ingest(refs, progress)
            total.filings += r.filings
            total.errors += r.errors
            total.buys.extend(r.buys)
        return total

    # --- ranking ----------------------------------------------------------

    def score(self, buy: BuyEvent) -> Signal:
        w = self.window_days
        try:
            peers = self.db.buys(
                issuer_cik=buy.issuer_cik, since=shift(buy.last_date, -w), until=shift(buy.last_date, w)
            )
        except ValueError:
            peers = []
        return Signal(buy, score_buy(buy, cluster_size(buy, peers, w)))

    def ranked(
        self,
        since: str,
        until: str | None = None,
        ticker: str | None = None,
        min_score: int = 0,
        min_value: float = 0,
    ) -> list[Signal]:
        """Buys with a last trade date in [since, until], best first."""
        w = self.window_days
        peers = self.db.buys(since=shift(since, -w), until=shift(until, w) if until else None, ticker=ticker)
        by_issuer: dict[str, list[BuyEvent]] = defaultdict(list)
        for p in peers:
            by_issuer[p.issuer_cik].append(p)

        signals = []
        for b in peers:
            if b.last_date < since or (until and b.last_date > until):
                continue
            if b.value < min_value:
                continue
            s = Signal(b, score_buy(b, cluster_size(b, by_issuer[b.issuer_cik], w)))
            if s.score.total >= min_score:
                signals.append(s)
        signals.sort(key=lambda s: (s.score.total, s.buy.value), reverse=True)
        keep = {id(b) for b in dedupe_purchases([s.buy for s in signals])}
        return [s for s in signals if id(s.buy) in keep]

    def clusters(self, since: str, until: str | None = None, min_insiders: int = 2) -> list[Cluster]:
        """Stocks where at least `min_insiders` different insiders bought in the period."""
        by_issuer: dict[str, list[BuyEvent]] = defaultdict(list)
        for b in self.db.buys(since=since, until=until):
            by_issuer[b.issuer_cik].append(b)
        out = []
        for buys in by_issuer.values():
            buys = dedupe_purchases(sorted(buys, key=lambda b: (b.last_date, b.filed_at)))
            if len({b.owner_cik for b in buys}) >= min_insiders:
                latest = buys[-1]
                out.append(Cluster(latest.issuer_cik, latest.issuer_name, latest.ticker, buys))
        out.sort(key=lambda c: (len(c.insiders), c.total_value), reverse=True)
        return out
