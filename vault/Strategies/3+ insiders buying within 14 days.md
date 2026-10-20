---
type: "strategy"
key: "cluster_3"
signals: 7458
cagr: 0.0601742
spy_cagr: 0.110437
sharpe: 0.288989
max_drawdown: 0.591046
holdout_excess: 0.00737948
---

# 3+ insiders buying within 14 days

Rule key: `cluster_3`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,458 |
| 3-month excess vs SPY (mean / median) | +2.1% / +0.1% |
| Beat SPY over 3 months | 50% |
| Entering one session later | +2.0% |
| vs surviving stocks | +0.9% |
| 2006-2015 excess /yr | +8.7% (p 0.030) |
| 2016+ excess /yr | +0.7% (p 0.888) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +5.9% | +11.0% | 0.30 | 0.55 | 52% | 0.75 | -1.7% | 24% | 2,846 | 5.9% | +1.4% / 0.03 / 36% |
| 63d | +6.0% | +11.0% | 0.29 | 0.55 | 59% | 1.13 | -4.4% | 33% | 1,539 | 3.0% | -1.1% / -0.12 / 55% |
| 126d | +10.4% | +11.0% | 0.44 | 0.55 | 67% | 1.14 | -0.3% | 48% | 820 | 1.7% | +2.5% / 0.13 / 46% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +9.3%/yr, double costs +3.1%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +17.4% | +13.3% | +4.1% |
| 2007 | -8.0% | +5.1% | -13.2% |
| 2008 | -27.5% | -36.8% | +9.3% |
| 2009 | +27.1% | +26.4% | +0.7% |
| 2010 | +30.0% | +15.1% | +15.0% |
| 2011 | -2.6% | +1.9% | -4.5% |
| 2012 | +32.5% | +16.0% | +16.5% |
| 2013 | +30.5% | +32.3% | -1.8% |
| 2014 | +2.4% | +13.5% | -11.1% |
| 2015 | -9.7% | +1.2% | -10.9% |
| 2016 | +24.1% | +12.0% | +12.1% |
| 2017 | +17.8% | +21.7% | -3.9% |
| 2018 | -14.5% | -4.6% | -10.0% |
| 2019 | +18.3% | +31.2% | -12.9% |
| 2020 | +35.0% | +18.3% | +16.7% |
| 2021 | +10.1% | +28.7% | -18.6% |
| 2022 | -35.3% | -18.2% | -17.1% |
| 2023 | +16.7% | +26.2% | -9.5% |
| 2024 | +0.5% | +24.9% | -24.4% |
| 2025 | +3.3% | +17.7% | -14.5% |
| 2026 | -3.1% | +13.3% | -16.4% |


## Live forward test

0 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-19 | [[BPRE]] | [[KAMFAR RAMIN]] | $2.4M | 64 | – | pending |
| 2026-10-15 | [[BPRE]] | [[MacDonald Ryan S]] | $2K | 34 | -1.5% | open |
| 2026-10-15 | [[BPRE]] | [[Ruddy Jordan B]] | $44K | 63 | -1.5% | open |
| 2026-10-15 | [[IMSR]] | [[Pardee Charles G]] | $22K | 55 | -11.2% | open |
| 2026-10-14 | [[BPRE]] | [[KAMFAR RAMIN]] | $5.5M | 73 | -2.7% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[CULLIGAN THOMAS M]] | $175K | 57 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[Hildebrandt Mark H]] | $175K | 53 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[Fine Carol F]] | $175K | 69 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[SCHRIESHEIM ALAN]] | $175K | 69 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[HENRIQUES ADOLFO]] | $175K | 55 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[CHERUVATATH NANDAKUMAR]] | $175K | 62 | +4.8% | open |
| 2026-10-09 | [[BPRE]] | [[KAMFAR RAMIN]] | $8.5M | 81 | -5.1% | open |
| 2026-10-08 | [[PDI]] | [[FLATTUM DAVID C]] | $250K | 66 | +1.2% | open |
| 2026-10-08 | [[FUL]] | [[BAILLY R JEFFREY]] | $500K | 74 | +3.4% | open |
| 2026-10-05 | [[BPRE]] | [[KAMFAR RAMIN]] | $3.4M | 73 | -2.0% | open |
| 2026-10-05 | [[BPRE]] | [[MacDonald Ryan S]] | $85K | 54 | -2.0% | open |
| 2026-10-02 | [[GME]] | [[Cohen Ryan]] | $17.1M | 79 | +6.3% | open |
| 2026-10-01 | [[GME]] | [[Turner Nat]] | $255K | 66 | +9.8% | open |
| 2026-10-01 | [[DKS]] | [[Barnes Matthew]] | $500K | 78 | +7.1% | open |
| 2026-10-01 | [[FUL]] | [[Happe Michael J]] | $99K | 67 | +0.6% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "cluster_3")
SORT filed DESC
```

Back to [[What Works]].
