---
type: "strategy"
key: "cluster_3"
signals: 8062
cagr: 0.0748308
spy_cagr: 0.110804
sharpe: 0.339857
max_drawdown: 0.568051
holdout_excess: 0.00704047
---

# 3+ insiders buying within 14 days

Rule key: `cluster_3`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 8,062 |
| 3-month excess vs SPY (mean / median) | +1.9% / -0.1% |
| Beat SPY over 3 months | 50% |
| Entering one session later | +1.8% |
| vs surviving stocks | +0.9% |
| 2006-2015 excess /yr | +9.0% (p 0.021) |
| 2016+ excess /yr | +0.7% (p 0.892) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Years beating SPY | Trades | Costs/yr |
|---|---|---|---|---|---|---|---|---|---|
| 21d | +5.9% | +11.1% | 0.29 | 0.56 | 55% | 0.83 | 38% | 2,930 | 6.0% |
| 63d | +7.5% | +11.1% | 0.34 | 0.56 | 57% | 1.10 | 38% | 1,539 | 3.0% |
| 126d | +10.4% | +11.1% | 0.43 | 0.56 | 65% | 1.11 | 38% | 820 | 1.8% |


Cost sensitivity (63-session hold): no costs +10.7%/yr, double costs +4.5%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.6% | +13.3% | +3.3% |
| 2007 | -6.5% | +5.1% | -11.6% |
| 2008 | -25.9% | -36.8% | +10.9% |
| 2009 | +45.8% | +26.4% | +19.4% |
| 2010 | +38.9% | +15.1% | +23.8% |
| 2011 | +0.1% | +1.9% | -1.8% |
| 2012 | +34.2% | +16.0% | +18.2% |
| 2013 | +33.0% | +32.3% | +0.7% |
| 2014 | +1.2% | +13.5% | -12.2% |
| 2015 | -18.5% | +1.2% | -19.7% |
| 2016 | +16.3% | +12.0% | +4.3% |
| 2017 | +14.8% | +21.7% | -6.9% |
| 2018 | -13.5% | -4.6% | -9.0% |
| 2019 | +26.7% | +31.2% | -4.5% |
| 2020 | +52.1% | +18.3% | +33.8% |
| 2021 | +2.6% | +28.7% | -26.1% |
| 2022 | -32.9% | -18.2% | -14.7% |
| 2023 | +11.5% | +26.2% | -14.6% |
| 2024 | +0.3% | +24.9% | -24.6% |
| 2025 | +4.1% | +17.7% | -13.6% |
| 2026 | +3.4% | +13.4% | -9.9% |


## Live forward test

0 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-15 | [[BPRE]] | [[MacDonald Ryan S]] | $2K | 34 | -1.5% | open |
| 2026-10-15 | [[BPRE]] | [[Ruddy Jordan B]] | $44K | 63 | -1.5% | open |
| 2026-10-15 | [[IMSR]] | [[Pardee Charles G]] | $22K | 55 | -10.4% | open |
| 2026-10-14 | [[BPRE]] | [[KAMFAR RAMIN]] | $5.5M | 73 | -2.7% | open |
| 2026-10-09 | [[BPRE]] | [[KAMFAR RAMIN]] | $8.5M | 81 | -5.1% | open |
| 2026-10-08 | [[PDI]] | [[FLATTUM DAVID C]] | $250K | 66 | +0.9% | open |
| 2026-10-08 | [[FUL]] | [[BAILLY R JEFFREY]] | $500K | 74 | +3.4% | open |
| 2026-10-05 | [[BPRE]] | [[KAMFAR RAMIN]] | $3.4M | 73 | -2.0% | open |
| 2026-10-05 | [[BPRE]] | [[MacDonald Ryan S]] | $85K | 54 | -2.0% | open |
| 2026-10-02 | [[GME]] | [[Cohen Ryan]] | $17.1M | 79 | +5.9% | open |
| 2026-10-01 | [[GME]] | [[Turner Nat]] | $255K | 66 | +9.4% | open |
| 2026-10-01 | [[DKS]] | [[Barnes Matthew]] | $500K | 78 | +6.8% | open |
| 2026-10-01 | [[FUL]] | [[Happe Michael J]] | $99K | 67 | +0.6% | open |
| 2026-10-01 | [[FUL]] | [[Martin Celine Christine]] | $23K | 61 | +0.6% | open |
| 2026-09-30 | [[ADRX]] | [[OrbiMed Genesis GP LLC]] | $16.1M | 82 | -11.9% | open |
| 2026-09-30 | [[ADRX]] | [[Chimovits Erez]] | $1.0M | 55 | -11.9% | open |
| 2026-09-30 | [[KOD]] | [[Baker Bros. Advisors (GP) LLC]] | $58.6M | 68 | -5.4% | open |
| 2026-09-30 | [[KOD]] | [[BAKER JULIAN]] | $35.0M | 66 | -5.4% | open |
| 2026-09-30 | [[KOD]] | [[667, L.P]] | $63.4M | 82 | -5.4% | open |
| 2026-09-30 | [[FUL]] | [[Zaheer Srilata]] | $100K | 67 | +3.6% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "cluster_3")
SORT filed DESC
```

Back to [[What Works]].
