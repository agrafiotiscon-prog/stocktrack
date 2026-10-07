"""SQLite storage for processed filings and insider buy events."""

from __future__ import annotations

import dataclasses
import datetime as dt
import sqlite3
from pathlib import Path

from stocktrack.signals import BuyEvent

SCHEMA = """
CREATE TABLE IF NOT EXISTS filings (
    accession     TEXT PRIMARY KEY,
    form_type     TEXT,
    cik           TEXT,
    processed_at  TEXT NOT NULL,
    has_buy       INTEGER NOT NULL DEFAULT 0,
    error         TEXT
);

CREATE TABLE IF NOT EXISTS buys (
    accession       TEXT PRIMARY KEY,
    issuer_cik      TEXT NOT NULL,
    issuer_name     TEXT,
    ticker          TEXT,
    owner_cik       TEXT,
    owner_name      TEXT,
    owner_names     TEXT,
    role            TEXT,
    officer_title   TEXT,
    first_date      TEXT,
    last_date       TEXT,
    filed_at        TEXT,
    shares          REAL,
    value           REAL,
    avg_price       REAL,
    shares_before   REAL,
    shares_after    REAL,
    plan_10b5_1     INTEGER,
    n_transactions  INTEGER,
    url             TEXT,
    alerted_at      TEXT
);

CREATE INDEX IF NOT EXISTS buys_issuer_date ON buys (issuer_cik, last_date);
CREATE INDEX IF NOT EXISTS buys_last_date ON buys (last_date);
CREATE INDEX IF NOT EXISTS buys_ticker ON buys (ticker);
"""

_BUY_FIELDS = [f.name for f in dataclasses.fields(BuyEvent)]


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


class Database:
    def __init__(self, path: str | Path) -> None:
        if str(path) != ":memory:":
            path = Path(path).expanduser()
            path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)

    def close(self) -> None:
        self.conn.close()

    def seen(self, accession: str) -> bool:
        row = self.conn.execute("SELECT 1 FROM filings WHERE accession = ?", (accession,)).fetchone()
        return row is not None

    def record_filing(
        self, accession: str, form_type: str, cik: str, buy: BuyEvent | None, error: str | None = None
    ) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT OR REPLACE INTO filings (accession, form_type, cik, processed_at, has_buy, error) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (accession, form_type, cik, _now(), int(buy is not None), error),
            )
            if buy is not None:
                cols = ", ".join(_BUY_FIELDS)
                marks = ", ".join("?" for _ in _BUY_FIELDS)
                self.conn.execute(
                    f"INSERT OR REPLACE INTO buys ({cols}) VALUES ({marks})",
                    [getattr(buy, f) for f in _BUY_FIELDS],
                )

    def mark_alerted(self, accession: str) -> None:
        with self.conn:
            self.conn.execute("UPDATE buys SET alerted_at = ? WHERE accession = ?", (_now(), accession))

    def was_alerted(self, accession: str) -> bool:
        row = self.conn.execute("SELECT alerted_at FROM buys WHERE accession = ?", (accession,)).fetchone()
        return bool(row and row["alerted_at"])

    @staticmethod
    def _to_buy(row: sqlite3.Row) -> BuyEvent:
        d = {f: row[f] for f in _BUY_FIELDS}
        d["plan_10b5_1"] = bool(d["plan_10b5_1"])
        return BuyEvent(**d)

    def buys(
        self,
        since: str | None = None,
        until: str | None = None,
        ticker: str | None = None,
        issuer_cik: str | None = None,
    ) -> list[BuyEvent]:
        """Buy events filtered by last trade date (inclusive, YYYY-MM-DD), newest first."""
        sql, args = "SELECT * FROM buys WHERE 1=1", []
        if since:
            sql += " AND last_date >= ?"
            args.append(since)
        if until:
            sql += " AND last_date <= ?"
            args.append(until)
        if ticker:
            sql += " AND ticker = ?"
            args.append(ticker.upper())
        if issuer_cik:
            sql += " AND issuer_cik = ?"
            args.append(issuer_cik.lstrip("0"))
        sql += " ORDER BY last_date DESC, filed_at DESC"
        return [self._to_buy(r) for r in self.conn.execute(sql, args)]

    def stats(self) -> dict[str, object]:
        c = self.conn
        return {
            "filings": c.execute("SELECT COUNT(*) FROM filings").fetchone()[0],
            "errors": c.execute("SELECT COUNT(*) FROM filings WHERE error IS NOT NULL").fetchone()[0],
            "buys": c.execute("SELECT COUNT(*) FROM buys").fetchone()[0],
            "first_trade": c.execute("SELECT MIN(last_date) FROM buys").fetchone()[0],
            "last_trade": c.execute("SELECT MAX(last_date) FROM buys").fetchone()[0],
        }
