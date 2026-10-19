"""SQLite store for the historical event set used by backtests."""

from __future__ import annotations

import dataclasses
import sqlite3
from pathlib import Path
from typing import Iterable

from stocktrack.signals import BuyEvent

_FIELDS = [f.name for f in dataclasses.fields(BuyEvent)]
_TYPES = {"shares": "REAL", "value": "REAL", "avg_price": "REAL", "shares_before": "REAL",
          "shares_after": "REAL", "plan_10b5_1": "INTEGER", "plan_purchase": "INTEGER",
          "n_transactions": "INTEGER"}

SCHEMA = (
    "CREATE TABLE IF NOT EXISTS events ("
    + ", ".join(f"{f} {_TYPES.get(f, 'TEXT')}" + (" PRIMARY KEY" if f == "accession" else "") for f in _FIELDS)
    + ", source TEXT);\n"
    "CREATE TABLE IF NOT EXISTS loaded (name TEXT PRIMARY KEY, events INTEGER);\n"
    "CREATE INDEX IF NOT EXISTS events_filed ON events (filed_at);\n"
)


class ResearchDB:
    def __init__(self, path: str | Path) -> None:
        if str(path) != ":memory:":
            path = Path(path).expanduser()
            path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)

    def close(self) -> None:
        self.conn.close()

    def is_loaded(self, name: str) -> bool:
        return self.conn.execute("SELECT 1 FROM loaded WHERE name = ?", (name,)).fetchone() is not None

    def add_events(self, events: Iterable[BuyEvent], source: str, loaded_name: str | None = None) -> int:
        cols = ", ".join(_FIELDS) + ", source"
        marks = ", ".join("?" for _ in range(len(_FIELDS) + 1))
        rows = [[getattr(e, f) for f in _FIELDS] + [source] for e in events]
        with self.conn:
            self.conn.executemany(f"INSERT OR IGNORE INTO events ({cols}) VALUES ({marks})", rows)
            if loaded_name:
                self.conn.execute("INSERT OR REPLACE INTO loaded VALUES (?, ?)", (loaded_name, len(rows)))
        return len(rows)

    def forget(self, name: str) -> None:
        with self.conn:
            self.conn.execute("DELETE FROM loaded WHERE name = ?", (name,))

    def events(self, since: str | None = None) -> list[BuyEvent]:
        sql, args = "SELECT * FROM events", []
        if since:
            sql += " WHERE filed_at >= ?"
            args.append(since)
        sql += " ORDER BY filed_at, accession"
        out = []
        for r in self.conn.execute(sql, args):
            d = {f: r[f] for f in _FIELDS}
            d["plan_10b5_1"] = bool(d["plan_10b5_1"])
            d["plan_purchase"] = bool(d["plan_purchase"])
            out.append(BuyEvent(**d))
        return out

    def count(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
