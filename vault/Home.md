---
type: "home"
updated: "2026-10-28"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-10-28 Backtest]]: the latest full backtest
- [[2026-10-28]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 101,022 signals since 2006). That is roughly +3.4% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.9% a year, p 0.006) and has **faded since 2016** (+1.1% a year, p 0.768).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +20.1% a year after costs with a 40% max drawdown, against SPY's +11.1% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.9% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-10-28 | [[ACN]] | [[Sweet Julie Spellman]] | Chair and CEO | $3.0M | 78 | – |
| 2026-10-28 | [[ACN]] | [[Price Paula A]] | Director | $200K | 46 | – |
| 2026-10-27 | [[PDI]] | [[Morris Sonya]] | Director | $82K | 41 | – |
| 2026-10-27 | [[LRN]] | [[Haggart Dylan G]] | Director | $12.2M | 50 | – |
| 2026-10-27 | [[SRRK]] | [[AKKARAJU SRINIVAS]] | Director | $12.0M | 48 | – |
| 2026-10-27 | [[LYCA]] | [[Venrock Healthcare Capital Partners III, L.P]] | 10% Owner | $37.7M | 57 | – |
| 2026-10-27 | [[AIOK]] | [[Panagiotidis Petros Panagiotis]] | Chief Executive Officer | $1.1M | 51 | – |
| 2026-10-27 | [[MSM]] | [[JACOBSON MITCHELL]] | Director | $29.0M | 63 | – |
| 2026-10-27 | [[STC]] | [[Matz Deborah Jane]] | Director | $44K | 63 | – |
| 2026-10-27 | [[NMCO]] | [[Robert Young L]] | Other | $249K | 50 | – |
| 2026-10-27 | [[STC]] | [[EPPINGER FREDERICK H]] | Chief Executive Officer | $133K | 65 | – |
| 2026-10-27 | [[NPB]] | [[Long Joseph B]] | Chief Operating Officer | $50K | 65 | – |
| 2026-10-27 | [[NPB]] | [[Boer Carrie L]] | Director | $185K | 65 | – |
| 2026-10-27 | [[NPB]] | [[Williams Charles Alan]] | CHAIRMAN & CEO | $1.5M | 73 | – |
| 2026-10-27 | [[KIO]] | [[Takao Justin]] | Treasurer, CAO & CFO | $78K | 51 | – |


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
