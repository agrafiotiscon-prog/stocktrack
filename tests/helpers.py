"""Builders for synthetic EDGAR documents used across tests."""

from __future__ import annotations


def owner_xml(
    cik: str = "0001111111",
    name: str = "Doe Jane",
    director: bool = False,
    officer: bool = False,
    ten_percent: bool = False,
    title: str = "",
    other_text: str = "",
) -> str:
    return f"""
    <reportingOwner>
        <reportingOwnerId><rptOwnerCik>{cik}</rptOwnerCik><rptOwnerName>{name}</rptOwnerName></reportingOwnerId>
        <reportingOwnerRelationship>
            <isDirector>{int(director)}</isDirector>
            <isOfficer>{int(officer)}</isOfficer>
            <isTenPercentOwner>{int(ten_percent)}</isTenPercentOwner>
            <isOther>0</isOther>
            {f"<officerTitle>{title}</officerTitle>" if title else ""}
            {f"<otherText>{other_text}</otherText>" if other_text else ""}
        </reportingOwnerRelationship>
    </reportingOwner>"""


def tx_xml(
    date: str = "2026-10-01",
    code: str = "P",
    shares: float | str = 1000,
    price: float | str | None = 10.0,
    ad: str = "A",
    after: float | str | None = 11000,
    di: str = "D",
    nature: str = "",
) -> str:
    price_el = f"<value>{price}</value>" if price is not None else '<footnoteId id="F1"/>'
    after_el = (
        f"<postTransactionAmounts><sharesOwnedFollowingTransaction><value>{after}</value>"
        f"</sharesOwnedFollowingTransaction></postTransactionAmounts>"
        if after is not None
        else ""
    )
    nature_el = f"<natureOfOwnership><value>{nature}</value></natureOfOwnership>" if nature else ""
    return f"""
        <nonDerivativeTransaction>
            <securityTitle><value>Common Stock</value></securityTitle>
            <transactionDate><value>{date}</value></transactionDate>
            <transactionCoding>
                <transactionFormType>4</transactionFormType>
                <transactionCode>{code}</transactionCode>
                <equitySwapInvolved>0</equitySwapInvolved>
            </transactionCoding>
            <transactionAmounts>
                <transactionShares><value>{shares}</value></transactionShares>
                <transactionPricePerShare>{price_el}</transactionPricePerShare>
                <transactionAcquiredDisposedCode><value>{ad}</value></transactionAcquiredDisposedCode>
            </transactionAmounts>
            {after_el}
            <ownershipNature>
                <directOrIndirectOwnership><value>{di}</value></directOrIndirectOwnership>
                {nature_el}
            </ownershipNature>
        </nonDerivativeTransaction>"""


def form4_xml(
    owners: list[str] | None = None,
    txs: list[str] | None = None,
    issuer_cik: str = "0000320193",
    issuer_name: str = "Acme Corp",
    ticker: str = "ACME",
    aff10b5one: str | None = "0",
    doc_type: str = "4",
) -> str:
    owners = owners if owners is not None else [owner_xml(officer=True, title="Chief Executive Officer")]
    txs = txs if txs is not None else [tx_xml()]
    aff = f"<aff10b5One>{aff10b5one}</aff10b5One>" if aff10b5one is not None else ""
    return f"""<?xml version="1.0"?>
<ownershipDocument>
    <schemaVersion>X0609</schemaVersion>
    <documentType>{doc_type}</documentType>
    <periodOfReport>2026-10-01</periodOfReport>
    <issuer>
        <issuerCik>{issuer_cik}</issuerCik>
        <issuerName>{issuer_name}</issuerName>
        <issuerTradingSymbol>{ticker}</issuerTradingSymbol>
    </issuer>
    {"".join(owners)}
    {aff}
    <nonDerivativeTable>{"".join(txs)}</nonDerivativeTable>
    <footnotes><footnote id="F1">Weighted average price.</footnote></footnotes>
    <remarks>Test filing</remarks>
</ownershipDocument>"""


def submission(xml: str, accession: str = "0000000000-26-000001", accepted: str = "20261002163000") -> str:
    return f"""<SEC-DOCUMENT>{accession}.txt : 20261002
<SEC-HEADER>{accession}.hdr.sgml : 20261002
<ACCEPTANCE-DATETIME>{accepted}
ACCESSION NUMBER:		{accession}
CONFORMED SUBMISSION TYPE:	4
</SEC-HEADER>
<DOCUMENT>
<TYPE>4
<SEQUENCE>1
<FILENAME>form4.xml
<TEXT>
<XML>
{xml}
</XML>
</TEXT>
</DOCUMENT>
</SEC-DOCUMENT>
"""


def atom_feed(entries: list[tuple[str, str, str, str]]) -> str:
    """entries: (form_type, accession, cik, role) e.g. ("4", "0000000000-26-000001", "320193", "Issuer")."""
    body = "".join(
        f"""<entry>
<title>{form} - Someone ({cik}) ({role})</title>
<link rel="alternate" type="text/html"
  href="https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{acc}-index.htm"/>
<summary type="html"> &lt;b&gt;Filed:&lt;/b&gt; 2026-10-07 &lt;b&gt;AccNo:&lt;/b&gt; {acc}</summary>
<updated>2026-10-07T06:10:14-04:00</updated>
<category scheme="https://www.sec.gov/" label="form type" term="{form}"/>
<id>urn:tag:sec.gov,2008:accession-number={acc}</id>
</entry>"""
        for form, acc, cik, role in entries
    )
    return f"""<?xml version="1.0" encoding="ISO-8859-1" ?>
<feed xmlns="http://www.w3.org/2005/Atom">
<title>Latest Filings</title>
<updated>2026-10-07T07:14:20-04:00</updated>
{body}
</feed>"""
