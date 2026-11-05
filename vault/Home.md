---
type: "home"
updated: "2026-11-05"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-04 Backtest]]: the latest full backtest
- [[2026-11-05]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 100,883 signals since 2006). That is roughly +3.4% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.006) and has **faded since 2016** (+0.8% a year, p 0.827).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +19.9% a year after costs with a 40% max drawdown, against SPY's +10.9% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.9% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-04 | [[ASPE]] | [[ORBIMED ADVISORS LLC]] | Director | $15.0M | 80 | – |
| 2026-11-04 | [[PAM]] | [[Zuberbuhler Adolfo Fernando]] | Chief Financial Officer | $207K | 55 | – |
| 2026-11-04 | [[LRN]] | [[Shepherd Brian A]] | Director | $1.7M | 66 | – |
| 2026-11-04 | [[DOLE]] | [[Pale Fire Capital SE]] | 10% Owner | $12.9M | 47 | – |
| 2026-11-04 | [[HGV]] | [[Wang Mark D]] | See Remarks | $499K | 46 | – |
| 2026-11-04 | [[JBLU]] | [[Mittal Nik]] | Director | $324K | 59 | – |
| 2026-11-04 | [[PRLB]] | [[Krishna Suresh]] | President and CEO | $52K | 49 | – |
| 2026-11-04 | [[UPBD]] | [[Khouri Halim]] | EVP, Chief Financial Officer | $251K | 70 | – |
| 2026-11-04 | [[UPBD]] | [[MARINO GLENN P]] | Director | $393K | 73 | – |
| 2026-11-04 | [[UPBD]] | [[Wooters Rebecca]] | EVP, Chief Growth Officer | $99K | 67 | – |
| 2026-11-04 | [[UPBD]] | [[Kumar Balaji]] | EVP, Chief Technology Officer | $50K | 61 | – |
| 2026-11-04 | [[UPBD]] | [[BROWN JEFFREY J]] | Director | $400K | 65 | – |
| 2026-11-04 | [[UPBD]] | [[LANGENSTEIN MOLLY]] | Director | $50K | 64 | – |
| 2026-11-04 | [[AN]] | [[EDMUNDS C COLEMAN]] | EVP, Gen Counsel & Corp Sec | $101K | 48 | – |
| 2026-11-04 | [[AN]] | [[Szlosek Thomas A]] | EVP & CFO | $300K | 65 | – |


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
