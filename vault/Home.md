---
type: "home"
updated: "2026-11-03"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-10-28 Backtest]]: the latest full backtest
- [[2026-11-03]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 101,022 signals since 2006). That is roughly +3.4% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.9% a year, p 0.006) and has **faded since 2016** (+1.1% a year, p 0.768).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +20.1% a year after costs with a 40% max drawdown, against SPY's +11.1% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.9% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-02 | [[ASPE]] | [[ARCH Venture Fund X, L.P]] | 10% Owner | $20.0M | 70 | – |
| 2026-11-02 | [[ASPE]] | [[ARCH Venture Partners XIV, L.P]] | 10% Owner | $18.0M | 70 | – |
| 2026-11-02 | [[RSI]] | [[Winter Thomas]] | Director | $118K | 42 | – |
| 2026-11-02 | [[ROL]] | [[LOR INC]] | 10% Owner | $50.0M | 41 | – |
| 2026-11-02 | [[JBLU]] | [[BONEPARTH PETER]] | Director | $300K | 47 | – |
| 2026-11-02 | [[FCPT]] | [[Lenehan William H]] | President and CEO | $226K | 42 | – |
| 2026-11-02 | [[ENPH]] | [[Kothandaraman Badrinarayanan]] | President & CEO | $268K | 41 | – |
| 2026-11-02 | [[SEVN]] | [[Lorenzini Thomas J]] | President and CIO | $33K | 48 | – |
| 2026-11-02 | [[SEVN]] | [[Jordan Matthew P]] | Director | $66K | 40 | – |
| 2026-11-02 | [[BBTX]] | [[Jeggle Helmut Wolfgang]] | Director | $6.0M | 46 | – |
| 2026-11-02 | [[BBT]] | [[Hughes William H III]] | Director | $6K | 40 | – |
| 2026-11-02 | [[OCFC]] | [[Katsoulis Nicos]] | Director | $178K | 53 | – |
| 2026-11-02 | [[LSTR]] | [[Lonegro Frank A]] | President & CEO | $715K | 57 | – |
| 2026-10-30 | [[RAPP]] | [[HEALY JAMES]] | Director | $20.4M | 87 | +0.8% |
| 2026-10-30 | [[FFIN]] | [[Denny Michael B]] | Director | $100K | 42 | +2.7% |


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
