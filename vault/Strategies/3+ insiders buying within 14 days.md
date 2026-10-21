---
type: "strategy"
key: "cluster_3"
signals: 7455
cagr: 0.0603797
spy_cagr: 0.110594
sharpe: 0.289693
max_drawdown: 0.59275
holdout_excess: 0.00895897
---

# 3+ insiders buying within 14 days

Rule key: `cluster_3`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,455 |
| 3-month excess vs SPY (mean / median) | +2.1% / +0.1% |
| Beat SPY over 3 months | 50% |
| Entering one session later | +2.1% |
| vs surviving stocks | +2.0% |
| 2006-2015 excess /yr | +8.8% (p 0.029) |
| 2016+ excess /yr | +0.9% (p 0.864) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.1% | +11.1% | 0.30 | 0.55 | 52% | 0.74 | -1.5% | 24% | 2,846 | 6.0% | +1.6% / 0.04 / 36% |
| 63d | +6.0% | +11.1% | 0.29 | 0.55 | 59% | 1.13 | -4.4% | 33% | 1,538 | 3.0% | -1.0% / -0.12 / 54% |
| 126d | +10.7% | +11.1% | 0.45 | 0.55 | 67% | 1.14 | -0.0% | 52% | 821 | 1.7% | +2.8% / 0.15 / 46% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +9.4%/yr, double costs +3.1%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +17.2% | +13.3% | +3.9% |
| 2007 | -8.7% | +5.1% | -13.9% |
| 2008 | -27.5% | -36.8% | +9.3% |
| 2009 | +27.1% | +26.4% | +0.7% |
| 2010 | +30.2% | +15.1% | +15.1% |
| 2011 | -2.6% | +1.9% | -4.5% |
| 2012 | +32.5% | +16.0% | +16.5% |
| 2013 | +30.5% | +32.3% | -1.8% |
| 2014 | +2.4% | +13.5% | -11.1% |
| 2015 | -9.7% | +1.2% | -10.9% |
| 2016 | +24.1% | +12.0% | +12.1% |
| 2017 | +18.6% | +21.7% | -3.1% |
| 2018 | -14.7% | -4.6% | -10.1% |
| 2019 | +18.3% | +31.2% | -12.9% |
| 2020 | +35.0% | +18.3% | +16.7% |
| 2021 | +10.1% | +28.7% | -18.6% |
| 2022 | -35.2% | -18.2% | -17.1% |
| 2023 | +16.8% | +26.2% | -9.4% |
| 2024 | +0.7% | +24.9% | -24.2% |
| 2025 | +3.3% | +17.7% | -14.5% |
| 2026 | -2.7% | +13.7% | -16.4% |


## Live forward test

1 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-19 | [[BPRE]] | [[KAMFAR RAMIN]] | $2.4M | 64 | +0.8% | open |
| 2026-10-15 | [[BPRE]] | [[MacDonald Ryan S]] | $2K | 34 | -0.7% | open |
| 2026-10-15 | [[BPRE]] | [[Ruddy Jordan B]] | $44K | 63 | -0.7% | open |
| 2026-10-15 | [[IMSR]] | [[Pardee Charles G]] | $22K | 55 | -13.0% | open |
| 2026-10-14 | [[BPRE]] | [[KAMFAR RAMIN]] | $5.5M | 73 | -1.9% | open |
| 2026-10-13 | [[HEI]] | [[CULLIGAN THOMAS M]] | $175K | 57 | +3.4% | open |
| 2026-10-13 | [[HEI]] | [[Hildebrandt Mark H]] | $175K | 53 | +3.4% | open |
| 2026-10-13 | [[HEI]] | [[Fine Carol F]] | $175K | 69 | +3.4% | open |
| 2026-10-13 | [[HEI]] | [[SCHRIESHEIM ALAN]] | $175K | 69 | +3.4% | open |
| 2026-10-13 | [[HEI]] | [[HENRIQUES ADOLFO]] | $175K | 55 | +3.4% | open |
| 2026-10-13 | [[HEI]] | [[CHERUVATATH NANDAKUMAR]] | $175K | 62 | +3.4% | open |
| 2026-10-09 | [[BPRE]] | [[KAMFAR RAMIN]] | $8.5M | 81 | -4.3% | open |
| 2026-10-08 | [[PDI]] | [[FLATTUM DAVID C]] | $250K | 66 | +0.9% | open |
| 2026-10-08 | [[FUL]] | [[BAILLY R JEFFREY]] | $500K | 74 | +2.1% | open |
| 2026-10-05 | [[BPRE]] | [[KAMFAR RAMIN]] | $3.4M | 73 | -1.2% | open |
| 2026-10-05 | [[BPRE]] | [[MacDonald Ryan S]] | $85K | 54 | -1.2% | open |
| 2026-10-02 | [[GME]] | [[Cohen Ryan]] | $17.1M | 79 | +6.1% | open |
| 2026-10-01 | [[GME]] | [[Turner Nat]] | $255K | 66 | +9.6% | open |
| 2026-10-01 | [[DKS]] | [[Barnes Matthew]] | $500K | 78 | +6.3% | open |
| 2026-10-01 | [[FUL]] | [[Happe Michael J]] | $99K | 67 | -0.6% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "cluster_3")
SORT filed DESC
```

Back to [[What Works]].
