---
type: "home"
updated: "2026-11-07"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-04 Backtest]]: the latest full backtest
- [[2026-11-07]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 100,883 signals since 2006). That is roughly +3.4% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.006) and has **faded since 2016** (+0.8% a year, p 0.827).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +19.9% a year after costs with a 40% max drawdown, against SPY's +10.9% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.9% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-06 | [[KMI]] | [[KINDER RICHARD D]] | Executive Chairman | $15.0M | 53 | – |
| 2026-11-06 | [[GFS]] | [[MOORTHY GANESH]] | Director | $94K | 42 | – |
| 2026-11-06 | [[MDGL]] | [[BAKER BROS. ADVISORS LP]] | Director | $35.0M | 48 | – |
| 2026-11-06 | [[KOD]] | [[BAKER BROS. ADVISORS LP]] | Director | $24.3M | 45 | – |
| 2026-11-06 | [[CVS]] | [[Shah Prem S]] | EVP and Group President | $2.0M | 54 | – |
| 2026-11-06 | [[TRNS]] | [[IRICK JAIME A]] | President and CEO | $230K | 59 | – |
| 2026-11-06 | [[KYN]] | [[Little Harrison James]] | Executive Vice President | $52K | 45 | – |
| 2026-11-06 | [[KYN]] | [[Baker James C]] | President | $331K | 54 | – |
| 2026-11-06 | [[KMT]] | [[Chowbey Sanjay]] | President and CEO | $165K | 42 | – |
| 2026-11-06 | [[LKQ]] | [[GOVE SUE]] | Director | $201K | 65 | – |
| 2026-11-06 | [[PMN]] | [[Williams Eugene]] | Director | $91K | 54 | – |
| 2026-11-06 | [[MTDR]] | [[Elsener William Thomas]] | EVP, Reservoir Engineering | $46K | 48 | – |
| 2026-11-06 | [[MTDR]] | [[Erman Bryan A]] | President | $46K | 67 | – |
| 2026-11-06 | [[AGMB]] | [[Epstein David R]] | Director | $104K | 42 | – |
| 2026-11-05 | [[FLOC]] | [[Fairbanks Jonathan B]] | Director | $293K | 47 | +3.4% |


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
