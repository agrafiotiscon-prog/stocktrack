"""Load historical insider purchases from SEC's quarterly Insider Transactions Data Sets.

https://www.sec.gov/data-research/sec-markets-data/insider-transactions-data-sets

Each quarter is a zip of tab-separated tables (one row per filing, owner,
transaction and footnote). Rows are rebuilt into the same Form4 objects the live
parser produces and run through signals.build_buy, so historical events are
defined and scored exactly like live ones.
"""

from __future__ import annotations

import csv
import datetime as dt
import io
import logging
import re
import zipfile
from collections import defaultdict
from pathlib import Path
from typing import Iterator

from stocktrack.form4 import Form4, Owner, Transaction
from stocktrack.sec import HttpClient
from stocktrack.signals import BuyEvent, build_buy

log = logging.getLogger(__name__)

DATASETS_PAGE = "https://www.sec.gov/data-research/sec-markets-data/insider-transactions-data-sets"

# Footnote columns describing the trade itself. Notes on the post-trade balance
# and ownership form are left out, matching form4._HOLDING_FIELDS.
TRADE_FN_COLUMNS = (
    "SECURITY_TITLE_FN",
    "TRANS_DATE_FN",
    "DEEMED_EXECUTION_DATE_FN",
    "EQUITY_SWAP_TRANS_CD_FN",
    "TRANS_TIMELINESS_FN",
    "TRANS_SHARES_FN",
    "TRANS_PRICEPERSHARE_FN",
    "TRANS_ACQUIRED_DISP_CD_FN",
)

_MONTHS = {m: i for i, m in enumerate(
    ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"], 1)}


def sec_date(s: str) -> str:
    """'29-DEC-2025' -> '2025-12-29'; '' on anything unparseable."""
    s = s.strip()
    try:
        d, m, y = s.split("-")
        return dt.date(int(y), _MONTHS[m.upper()], int(d)).isoformat()
    except (ValueError, KeyError):
        return ""


def _num(s: str) -> float | None:
    s = (s or "").replace(",", "").strip()
    try:
        return float(s) if s else None
    except ValueError:
        return None


def _bool(s: str | None) -> bool | None:
    if s is None or not s.strip():
        return None
    return s.strip().lower() in ("1", "true")


def _fn_ids(cell: str) -> list[str]:
    return [x for x in re.split(r"[,\s]+", cell or "") if x]


def _rows(z: zipfile.ZipFile, name: str) -> Iterator[dict[str, str]]:
    with z.open(name) as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
        yield from csv.DictReader(text, delimiter="\t", quoting=csv.QUOTE_NONE)


def quarter_forms(zip_path: str | Path, doc_types: tuple[str, ...] = ("4",)) -> Iterator[Form4]:
    """Form4 objects for every filing in the quarter that has an open-market purchase."""
    with zipfile.ZipFile(zip_path) as z:
        txs: dict[str, list[Transaction]] = defaultdict(list)
        for r in _rows(z, "NONDERIV_TRANS.tsv"):
            if r.get("TRANS_CODE") != "P" or r.get("TRANS_ACQUIRED_DISP_CD") != "A":
                continue
            ids: list[str] = []
            for col in TRADE_FN_COLUMNS:
                ids.extend(_fn_ids(r.get(col, "")))
            txs[r["ACCESSION_NUMBER"]].append(
                Transaction(
                    security=r.get("SECURITY_TITLE", ""),
                    date=sec_date(r.get("TRANS_DATE", "")),
                    code="P",
                    shares=_num(r.get("TRANS_SHARES", "")),
                    price=_num(r.get("TRANS_PRICEPERSHARE", "")),
                    acquired_disposed="A",
                    shares_after=_num(r.get("SHRS_OWND_FOLWNG_TRANS", "")),
                    direct_indirect=r.get("DIRECT_INDIRECT_OWNERSHIP", ""),
                    nature=r.get("NATURE_OF_OWNERSHIP", ""),
                    footnote_ids=list(dict.fromkeys(ids)),
                )
            )
        if not txs:
            return

        subs: dict[str, dict[str, str]] = {}
        for r in _rows(z, "SUBMISSION.tsv"):
            if r["ACCESSION_NUMBER"] in txs and r.get("DOCUMENT_TYPE") in doc_types:
                subs[r["ACCESSION_NUMBER"]] = r

        owners: dict[str, list[Owner]] = defaultdict(list)
        for r in _rows(z, "REPORTINGOWNER.tsv"):
            if r["ACCESSION_NUMBER"] not in subs:
                continue
            rel = {x.strip() for x in (r.get("RPTOWNER_RELATIONSHIP") or "").split(",")}
            owners[r["ACCESSION_NUMBER"]].append(
                Owner(
                    cik=r.get("RPTOWNERCIK", ""),
                    name=r.get("RPTOWNERNAME", ""),
                    is_director="Director" in rel,
                    is_officer="Officer" in rel,
                    is_ten_percent="TenPercentOwner" in rel,
                    is_other="Other" in rel,
                    officer_title=r.get("RPTOWNER_TITLE", "") or "",
                    other_text=r.get("RPTOWNER_TXT", "") or "",
                )
            )

        notes: dict[str, dict[str, str]] = defaultdict(dict)
        for r in _rows(z, "FOOTNOTES.tsv"):
            if r["ACCESSION_NUMBER"] in subs:
                notes[r["ACCESSION_NUMBER"]][r.get("FOOTNOTE_ID", "")] = " ".join(
                    (r.get("FOOTNOTE_TXT") or "").split())

    for acc, s in subs.items():
        ticker = (s.get("ISSUERTRADINGSYMBOL") or "").strip().upper()
        if ticker in ("NONE", "N/A", "NA"):
            ticker = ""
        yield Form4(
            accession=acc,
            form_type=s.get("DOCUMENT_TYPE", ""),
            period=sec_date(s.get("PERIOD_OF_REPORT", "")),
            issuer_cik=s.get("ISSUERCIK", ""),
            issuer_name=s.get("ISSUERNAME", ""),
            ticker=ticker,
            owners=owners.get(acc, []),
            transactions=txs[acc],
            plan_10b5_1=_bool(s.get("AFF10B5ONE")),
            filed_at=sec_date(s.get("FILING_DATE", "")),
            footnotes=notes.get(acc, {}),
            remarks=s.get("REMARKS", "") or "",
        )


def quarter_events(zip_path: str | Path) -> list[BuyEvent]:
    out = []
    for form in quarter_forms(zip_path):
        if not form.filed_at:
            continue
        buy = build_buy(form)
        if buy is not None:
            out.append(buy)
    return out


def dataset_urls(http: HttpClient) -> list[str]:
    html = http.get_text(DATASETS_PAGE)
    paths = sorted(set(re.findall(r'href="([^"]*\d{4}q\d_form345\.zip)"', html)))
    return [p if p.startswith("http") else "https://www.sec.gov" + p for p in paths]


def download_datasets(http: HttpClient, cache_dir: str | Path, refresh_latest: bool = False,
                      progress=None) -> list[Path]:
    """Download every quarterly zip not already cached; returns local paths, oldest first."""
    cache = Path(cache_dir).expanduser()
    cache.mkdir(parents=True, exist_ok=True)
    urls = dataset_urls(http)
    paths = []
    for i, url in enumerate(urls, 1):
        path = cache / url.rsplit("/", 1)[-1]
        latest = i == len(urls)
        if not path.exists() or (latest and refresh_latest):
            tmp = path.with_suffix(".part")
            tmp.write_bytes(http.get(url))
            tmp.replace(path)
        paths.append(path)
        if progress:
            progress(i, len(urls))
    return sorted(paths, key=lambda p: p.name)
