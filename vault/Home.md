---
type: "home"
updated: "2026-11-19"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-18 Backtest]]: the latest full backtest
- [[2026-11-19]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 101,092 signals since 2006). That is roughly +3.3% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.007) and has **faded since 2016** (+0.8% a year, p 0.815).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +19.6% a year after costs with a 40% max drawdown, against SPY's +10.8% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.8% to -0.1%; if they did badly, to -12.7%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-18 | [[USAR]] | [[BLITZER MICHAEL]] | Director | $3.0M | 51 | – |
| 2026-11-18 | [[RMIX]] | [[Johnston Bretton A]] | Director | $12K | 58 | – |
| 2026-11-18 | [[RMIX]] | [[Rees-Jones David]] | Director | $731K | 76 | – |
| 2026-11-18 | [[EQPT]] | [[Schlacks William J]] | Founder & President | $145K | 64 | – |
| 2026-11-18 | [[EQPT]] | [[Schlacks Jabbok]] | Founder & CEO / | $250K | 69 | – |
| 2026-11-18 | [[OIG]] | [[DEUTSCH ROBERT V]] | Director | $106K | 54 | – |
| 2026-11-18 | [[RMIX]] | [[Matteson Mark R]] | Director | $55K | 64 | – |
| 2026-11-18 | [[RMIX]] | [[Jones Mark Alan]] | Chief Operating Officer | $50K | 53 | – |
| 2026-11-18 | [[BPRE]] | [[KAMFAR RAMIN]] | Director | $3.2M | 45 | – |
| 2026-11-18 | [[ANAB]] | [[EcoR1 Capital, LLC]] | Director | $17.2M | 48 | – |
| 2026-11-18 | [[BH]] | [[BIGLARI, SARDAR]] | Chairman and CEO | $2.2M | 50 | – |
| 2026-11-18 | [[ECC]] | [[Majewski Thomas P]] | Chief Executive Officer | $118K | 68 | – |
| 2026-11-18 | [[BA]] | [[JOHRI AKHIL]] | Director | $500K | 49 | – |
| 2026-11-18 | [[FPS]] | [[Lund Inez]] | Chief Accounting Officer | $65K | 70 | – |
| 2026-11-18 | [[KGS]] | [[HOGAN RANDALL J]] | Director | $494K | 71 | – |


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
