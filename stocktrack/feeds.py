"""Find Form 4 filings on EDGAR.

Two sources:
  * the "latest filings" Atom feed, updated within minutes of acceptance (for live scanning)
  * the daily form index, published each evening (for backfilling past days)
"""

from __future__ import annotations

import datetime as dt
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass

EDGAR = "https://www.sec.gov"
ATOM_NS = {"a": "http://www.w3.org/2005/Atom"}

FORM4_TYPES = ("4",)
FORM4_TYPES_WITH_AMENDMENTS = ("4", "4/A")


@dataclass(frozen=True)
class FilingRef:
    accession: str  # e.g. 0001062993-26-005214
    cik: str  # any CIK the filing is filed under (issuer or reporting owner)
    form_type: str
    filed: str = ""  # YYYY-MM-DD or ISO datetime, if known

    @property
    def submission_url(self) -> str:
        """Full submission text file, which embeds the Form 4 XML."""
        return f"{EDGAR}/Archives/edgar/data/{int(self.cik)}/{self.accession}.txt"


def filing_index_url(cik: str, accession: str) -> str:
    return (
        f"{EDGAR}/Archives/edgar/data/{int(cik)}/"
        f"{accession.replace('-', '')}/{accession}-index.htm"
    )


def latest_feed_url(start: int = 0, count: int = 100) -> str:
    # type=4 is a prefix match (it also returns 424B3, 425, ...); parse_atom filters.
    return (
        f"{EDGAR}/cgi-bin/browse-edgar?action=getcurrent&type=4&company=&dateb="
        f"&owner=include&start={start}&count={count}&output=atom"
    )


def daily_index_url(day: dt.date) -> str:
    quarter = (day.month - 1) // 3 + 1
    return f"{EDGAR}/Archives/edgar/daily-index/{day.year}/QTR{quarter}/form.{day:%Y%m%d}.idx"


_ACCESSION_RE = re.compile(r"accession-number=(\d{10}-\d{2}-\d{6})")
_CIK_RE = re.compile(r"/edgar/data/(\d+)/")


def parse_atom(data: bytes | str, form_types: tuple[str, ...] = FORM4_TYPES) -> list[FilingRef]:
    """Parse the EDGAR latest-filings Atom feed, newest first, one ref per accession."""
    root = ET.fromstring(data)
    refs: list[FilingRef] = []
    seen: set[str] = set()
    for entry in root.findall("a:entry", ATOM_NS):
        cat = entry.find("a:category", ATOM_NS)
        form_type = cat.get("term", "") if cat is not None else ""
        if form_type not in form_types:
            continue
        m = _ACCESSION_RE.search(entry.findtext("a:id", "", ATOM_NS))
        link = entry.find("a:link", ATOM_NS)
        c = _CIK_RE.search(link.get("href", "")) if link is not None else None
        if not m or not c or m.group(1) in seen:
            continue
        seen.add(m.group(1))
        refs.append(
            FilingRef(
                accession=m.group(1),
                cik=c.group(1),
                form_type=form_type,
                filed=entry.findtext("a:updated", "", ATOM_NS),
            )
        )
    return refs


def parse_daily_index(text: str, form_types: tuple[str, ...] = FORM4_TYPES) -> list[FilingRef]:
    """Parse a form.YYYYMMDD.idx daily index, one ref per accession.

    Data lines look like:
    4                AFLAC INC                       4977        20261006    edgar/data/4977/0001104659-26-113911.txt
    Company names can contain runs of spaces, so the line is split from the right.
    """
    refs: list[FilingRef] = []
    seen: set[str] = set()
    for line in text.splitlines():
        form_type = line[:17].strip()
        if form_type not in form_types:
            continue
        parts = line.rsplit(None, 3)
        if len(parts) != 4:
            continue
        _, cik, date, path = parts
        accession = path.rsplit("/", 1)[-1].removesuffix(".txt")
        if accession in seen or not cik.isdigit():
            continue
        seen.add(accession)
        filed = f"{date[:4]}-{date[4:6]}-{date[6:8]}" if len(date) == 8 else ""
        refs.append(FilingRef(accession=accession, cik=cik, form_type=form_type, filed=filed))
    return refs
