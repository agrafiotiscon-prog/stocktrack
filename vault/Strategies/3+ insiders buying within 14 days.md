---
type: "strategy"
key: "cluster_3"
signals: 7449
cagr: 0.0642904
spy_cagr: 0.109342
sharpe: 0.303152
max_drawdown: 0.59275
holdout_excess: 0.00692887
---

# 3+ insiders buying within 14 days

Rule key: `cluster_3`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,449 |
| 3-month excess vs SPY (mean / median) | +2.1% / +0.1% |
| Beat SPY over 3 months | 50% |
| Entering one session later | +2.0% |
| vs surviving stocks | +2.0% |
| 2006-2015 excess /yr | +8.4% (p 0.037) |
| 2016+ excess /yr | +0.7% (p 0.894) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.4% | +10.9% | 0.32 | 0.55 | 52% | 0.75 | -1.2% | 24% | 2,846 | 6.0% | +1.7% / 0.06 / 35% |
| 63d | +6.4% | +10.9% | 0.30 | 0.55 | 59% | 1.13 | -3.9% | 33% | 1,540 | 3.0% | -0.8% / -0.11 / 50% |
| 126d | +10.5% | +10.9% | 0.44 | 0.55 | 67% | 1.14 | -0.1% | 48% | 822 | 1.7% | +2.5% / 0.12 / 46% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +9.6%/yr, double costs +3.5%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +17.2% | +13.3% | +3.9% |
| 2007 | -8.7% | +5.1% | -13.9% |
| 2008 | -27.5% | -36.8% | +9.3% |
| 2009 | +27.1% | +26.4% | +0.7% |
| 2010 | +30.2% | +15.1% | +15.1% |
| 2011 | -2.6% | +1.9% | -4.5% |
| 2012 | +25.6% | +16.0% | +9.6% |
| 2013 | +30.0% | +32.3% | -2.4% |
| 2014 | +2.0% | +13.5% | -11.4% |
| 2015 | -10.5% | +1.2% | -11.8% |
| 2016 | +26.4% | +12.0% | +14.4% |
| 2017 | +18.8% | +21.7% | -2.9% |
| 2018 | -14.8% | -4.6% | -10.2% |
| 2019 | +18.3% | +31.2% | -12.9% |
| 2020 | +35.1% | +18.3% | +16.7% |
| 2021 | +10.0% | +28.7% | -18.7% |
| 2022 | -33.9% | -18.2% | -15.7% |
| 2023 | +16.8% | +26.2% | -9.4% |
| 2024 | +0.7% | +24.9% | -24.2% |
| 2025 | +8.1% | +17.7% | -9.7% |
| 2026 | +3.9% | +11.5% | -7.6% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 7 | +0.6% | +3.7% | 57% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-03 | [[OCFC]] | [[Farris Jack M]] | $10K | 36 | – | pending |
| 2026-11-03 | [[TRTX]] | [[Gillmore Michael]] | $13K | 53 | – | pending |
| 2026-11-03 | [[STRZ]] | [[Kapenstein James M]] | $11K | 40 | – | pending |
| 2026-11-02 | [[BBT]] | [[Hughes William H III]] | $6K | 40 | -2.2% | open |
| 2026-10-30 | [[RAPP]] | [[HEALY JAMES]] | $20.4M | 87 | +1.8% | open |
| 2026-10-30 | [[BBT]] | [[Charnley Nina A]] | $11K | 57 | +2.3% | open |
| 2026-10-29 | [[NPB]] | [[Chaudhary Rajeev Kumar]] | $47K | 64 | -2.3% | open |
| 2026-10-29 | [[BBT]] | [[Callahan Mary Anne]] | $97K | 54 | +0.5% | open |
| 2026-10-28 | [[BBT]] | [[Rosengren Eric S]] | $21K | 44 | +1.5% | open |
| 2026-10-28 | [[BBT]] | [[Fitzgerald Margaret Boles]] | $10K | 36 | +1.5% | open |
| 2026-10-27 | [[STC]] | [[Matz Deborah Jane]] | $44K | 63 | +4.1% | open |
| 2026-10-27 | [[STC]] | [[EPPINGER FREDERICK H]] | $133K | 65 | +4.1% | open |
| 2026-10-27 | [[NPB]] | [[Long Joseph B]] | $50K | 65 | -1.2% | open |
| 2026-10-27 | [[NPB]] | [[Boer Carrie L]] | $185K | 65 | -1.2% | open |
| 2026-10-27 | [[NPB]] | [[Williams Charles Alan]] | $1.5M | 73 | -1.2% | open |
| 2026-10-26 | [[STC]] | [[Apel Thomas G]] | $95K | 48 | +3.7% | open |
| 2026-10-26 | [[STC]] | [[Corey William S. Jr]] | $94K | 54 | +3.7% | open |
| 2026-10-26 | [[STC]] | [[BRADLEY C ALLEN JR]] | $95K | 50 | +3.7% | open |
| 2026-10-23 | [[NXG]] | [[Swank Jerry V]] | $439K | 64 | +5.6% | open |
| 2026-10-23 | [[NXG]] | [[Nelson Blake]] | $40K | 68 | +5.6% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "cluster_3")
SORT filed DESC
```

Back to [[What Works]].
