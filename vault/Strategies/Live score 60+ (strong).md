---
type: "strategy"
key: "score_60"
signals: 7190
cagr: 0.108412
spy_cagr: 0.110525
sharpe: 0.450139
max_drawdown: 0.619337
holdout_excess: 0.0190184
---

# Live score 60+ (strong)

Rule key: `score_60`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,190 |
| 3-month excess vs SPY (mean / median) | +1.6% / -0.5% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +1.4% |
| vs surviving stocks | +1.8% |
| 2006-2015 excess /yr | +7.3% (p 0.075) |
| 2016+ excess /yr | +1.9% (p 0.724) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.6% | +11.1% | 0.24 | 0.55 | 63% | 0.92 | -4.2% | 33% | 3,300 | 6.1% | +0.2% / -0.07 / 60% |
| 63d | +10.8% | +11.1% | 0.45 | 0.55 | 62% | 1.22 | -0.4% | 62% | 1,586 | 2.9% | +3.1% / 0.17 / 30% |
| 126d | +11.5% | +11.1% | 0.48 | 0.55 | 65% | 1.13 | +0.7% | 57% | 822 | 1.6% | +3.5% / 0.19 / 43% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +13.9%/yr, double costs +7.9%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.4% | +13.3% | +3.1% |
| 2007 | -13.5% | +5.1% | -18.6% |
| 2008 | -29.0% | -36.8% | +7.8% |
| 2009 | +41.3% | +26.4% | +15.0% |
| 2010 | +30.2% | +15.1% | +15.1% |
| 2011 | -2.9% | +1.9% | -4.8% |
| 2012 | +19.3% | +16.0% | +3.3% |
| 2013 | +45.1% | +32.3% | +12.8% |
| 2014 | +7.4% | +13.5% | -6.1% |
| 2015 | -12.9% | +1.2% | -14.2% |
| 2016 | +28.9% | +12.0% | +16.9% |
| 2017 | +28.0% | +21.7% | +6.3% |
| 2018 | -10.8% | -4.6% | -6.3% |
| 2019 | +47.2% | +31.2% | +16.0% |
| 2020 | +18.4% | +18.3% | +0.1% |
| 2021 | -0.8% | +28.7% | -29.5% |
| 2022 | -8.5% | -18.2% | +9.7% |
| 2023 | +34.4% | +26.2% | +8.2% |
| 2024 | +2.2% | +24.9% | -22.7% |
| 2025 | +23.3% | +17.7% | +5.6% |
| 2026 | +4.1% | +13.7% | -9.6% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 2 | -3.9% | +3.7% | 50% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-28 | [[TTMI]] | [[Roks Edwin]] | $440K | 62 | – | pending |
| 2026-10-28 | [[TTMI]] | [[Ali Wajid]] | $902K | 61 | – | pending |
| 2026-10-28 | [[ACN]] | [[Sweet Julie Spellman]] | $3.0M | 78 | – | pending |
| 2026-10-27 | [[MSM]] | [[JACOBSON MITCHELL]] | $29.0M | 63 | +1.8% | open |
| 2026-10-27 | [[STC]] | [[Matz Deborah Jane]] | $44K | 63 | +0.8% | open |
| 2026-10-27 | [[STC]] | [[EPPINGER FREDERICK H]] | $133K | 65 | +0.8% | open |
| 2026-10-27 | [[NPB]] | [[Long Joseph B]] | $50K | 65 | -0.8% | open |
| 2026-10-27 | [[NPB]] | [[Boer Carrie L]] | $185K | 65 | -0.8% | open |
| 2026-10-27 | [[NPB]] | [[Williams Charles Alan]] | $1.5M | 73 | -0.8% | open |
| 2026-10-26 | [[THRM]] | [[MASCARENAS PAUL ANTHONY]] | $533K | 61 | +10.6% | open |
| 2026-10-23 | [[NXG]] | [[Swank Jerry V]] | $439K | 64 | +7.4% | open |
| 2026-10-23 | [[NXG]] | [[Nelson Blake]] | $40K | 68 | +7.4% | open |
| 2026-10-23 | [[RAPP]] | [[Sanchez Ramiro]] | $98K | 67 | -14.8% | open |
| 2026-10-22 | [[RAPP]] | [[Silva Paul M]] | $100K | 67 | -19.9% | open |
| 2026-10-22 | [[RAPP]] | [[Young Wendy B]] | $100K | 65 | -19.9% | open |
| 2026-10-22 | [[RAPP]] | [[PAUL STEVEN M]] | $974K | 77 | -19.9% | open |
| 2026-10-22 | [[RAPP]] | [[MARAGANORE JOHN]] | $249K | 71 | -19.9% | open |
| 2026-10-19 | [[IAM]] | [[Rachlin Evan Lockwood]] | $11.5M | 60 | -10.2% | open |
| 2026-10-19 | [[BPRE]] | [[KAMFAR RAMIN]] | $2.4M | 64 | +1.8% | open |
| 2026-10-19 | [[APLD]] | [[Cummins Wes]] | $1.0M | 60 | +8.8% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_60")
SORT filed DESC
```

Back to [[What Works]].
