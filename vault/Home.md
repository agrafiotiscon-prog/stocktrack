---
type: "home"
updated: "2026-11-06"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-04 Backtest]]: the latest full backtest
- [[2026-11-06]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 100,883 signals since 2006). That is roughly +3.4% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.006) and has **faded since 2016** (+0.8% a year, p 0.827).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +19.9% a year after costs with a 40% max drawdown, against SPY's +10.9% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.9% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-06 | [[AGMB]] | [[Epstein David R]] | Director | $104K | 42 | – |
| 2026-11-05 | [[FLOC]] | [[Fairbanks Jonathan B]] | Director | $293K | 47 | – |
| 2026-11-05 | [[MTDR]] | [[Colodney Benjamin T]] | SVP & Chief Accounting Officer | $26K | 40 | – |
| 2026-11-05 | [[MTDR]] | [[Calvert Christopher P]] | EVP and CFO | $105K | 50 | – |
| 2026-11-05 | [[BXMT]] | [[NASSAU HENRY N]] | Director | $114K | 41 | – |
| 2026-11-05 | [[BXMT]] | [[Johnson Timothy Steven]] | Chief Executive Officer | $1.0M | 69 | – |
| 2026-11-05 | [[ETRA]] | [[ORBIMED ADVISORS LLC]] | Director | $3.6M | 53 | – |
| 2026-11-05 | [[LYEL]] | [[ARCH Venture Fund XIII, L.P]] | 10% Owner | $25.0M | 58 | – |
| 2026-11-05 | [[COUR]] | [[Pale Fire Capital SE]] | 10% Owner | $31.5M | 53 | – |
| 2026-11-05 | [[LBRT]] | [[Gosney Ryan T]] | Chief Accounting Officer | $45K | 48 | – |
| 2026-11-05 | [[LBRT]] | [[Gusek Ron]] | CEO and President | $377K | 65 | – |
| 2026-11-05 | [[GLXY]] | [[Novogratz Michael]] | Chief Executive Officer | $9.9M | 75 | – |
| 2026-11-05 | [[FBRT]] | [[Byrne Richard J]] | Chairman and CEO | $998K | 65 | – |
| 2026-11-05 | [[UPBD]] | [[Karam Fahmi]] | Chief Executive Officer | $100K | 64 | – |
| 2026-11-05 | [[SYY]] | [[Ondrof Thomas Gerard]] | Director | $192K | 45 | – |


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
