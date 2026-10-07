"""Render a self-contained HTML dashboard of ranked insider buys and clusters."""

from __future__ import annotations

import datetime as dt
import math
from html import escape

from stocktrack.prices import MISMATCH_NOTE
from stocktrack.signals import NOTABLE, STRONG, money, qty, stake_text
from stocktrack.tracker import Cluster, Signal


def _row(sig: Signal, with_prices: bool) -> str:
    b, s = sig.buy, sig.score
    inc = b.stake_increase
    stake_txt = stake_text(inc)
    stake_sort = -1.0 if inc is None else (1e9 if math.isinf(inc) else inc)
    # The stake change has its own column.
    tags = "".join(
        f'<span class="tag">{escape(t)}</span>'
        for t in s.tags
        if not (t.startswith("Stake ") or t == "New position")
    )
    breakdown = (
        f"value {s.value_pts:.0f} + role {s.role_pts:.0f} + conviction {s.conviction_pts:.0f}"
        f" + cluster {s.cluster_pts:.0f}" + (f" - penalties {s.penalty:.0f}" if s.penalty else "")
    )
    price_cells = ""
    if with_prices:
        q = sig.quote
        chg = q.change_from(b.avg_price) if q else None
        cls = "" if chg is None else ("up" if chg >= 0 else "down")
        if chg is not None:
            vs = f"{chg:+.1%}"
        elif q and b.avg_price:
            vs = f'<span title="{escape(MISMATCH_NOTE)}">?</span>'
        else:
            vs = "–"
        price_cells = (
            f'<td class="num" data-v="{q.price if q else -1}">{f"${q.price:,.2f}" if q else "–"}</td>'
            f'<td class="num {cls}" data-v="{chg if chg is not None else -99}">{vs}</td>'
        )
    who = escape(b.owner_name)
    if b.owner_names and b.owner_names != b.owner_name:
        who = f"{who} +"
    role = escape(b.officer_title or b.role)
    return f"""<tr data-search="{escape((b.ticker + ' ' + b.issuer_name + ' ' + b.owner_names).lower())}">
<td data-v="{s.total}"><span class="score {s.label.lower()}" title="{escape(breakdown)}">{s.total}</span></td>
<td data-v="{escape(b.ticker)}"><b>{escape(b.ticker) or "–"}</b>
<div class="sub" title="{escape(b.issuer_name)}">{escape(b.issuer_name)}</div></td>
<td data-v="{escape(b.owner_name)}"><div class="clip" title="{escape(b.owner_names)}">{who}</div>
<div class="sub" title="{role}">{role}</div></td>
<td data-v="{b.last_date}">{b.last_date}</td>
<td class="num" data-v="{b.shares}">{qty(b.shares)}</td>
<td class="num" data-v="{b.avg_price or 0}">{f"${b.avg_price:,.2f}" if b.avg_price else "–"}</td>
<td class="num" data-v="{b.value}">{money(b.value) if b.value else "–"}</td>
<td class="num" data-v="{stake_sort}">{stake_txt or "–"}</td>
{price_cells}
<td>{tags}</td>
<td><a href="{escape(b.url)}" target="_blank" rel="noopener">Form 4</a></td>
</tr>"""


def _cluster_card(c: Cluster) -> str:
    people = "".join(
        f"<li><span>{escape(b.owner_name)}</span><span class='muted'>{escape(b.officer_title or b.role)}</span>"
        f"<span class='num'>{money(b.value) if b.value else '–'}</span></li>"
        for b in c.insiders
    )
    return f"""<div class="card">
<div class="card-head"><b>{escape(c.ticker) or "–"}</b><span class="pill">{len(c.insiders)} insiders</span></div>
<div class="co">{escape(c.issuer_name)}</div>
<div class="muted small">{money(c.total_value)} bought, {c.first_date} to {c.last_date}</div>
<ul>{people}</ul>
</div>"""


def render_report(
    signals: list[Signal],
    clusters: list[Cluster],
    since: str,
    until: str,
    with_prices: bool = False,
) -> str:
    strong = sum(1 for s in signals if s.score.label == "Strong")
    total = sum(s.buy.value for s in signals)
    generated = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    rows = "\n".join(_row(s, with_prices) for s in signals)
    cards = "\n".join(_cluster_card(c) for c in clusters[:12])
    price_heads = '<th data-t="n">Now</th><th data-t="n">vs paid</th>' if with_prices else ""
    empty = "" if signals else '<p class="muted">No insider buys in this period yet. Run a scan or backfill first.</p>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Insider Buys</title>
<style>
:root {{
  --bg: #f7f7f5; --panel: #ffffff; --ink: #1d1d1b; --muted: #6b6b66; --line: #e4e4df;
  --strong: #1f7a4d; --strong-bg: #e3f3ea; --notable: #8a5a00; --notable-bg: #fbf0d9;
  --minor: #5b5b57; --minor-bg: #eeeeea; --up: #1f7a4d; --down: #b3261e; --accent: #2d5bd7;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --bg: #141413; --panel: #1d1d1b; --ink: #ecece8; --muted: #a0a09a; --line: #2f2f2c;
    --strong: #6fd09d; --strong-bg: #173527; --notable: #f0c060; --notable-bg: #3a2e14;
    --minor: #b5b5ae; --minor-bg: #2a2a27; --up: #6fd09d; --down: #f28b82; --accent: #8fb0ff;
  }}
}}
:root[data-theme="dark"] {{
  --bg: #141413; --panel: #1d1d1b; --ink: #ecece8; --muted: #a0a09a; --line: #2f2f2c;
  --strong: #6fd09d; --strong-bg: #173527; --notable: #f0c060; --notable-bg: #3a2e14;
  --minor: #b5b5ae; --minor-bg: #2a2a27; --up: #6fd09d; --down: #f28b82; --accent: #8fb0ff;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--ink);
  font: 14px/1.45 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }}
main {{ max-width: 1280px; margin: 0 auto; padding: 24px 16px 48px; }}
h1 {{ font-size: 22px; margin: 0 0 4px; }}
h2 {{ font-size: 16px; margin: 32px 0 12px; }}
a {{ color: var(--accent); }}
.muted {{ color: var(--muted); }} .small {{ font-size: 12px; }}
.kpis {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin-top: 20px; }}
.kpi {{ background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 12px 14px; }}
.kpi b {{ display: block; font-size: 22px; font-variant-numeric: tabular-nums; }}
.cards {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px; }}
.card {{ background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 12px 14px; }}
.card-head {{ display: flex; justify-content: space-between; align-items: center; font-size: 16px; }}
.card ul {{ list-style: none; padding: 0; margin: 8px 0 0; }}
.card li {{ display: grid; grid-template-columns: 1fr auto auto; gap: 8px; padding: 3px 0;
  border-top: 1px solid var(--line); font-size: 13px; }}
.pill {{ font-size: 12px; background: var(--strong-bg); color: var(--strong); border-radius: 99px; padding: 1px 8px; }}
.controls {{ display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 10px; }}
input, select {{ font: inherit; color: var(--ink); background: var(--panel); border: 1px solid var(--line);
  border-radius: 8px; padding: 6px 10px; }}
input {{ flex: 1; min-width: 180px; }}
.table-wrap {{ overflow-x: auto; background: var(--panel); border: 1px solid var(--line); border-radius: 10px; }}
table {{ border-collapse: collapse; width: 100%; white-space: nowrap; }}
th, td {{ padding: 8px 10px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }}
th {{ font-size: 12px; color: var(--muted); font-weight: 600; cursor: pointer; user-select: none;
  position: sticky; top: 0; background: var(--panel); }}
tr:last-child td {{ border-bottom: 0; }}
.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
.co, .clip, .sub {{ max-width: 230px; overflow: hidden; text-overflow: ellipsis; }}
.sub {{ font-size: 12px; color: var(--muted); }}
.up {{ color: var(--up); }} .down {{ color: var(--down); }}
.score {{ display: inline-block; min-width: 34px; text-align: center; font-weight: 700; border-radius: 6px;
  padding: 1px 6px; font-variant-numeric: tabular-nums; }}
.score.strong {{ color: var(--strong); background: var(--strong-bg); }}
.score.notable {{ color: var(--notable); background: var(--notable-bg); }}
.score.minor {{ color: var(--minor); background: var(--minor-bg); }}
.tag {{ display: inline-block; font-size: 12px; border: 1px solid var(--line); border-radius: 99px;
  padding: 0 7px; margin: 0 4px 2px 0; color: var(--muted); }}
footer {{ margin-top: 32px; font-size: 12px; color: var(--muted); max-width: 820px; }}
</style>
</head>
<body>
<main>
<h1>Insider Buys</h1>
<div class="muted">Open-market purchases from SEC Form 4 filings, trades {since} to {until}. Generated {generated}.</div>

<div class="kpis">
<div class="kpi"><span class="muted small">Insider buys</span><b>{len(signals)}</b></div>
<div class="kpi"><span class="muted small">Total bought</span><b>{money(total)}</b></div>
<div class="kpi"><span class="muted small">Strong signals ({STRONG}+)</span><b>{strong}</b></div>
<div class="kpi"><span class="muted small">Cluster buys</span><b>{len(clusters)}</b></div>
</div>

{f'<h2>Cluster buys</h2><div class="cards">{cards}</div>' if clusters else ""}

<h2>Ranked buys</h2>
<div class="controls">
<input id="q" type="search" placeholder="Filter ticker, company, insider">
<select id="min"><option value="0">All scores</option><option value="{NOTABLE}">{NOTABLE}+ (notable)</option>
<option value="{STRONG}">{STRONG}+ (strong)</option></select>
</div>
{empty}
<div class="table-wrap">
<table id="t">
<thead><tr>
<th data-t="n">Score</th><th>Stock</th><th>Insider</th><th>Traded</th>
<th data-t="n">Shares</th><th data-t="n">Avg price</th><th data-t="n">Value</th><th data-t="n">Stake</th>
{price_heads}<th>Signals</th><th>Filing</th>
</tr></thead>
<tbody>
{rows}
</tbody>
</table>
</div>

<footer>
<p><b>How the score works (0-100).</b> Value up to 30 (log scale: $100K = 10, $1M = 20, $10M = 30).
Role up to 25 (CEO highest, then CFO/President/Chair, other executives, directors, 10% holders).
Conviction up to 20 (how much the purchase grew the insider's holding; a new position scores full).
Cluster up to 25 (2, 3 or 4+ different insiders each buying $25K+ within 14 days). Minus 30 for automatic
plan purchases (dividend reinvestment, stock purchase plans), 15 for purchases under a pre-arranged
Rule 10b5-1 plan, and 10 for filings made more than 10 days after the trade.
Hover a score to see its breakdown.</p>
<p>Data: SEC EDGAR. Insider purchases are public disclosures, not recommendations. This is not investment advice.</p>
</footer>
</main>
<script>
(function () {{
  const t = document.getElementById("t"), q = document.getElementById("q"), min = document.getElementById("min");
  const body = t.tBodies[0];
  function filter() {{
    const s = q.value.trim().toLowerCase(), m = +min.value;
    for (const r of body.rows) {{
      const score = +r.cells[0].dataset.v;
      r.hidden = (s && !r.dataset.search.includes(s)) || score < m;
    }}
  }}
  q.addEventListener("input", filter); min.addEventListener("change", filter);
  t.tHead.addEventListener("click", (e) => {{
    const th = e.target.closest("th"); if (!th) return;
    const i = th.cellIndex, numeric = th.dataset.t === "n";
    const dir = th.dataset.dir === "desc" ? 1 : -1;
    for (const h of t.tHead.rows[0].cells) delete h.dataset.dir;
    th.dataset.dir = dir === 1 ? "asc" : "desc";
    const val = (r) => {{ const c = r.cells[i]; return c.dataset.v ?? c.textContent.trim(); }};
    [...body.rows].sort((a, b) => {{
      const x = val(a), y = val(b);
      return dir * (numeric ? (+x - +y) : String(x).localeCompare(String(y)));
    }}).forEach((r) => body.appendChild(r));
  }});
}})();
</script>
</body>
</html>
"""
