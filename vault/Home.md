---
type: "home"
updated: "2026-10-19"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[What Works]]: the scoreboard
- [[2026-10-19 Backtest]]: the latest full backtest
- [[2026-10-19]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI +0.1% to +1.7%, 99,573 signals since 2006). That is roughly +3.4% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.008) and has **faded since 2016** (+1.1% a year, p 0.754).
- The best simulated portfolio (*Exec/director growing stake 25%+ with $100K+*) returned +11.7% a year after costs with a 61% max drawdown, against SPY's +11.1% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.9% to -0.1%; if they did badly, to -13.5%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-10-16 | [[PEP]] | [[POHLAD ROBERT C]] | Director | $23.7M | 62 | +1.7% |
| 2026-10-16 | [[BYRN]] | [[Roth Adam L]] | Director | $70K | 40 | +0.7% |
| 2026-10-16 | [[PAM]] | [[Mindlin Marcos Marcelo]] | Director | $35.1M | 49 | -2.5% |
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | Chief Operating Officer | $1.5M | 72 | -1.5% |
| 2026-10-16 | [[BORR]] | [[Troim Tor Olav]] | Director | $2.3M | 51 | -1.5% |
| 2026-10-15 | [[BPRE]] | [[Ruddy Jordan B]] | President | $44K | 63 | -1.5% |
| 2026-10-15 | [[IMSR]] | [[Pardee Charles G]] | Director | $22K | 55 | -10.4% |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | Chief Executive Officer | $3.0M | 70 | -0.9% |
| 2026-10-15 | [[TRXB]] | [[Alexandria Venture Investments, LLC]] | 10% Owner | $2.5M | 55 | +3.1% |
| 2026-10-15 | [[CXM]] | [[WARD JR STEPHEN M]] | Director | $850K | 51 | +0.1% |
| 2026-10-15 | [[GOLD]] | [[Tether Global Investments Fund, S.I.C.A.F., S.A]] | 10% Owner | $2.7M | 45 | -2.4% |
| 2026-10-15 | [[BORR]] | [[Troim Tor Olav]] | Director | $3.5M | 41 | -8.1% |
| 2026-10-14 | [[INBX]] | [[Lappe Mark]] | Chief Executive Officer | $849K | 47 | +2.0% |
| 2026-10-14 | [[BPRE]] | [[KAMFAR RAMIN]] | Director | $5.5M | 73 | -2.7% |
| 2026-10-14 | [[QVCG]] | [[GOLDENTREE ASSET MANAGEMENT LP]] | 10% Owner | $16.7M | 48 | -15.1% |


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
