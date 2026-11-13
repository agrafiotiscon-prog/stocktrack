---
type: "home"
updated: "2026-11-13"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-11 Backtest]]: the latest full backtest
- [[2026-11-13]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 100,945 signals since 2006). That is roughly +3.3% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.007) and has **faded since 2016** (+0.8% a year, p 0.830).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +20.0% a year after costs with a 40% max drawdown, against SPY's +10.9% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.8% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-12 | [[ASR]] | [[Perez Anton Jose Antonio]] | Director | $498K | 49 | – |
| 2026-11-12 | [[LRMR]] | [[Hamilton Thomas Edward]] | Director | $187K | 70 | – |
| 2026-11-12 | [[HPP]] | [[BORTZ JON E]] | Director | $680K | 62 | – |
| 2026-11-12 | [[HPP]] | [[COLEMAN VICTOR J]] | Chief Executive Officer | $182K | 62 | – |
| 2026-11-12 | [[VISN]] | [[Watts Claudius E. IV]] | Director | $831K | 42 | – |
| 2026-11-12 | [[EQPT]] | [[Schlacks Jabbok]] | Founder & CEO | $250K | 61 | – |
| 2026-11-12 | [[BKD]] | [[WINKLE C CHRISTIAN]] | Director | $358K | 48 | – |
| 2026-11-12 | [[BLMN]] | [[Spanos Mike]] | CEO | $502K | 55 | – |
| 2026-11-12 | [[MTDR]] | [[Foran Joseph Wm]] | Chairman and CEO | $123K | 75 | – |
| 2026-11-12 | [[LRMR]] | [[BEN-MAIMON CAROLE]] | President and CEO | $50K | 63 | – |
| 2026-11-12 | [[LRMR]] | [[THOMAS FRANK E]] | Director | $22K | 60 | – |
| 2026-11-12 | [[LRMR]] | [[Truitt Joseph]] | Director | $10K | 57 | – |
| 2026-11-12 | [[LRMR]] | [[Harlow John B. Jr]] | President and COO | $50K | 71 | – |
| 2026-11-12 | [[LRMR]] | [[Celano Michael]] | Chief Financial Officer | $50K | 62 | – |
| 2026-11-12 | [[LRMR]] | [[Shankar Gopi]] | Chief Development Officer | $14K | 52 | – |


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
