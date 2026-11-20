---
type: "strategy"
key: "big_stake_up"
signals: 11413
cagr: 0.0892515
spy_cagr: 0.107784
sharpe: 0.388164
max_drawdown: 0.669115
holdout_excess: 0.0172159
---

# Exec/director growing stake 25%+ with $100K+

Rule key: `big_stake_up`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 11,413 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.5% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.5% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +6.3% (p 0.035) |
| 2016+ excess /yr | +1.7% (p 0.668) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.6% | +10.8% | 0.20 | 0.54 | 54% | 1.05 | -6.1% | 19% | 4,269 | 6.3% | -2.2% / -0.26 / 52% |
| 63d | +8.9% | +10.8% | 0.39 | 0.54 | 67% | 1.29 | -2.8% | 52% | 1,657 | 2.7% | +0.8% / -0.00 / 36% |
| 126d | +7.6% | +10.8% | 0.34 | 0.54 | 66% | 1.26 | -3.8% | 48% | 840 | 1.3% | -0.2% / -0.08 / 47% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +11.6%/yr, double costs +6.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +14.2% | +13.8% | +0.3% |
| 2007 | -5.6% | +5.1% | -10.8% |
| 2008 | -43.3% | -36.8% | -6.5% |
| 2009 | +57.3% | +26.4% | +30.9% |
| 2010 | +35.2% | +15.1% | +20.1% |
| 2011 | +3.3% | +1.9% | +1.4% |
| 2012 | +17.9% | +16.0% | +1.9% |
| 2013 | +50.3% | +32.3% | +17.9% |
| 2014 | +17.2% | +13.5% | +3.8% |
| 2015 | -6.5% | +1.2% | -7.7% |
| 2016 | +17.1% | +12.0% | +5.1% |
| 2017 | +17.5% | +21.7% | -4.2% |
| 2018 | -16.8% | -4.6% | -12.2% |
| 2019 | +48.2% | +31.2% | +16.9% |
| 2020 | +21.5% | +18.3% | +3.2% |
| 2021 | -6.3% | +28.7% | -35.1% |
| 2022 | -16.6% | -18.2% | +1.6% |
| 2023 | +20.4% | +26.2% | -5.8% |
| 2024 | +5.8% | +24.9% | -19.1% |
| 2025 | +11.7% | +17.7% | -6.0% |
| 2026 | -0.6% | +8.2% | -8.9% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 69 | +0.6% | +0.2% | 52% |
| 21 sessions | 4 | -2.2% | -2.8% | 25% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-19 | [[RMIX]] | [[HEYER ANDREW R]] | $183K | 70 | – | pending |
| 2026-11-19 | [[CCB]] | [[HOVDE STEVEN D]] | $550K | 49 | – | pending |
| 2026-11-19 | [[IRTC]] | [[TALWALKAR ABHIJIT Y]] | $764K | 51 | – | pending |
| 2026-11-19 | [[BGS]] | [[Mills Robert D]] | $250K | 54 | – | pending |
| 2026-11-19 | [[PLD]] | [[KELLY ALFRED F JR]] | $587K | 50 | – | pending |
| 2026-11-19 | [[APC]] | [[HEYER ANDREW R]] | $279K | 46 | – | pending |
| 2026-11-19 | [[BCML]] | [[PERDUE MICHAEL J]] | $151K | 44 | – | pending |
| 2026-11-19 | [[ITT]] | [[Berryman Kevin C]] | $502K | 49 | – | pending |
| 2026-11-19 | [[SKYD]] | [[Cardinale Gerald J]] | $495K | 48 | – | pending |
| 2026-11-19 | [[AVK]] | [[MAITLAND TRACY V]] | $203K | 55 | – | pending |
| 2026-11-19 | [[HMH]] | [[McGee Thomas W]] | $1.6M | 76 | – | pending |
| 2026-11-19 | [[SRTS]] | [[Sachetta Eric]] | $183K | 52 | – | pending |
| 2026-11-18 | [[USAR]] | [[BLITZER MICHAEL]] | $3.0M | 51 | +2.6% | open |
| 2026-11-18 | [[RMIX]] | [[Rees-Jones David]] | $731K | 76 | -12.5% | open |
| 2026-11-18 | [[OIG]] | [[DEUTSCH ROBERT V]] | $106K | 54 | +1.6% | open |
| 2026-11-18 | [[ECC]] | [[Majewski Thomas P]] | $118K | 68 | +8.0% | open |
| 2026-11-18 | [[BA]] | [[JOHRI AKHIL]] | $500K | 49 | +0.9% | open |
| 2026-11-18 | [[KGS]] | [[HOGAN RANDALL J]] | $494K | 71 | +0.4% | open |
| 2026-11-18 | [[NPCE]] | [[Huennekens R Scott]] | $104K | 62 | +0.2% | open |
| 2026-11-18 | [[GPRK]] | [[Gilinski Gabriel]] | $1.6M | 54 | -2.2% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "big_stake_up")
SORT filed DESC
```

Back to [[What Works]].
