---
type: "strategy"
key: "big_stake_up"
signals: 11397
cagr: 0.0900584
spy_cagr: 0.109148
sharpe: 0.390936
max_drawdown: 0.669115
holdout_excess: 0.0168533
---

# Exec/director growing stake 25%+ with $100K+

Rule key: `big_stake_up`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 11,397 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.5% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.6% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +6.2% (p 0.036) |
| 2016+ excess /yr | +1.7% (p 0.673) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.0% | +10.9% | 0.21 | 0.55 | 54% | 1.06 | -5.8% | 24% | 4,266 | 6.4% | -1.9% / -0.24 / 48% |
| 63d | +9.0% | +10.9% | 0.39 | 0.55 | 67% | 1.28 | -2.8% | 43% | 1,657 | 2.7% | +0.7% / -0.01 / 38% |
| 126d | +7.7% | +10.9% | 0.35 | 0.55 | 66% | 1.25 | -3.8% | 48% | 840 | 1.3% | -0.3% / -0.09 / 48% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +11.7%/yr, double costs +6.3%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +14.4% | +13.8% | +0.6% |
| 2007 | -5.6% | +5.1% | -10.8% |
| 2008 | -43.3% | -36.8% | -6.5% |
| 2009 | +56.7% | +26.4% | +30.4% |
| 2010 | +36.4% | +15.1% | +21.4% |
| 2011 | +7.2% | +1.9% | +5.3% |
| 2012 | +15.7% | +16.0% | -0.3% |
| 2013 | +50.6% | +32.3% | +18.3% |
| 2014 | +17.2% | +13.5% | +3.8% |
| 2015 | -7.1% | +1.2% | -8.3% |
| 2016 | +17.1% | +12.0% | +5.1% |
| 2017 | +17.5% | +21.7% | -4.2% |
| 2018 | -16.8% | -4.6% | -12.2% |
| 2019 | +48.2% | +31.2% | +16.9% |
| 2020 | +21.5% | +18.3% | +3.2% |
| 2021 | -6.4% | +28.7% | -35.1% |
| 2022 | -18.9% | -18.2% | -0.7% |
| 2023 | +17.9% | +26.2% | -8.3% |
| 2024 | +4.3% | +24.9% | -20.6% |
| 2025 | +11.9% | +17.7% | -5.8% |
| 2026 | +4.8% | +10.8% | -6.0% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 44 | +0.9% | +0.6% | 57% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-13 | [[STWD]] | [[Pollack Jonathan Lee]] | $2.0M | 67 | – | pending |
| 2026-11-13 | [[STWD]] | [[STERNLICHT BARRY S]] | $14.7M | 87 | – | pending |
| 2026-11-13 | [[INDI]] | [[ALDRICH DAVID J]] | $299K | 47 | – | pending |
| 2026-11-13 | [[CTRI]] | [[Patton Charles R]] | $250K | 55 | – | pending |
| 2026-11-13 | [[IOND]] | [[Abbate Michael]] | $1.3M | 53 | – | pending |
| 2026-11-13 | [[UPST]] | [[Gu Paul]] | $1.0M | 63 | – | pending |
| 2026-11-13 | [[FF]] | [[Bedell Donald C]] | $113K | 68 | – | pending |
| 2026-11-13 | [[FF]] | [[Polet Roeland]] | $136K | 81 | – | pending |
| 2026-11-13 | [[KGS]] | [[Darden Alexander Newsom]] | $450K | 69 | – | pending |
| 2026-11-13 | [[WY]] | [[BECKWITT RICHARD]] | $307K | 46 | – | pending |
| 2026-11-12 | [[ASR]] | [[Perez Anton Jose Antonio]] | $498K | 49 | -0.7% | open |
| 2026-11-12 | [[LRMR]] | [[Hamilton Thomas Edward]] | $187K | 70 | +1.1% | open |
| 2026-11-12 | [[HPP]] | [[BORTZ JON E]] | $680K | 62 | -5.2% | open |
| 2026-11-12 | [[BKD]] | [[WINKLE C CHRISTIAN]] | $358K | 48 | -0.3% | open |
| 2026-11-12 | [[MTDR]] | [[Foran Joseph Wm]] | $123K | 75 | +0.5% | open |
| 2026-11-12 | [[EQPT]] | [[HILL W BRYAN]] | $554K | 61 | -5.3% | open |
| 2026-11-12 | [[CSQR]] | [[Kelley Philip M]] | $172K | 56 | -3.1% | open |
| 2026-11-12 | [[STVN]] | [[FEDERICI WILLIAM J]] | $274K | 58 | +8.5% | open |
| 2026-11-12 | [[ALNY]] | [[Sigal Charles Elliott]] | $244K | 58 | +4.4% | open |
| 2026-11-12 | [[DOX]] | [[Genish Amos]] | $150K | 60 | +1.3% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "big_stake_up")
SORT filed DESC
```

Back to [[What Works]].
