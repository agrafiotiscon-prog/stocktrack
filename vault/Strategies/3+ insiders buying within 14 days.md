---
type: "strategy"
key: "cluster_3"
signals: 7453
cagr: 0.0669319
spy_cagr: 0.110525
sharpe: 0.3123
max_drawdown: 0.59275
holdout_excess: 0.0066015
---

# 3+ insiders buying within 14 days

Rule key: `cluster_3`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,453 |
| 3-month excess vs SPY (mean / median) | +2.1% / +0.1% |
| Beat SPY over 3 months | 50% |
| Entering one session later | +2.0% |
| vs surviving stocks | +2.0% |
| 2006-2015 excess /yr | +8.8% (p 0.029) |
| 2016+ excess /yr | +0.7% (p 0.900) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.2% | +11.1% | 0.31 | 0.55 | 52% | 0.74 | -1.4% | 24% | 2,847 | 5.9% | +1.6% / 0.04 / 36% |
| 63d | +6.7% | +11.1% | 0.31 | 0.55 | 59% | 1.13 | -3.8% | 33% | 1,539 | 3.0% | -0.6% / -0.09 / 51% |
| 126d | +10.9% | +11.1% | 0.45 | 0.55 | 67% | 1.14 | +0.1% | 52% | 822 | 1.7% | +2.8% / 0.15 / 46% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +10.0%/yr, double costs +3.7%/yr.


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
| 2014 | +2.0% | +13.5% | -11.5% |
| 2015 | -9.9% | +1.2% | -11.2% |
| 2016 | +26.3% | +12.0% | +14.3% |
| 2017 | +18.8% | +21.7% | -3.0% |
| 2018 | -14.8% | -4.6% | -10.2% |
| 2019 | +18.3% | +31.2% | -12.9% |
| 2020 | +35.0% | +18.3% | +16.7% |
| 2021 | +10.2% | +28.7% | -18.6% |
| 2022 | -35.3% | -18.2% | -17.1% |
| 2023 | +16.8% | +26.2% | -9.4% |
| 2024 | +0.7% | +24.9% | -24.2% |
| 2025 | +8.0% | +17.7% | -9.7% |
| 2026 | +4.7% | +13.7% | -9.0% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 2 | -4.8% | +3.7% | 50% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-29 | [[NPB]] | [[Chaudhary Rajeev Kumar]] | $47K | 64 | – | pending |
| 2026-10-29 | [[BBT]] | [[Callahan Mary Anne]] | $97K | 54 | – | pending |
| 2026-10-28 | [[BBT]] | [[Rosengren Eric S]] | $21K | 44 | -1.1% | open |
| 2026-10-28 | [[BBT]] | [[Fitzgerald Margaret Boles]] | $10K | 36 | -1.1% | open |
| 2026-10-27 | [[STC]] | [[Matz Deborah Jane]] | $44K | 63 | +3.8% | open |
| 2026-10-27 | [[STC]] | [[EPPINGER FREDERICK H]] | $133K | 65 | +3.8% | open |
| 2026-10-27 | [[NPB]] | [[Long Joseph B]] | $50K | 65 | -0.5% | open |
| 2026-10-27 | [[NPB]] | [[Boer Carrie L]] | $185K | 65 | -0.5% | open |
| 2026-10-27 | [[NPB]] | [[Williams Charles Alan]] | $1.5M | 73 | -0.5% | open |
| 2026-10-26 | [[STC]] | [[Apel Thomas G]] | $95K | 48 | +3.4% | open |
| 2026-10-26 | [[STC]] | [[Corey William S. Jr]] | $94K | 54 | +3.4% | open |
| 2026-10-26 | [[STC]] | [[BRADLEY C ALLEN JR]] | $95K | 50 | +3.4% | open |
| 2026-10-23 | [[NXG]] | [[Swank Jerry V]] | $439K | 64 | +9.0% | open |
| 2026-10-23 | [[NXG]] | [[Nelson Blake]] | $40K | 68 | +9.0% | open |
| 2026-10-23 | [[RAPP]] | [[Sanchez Ramiro]] | $98K | 67 | -7.9% | open |
| 2026-10-22 | [[RAPP]] | [[Silva Paul M]] | $100K | 67 | -13.3% | open |
| 2026-10-22 | [[RAPP]] | [[Young Wendy B]] | $100K | 65 | -13.3% | open |
| 2026-10-22 | [[RAPP]] | [[PAUL STEVEN M]] | $974K | 77 | -13.3% | open |
| 2026-10-22 | [[RAPP]] | [[MARAGANORE JOHN]] | $249K | 71 | -13.3% | open |
| 2026-10-19 | [[BPRE]] | [[KAMFAR RAMIN]] | $2.4M | 64 | +3.2% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "cluster_3")
SORT filed DESC
```

Back to [[What Works]].
