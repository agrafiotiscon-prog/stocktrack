---
type: "home"
updated: "2026-10-29"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-10-28 Backtest]]: the latest full backtest
- [[2026-10-29]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 101,022 signals since 2006). That is roughly +3.4% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.9% a year, p 0.006) and has **faded since 2016** (+1.1% a year, p 0.768).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +20.1% a year after costs with a 40% max drawdown, against SPY's +11.1% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.9% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-10-28 | [[TTMI]] | [[Roks Edwin]] | President and CEO | $440K | 62 | – |
| 2026-10-28 | [[TTMI]] | [[Ali Wajid]] | Director | $902K | 61 | – |
| 2026-10-28 | [[BPRE]] | [[KAMFAR RAMIN]] | Director | $2.2M | 55 | – |
| 2026-10-28 | [[GOLD]] | [[Tether Global Investments Fund, S.I.C.A.F., S.A]] | 10% Owner | $3.9M | 48 | – |
| 2026-10-28 | [[HXL]] | [[KEATING NEAL J]] | Director | $242K | 46 | – |
| 2026-10-28 | [[BBT]] | [[Polito Karyn]] | Director | $31K | 49 | – |
| 2026-10-28 | [[WS]] | [[Ganem George John III]] | CEO Americas Kloeckner Metals | $31K | 40 | – |
| 2026-10-28 | [[BBT]] | [[Rosengren Eric S]] | Director | $21K | 44 | – |
| 2026-10-28 | [[HBAN]] | [[ROLLINS JAMES D III]] | Director | $254K | 46 | – |
| 2026-10-28 | [[ACN]] | [[Sweet Julie Spellman]] | Chair and CEO | $3.0M | 78 | – |
| 2026-10-28 | [[ACN]] | [[Price Paula A]] | Director | $200K | 46 | – |
| 2026-10-27 | [[PDI]] | [[Morris Sonya]] | Director | $82K | 41 | -0.4% |
| 2026-10-27 | [[LRN]] | [[Haggart Dylan G]] | Director | $12.2M | 50 | -1.2% |
| 2026-10-27 | [[SRRK]] | [[AKKARAJU SRINIVAS]] | Director | $12.0M | 48 | -1.4% |
| 2026-10-27 | [[LYCA]] | [[Venrock Healthcare Capital Partners III, L.P]] | 10% Owner | $37.7M | 57 | -5.5% |


## Live queries (Dataview plugin)

```dataview
TABLE ticker, insider, role, score, value, abn_now AS "vs SPY so far", status
FROM "Signals"
SORT filed DESC
LIMIT 30
```

```dataview
TABLE verdict, signals, holdout_excess AS "2016+ excess/yr"
FROM "Slices"
SORT holdout_excess DESC
```
