---
type: "home"
updated: "2026-11-10"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-04 Backtest]]: the latest full backtest
- [[2026-11-10]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 100,883 signals since 2006). That is roughly +3.4% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.006) and has **faded since 2016** (+0.8% a year, p 0.827).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +19.9% a year after costs with a 40% max drawdown, against SPY's +10.9% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.9% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-10 | [[MX]] | [[LEE CHAE]] | Chief Executive Officer | $155K | 49 | – |
| 2026-11-10 | [[LBTYA]] | [[MALONE JOHN C]] | 10% Owner | $1.5M | 53 | – |
| 2026-11-09 | [[NXRT]] | [[McGraner Matt]] | See Remarks | $199K | 44 | – |
| 2026-11-09 | [[NXRT]] | [[Richards Paul]] | See Remarks | $103K | 49 | – |
| 2026-11-09 | [[KRT]] | [[Guo Jian]] | Chief Financial Officer | $6K | 42 | – |
| 2026-11-09 | [[ADTN]] | [[Santo Timothy P]] | SVP of Finance; CFO | $74K | 58 | – |
| 2026-11-09 | [[ADTN]] | [[STANTON THOMAS R]] | Chairman & CEO | $601K | 65 | – |
| 2026-11-09 | [[ROK]] | [[Moret Blake D]] | President and CEO | $1.5M | 53 | – |
| 2026-11-09 | [[LRN]] | [[Haggart Dylan G]] | Director | $8.1M | 59 | – |
| 2026-11-09 | [[GFS]] | [[LAZAR JACK R]] | Director | $380K | 57 | – |
| 2026-11-09 | [[NATR]] | [[PRESCOTT GROUP CAPITAL MANAGEMENT, L.L.C]] | 10% Owner | $2.8M | 44 | – |
| 2026-11-09 | [[MTDR]] | [[Stetson Glenn W]] | EVP and COO | $51K | 53 | – |
| 2026-11-09 | [[MTDR]] | [[Appel Shelley F]] | Director | $68K | 60 | – |
| 2026-11-09 | [[WCC]] | [[Marino Anthony S]] | EVP & CHRO | $100K | 52 | – |
| 2026-11-09 | [[ADM]] | [[McAtee David R II]] | Director | $197K | 45 | – |


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
