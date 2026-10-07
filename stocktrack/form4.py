"""Parse SEC Form 4 ownership documents (the XML embedded in each filing)."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field


class Form4ParseError(ValueError):
    pass


@dataclass
class Owner:
    cik: str
    name: str
    is_director: bool = False
    is_officer: bool = False
    is_ten_percent: bool = False
    is_other: bool = False
    officer_title: str = ""
    other_text: str = ""


@dataclass
class Transaction:
    security: str
    date: str  # YYYY-MM-DD
    code: str  # P = open-market or private purchase, S = sale, A = award, ...
    shares: float | None
    price: float | None
    acquired_disposed: str  # A or D
    shares_after: float | None
    direct_indirect: str  # D or I
    nature: str  # for indirect holdings, e.g. "By Trust"
    footnote_ids: list[str] = field(default_factory=list)  # notes on the trade itself, not the holding

    @property
    def is_purchase(self) -> bool:
        return self.code == "P" and self.acquired_disposed == "A"


@dataclass
class Form4:
    accession: str
    form_type: str
    period: str
    issuer_cik: str
    issuer_name: str
    ticker: str
    owners: list[Owner]
    transactions: list[Transaction]
    plan_10b5_1: bool | None  # None on filings that predate the checkbox
    filed_at: str = ""  # acceptance time, ISO 8601
    footnotes: dict[str, str] = field(default_factory=dict)
    remarks: str = ""

    @property
    def purchases(self) -> list[Transaction]:
        return [t for t in self.transactions if t.is_purchase]

    def notes(self, t: Transaction) -> list[str]:
        return [self.footnotes[i] for i in t.footnote_ids if i in self.footnotes]


def _text(el: ET.Element | None, path: str) -> str:
    if el is None:
        return ""
    found = el.find(path)
    if found is None or found.text is None:
        return ""
    return found.text.strip()


def _bool(s: str) -> bool:
    return s.strip().lower() in ("1", "true", "yes")


def _num(s: str) -> float | None:
    s = s.replace(",", "").replace("$", "").strip()
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def _owner(el: ET.Element) -> Owner:
    rel = el.find("reportingOwnerRelationship")
    return Owner(
        cik=_text(el, "reportingOwnerId/rptOwnerCik"),
        name=_text(el, "reportingOwnerId/rptOwnerName"),
        is_director=_bool(_text(rel, "isDirector")),
        is_officer=_bool(_text(rel, "isOfficer")),
        is_ten_percent=_bool(_text(rel, "isTenPercentOwner")),
        is_other=_bool(_text(rel, "isOther")),
        officer_title=_text(rel, "officerTitle"),
        other_text=_text(rel, "otherText"),
    )


# Footnotes under these describe the resulting holding ("balance includes DRIP
# shares"), not how the reported shares were bought.
_HOLDING_FIELDS = ("postTransactionAmounts", "ownershipNature")


def _trade_footnote_ids(el: ET.Element) -> list[str]:
    ids: list[str] = []
    for child in el:
        if child.tag not in _HOLDING_FIELDS:
            ids.extend(f.get("id", "") for f in child.iter("footnoteId"))
    return list(dict.fromkeys(ids))


def _transaction(el: ET.Element) -> Transaction:
    return Transaction(
        security=_text(el, "securityTitle/value"),
        date=_text(el, "transactionDate/value")[:10],
        code=_text(el, "transactionCoding/transactionCode"),
        shares=_num(_text(el, "transactionAmounts/transactionShares/value")),
        price=_num(_text(el, "transactionAmounts/transactionPricePerShare/value")),
        acquired_disposed=_text(el, "transactionAmounts/transactionAcquiredDisposedCode/value"),
        shares_after=_num(_text(el, "postTransactionAmounts/sharesOwnedFollowingTransaction/value")),
        direct_indirect=_text(el, "ownershipNature/directOrIndirectOwnership/value"),
        nature=_text(el, "ownershipNature/natureOfOwnership/value"),
        footnote_ids=_trade_footnote_ids(el),
    )


def parse_form4_xml(xml: str | bytes, accession: str = "", filed_at: str = "") -> Form4:
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as e:
        raise Form4ParseError(f"invalid XML: {e}") from e
    if root.tag != "ownershipDocument":
        raise Form4ParseError(f"not an ownership document: <{root.tag}>")

    aff = _text(root, "aff10b5One")
    ticker = _text(root, "issuer/issuerTradingSymbol").upper()
    if ticker in ("NONE", "N/A", "NA"):
        ticker = ""
    return Form4(
        accession=accession,
        form_type=_text(root, "documentType"),
        period=_text(root, "periodOfReport"),
        issuer_cik=_text(root, "issuer/issuerCik"),
        issuer_name=_text(root, "issuer/issuerName"),
        ticker=ticker,
        owners=[_owner(o) for o in root.findall("reportingOwner")],
        transactions=[
            _transaction(t) for t in root.findall("nonDerivativeTable/nonDerivativeTransaction")
        ],
        plan_10b5_1=_bool(aff) if aff else None,
        filed_at=filed_at,
        footnotes={
            f.get("id", ""): " ".join((f.text or "").split()) for f in root.findall("footnotes/footnote")
        },
        remarks=_text(root, "remarks"),
    )


_XML_BLOCK_RE = re.compile(r"<XML>\s*(.*?)\s*</XML>", re.S | re.I)
_ACCEPTED_RE = re.compile(r"<ACCEPTANCE-DATETIME>\s*(\d{14})")
_XML_DECL_RE = re.compile(r"^\s*<\?xml[^>]*\?>")


def parse_submission(text: str, accession: str = "") -> Form4:
    """Parse a full EDGAR submission (.txt) that contains a Form 4 XML document."""
    filed_at = ""
    m = _ACCEPTED_RE.search(text)
    if m:
        s = m.group(1)
        filed_at = f"{s[:4]}-{s[4:6]}-{s[6:8]}T{s[8:10]}:{s[10:12]}:{s[12:14]}"
    for block in _XML_BLOCK_RE.findall(text):
        if "<ownershipDocument" in block:
            # The text is already decoded, so drop any encoding declaration.
            block = _XML_DECL_RE.sub("", block, count=1)
            return parse_form4_xml(block, accession=accession, filed_at=filed_at)
    raise Form4ParseError("no ownershipDocument XML in submission")
