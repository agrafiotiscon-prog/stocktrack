---
type: "strategy"
key: "contrarian"
signals: 8134
cagr: 0.0167198
spy_cagr: 0.108549
sharpe: 0.174638
max_drawdown: 0.72227
holdout_excess: -0.0582116
---

# Insider buying after a 30%+ drop

Rule key: `contrarian`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 8,134 |
| 3-month excess vs SPY (mean / median) | +5.2% / +2.0% |
| Beat SPY over 3 months | 53% |
| Entering one session later | +4.8% |
| vs surviving stocks | +3.8% |
| 2006-2015 excess /yr | +13.7% (p 0.149) |
| 2016+ excess /yr | -5.8% (p 0.407) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +2.5% | +10.9% | 0.17 | 0.54 | 72% | 1.14 | -6.9% | 33% | 2,248 | 6.1% | +0.9% / 0.04 / 66% |
| 63d | +1.7% | +10.9% | 0.17 | 0.54 | 72% | 1.56 | -9.6% | 19% | 1,183 | 3.3% | -2.2% / -0.08 / 67% |
| 126d | +5.8% | +10.9% | 0.29 | 0.54 | 66% | 1.62 | -6.2% | 48% | 714 | 2.0% | +0.1% / 0.02 / 71% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +5.0%/yr, double costs -1.5%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +22.1% | +9.7% | +12.4% |
| 2007 | +4.5% | +5.1% | -0.7% |
| 2008 | -44.1% | -36.8% | -7.3% |
| 2009 | +24.9% | +26.4% | -1.4% |
| 2010 | +21.5% | +15.1% | +6.4% |
| 2011 | -8.2% | +1.9% | -10.1% |
| 2012 | +29.1% | +16.0% | +13.1% |
| 2013 | +24.0% | +32.3% | -8.3% |
| 2014 | -2.0% | +13.5% | -15.5% |
| 2015 | -21.6% | +1.2% | -22.8% |
| 2016 | +38.5% | +12.0% | +26.5% |
| 2017 | +15.0% | +21.7% | -6.7% |
| 2018 | -11.5% | -4.6% | -6.9% |
| 2019 | +31.1% | +31.2% | -0.1% |
| 2020 | +14.9% | +18.3% | -3.4% |
| 2021 | -10.2% | +28.7% | -38.9% |
| 2022 | -44.4% | -18.2% | -26.2% |
| 2023 | +10.2% | +26.2% | -15.9% |
| 2024 | -7.9% | +24.9% | -32.8% |
| 2025 | +4.6% | +17.7% | -13.1% |
| 2026 | +2.2% | +10.8% | -8.6% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 32 | +0.1% | +1.6% | 62% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-13 | [[INDI]] | [[ALDRICH DAVID J]] | $299K | 47 | – | pending |
| 2026-11-13 | [[FISN]] | [[Muller Elizabeth]] | $22K | 48 | – | pending |
| 2026-11-13 | [[UPST]] | [[Gu Paul]] | $1.0M | 63 | – | pending |
| 2026-11-13 | [[NXRT]] | [[McGraner Matt]] | $100K | 40 | – | pending |
| 2026-11-13 | [[BW]] | [[Moeller Philip D]] | $14K | 42 | – | pending |
| 2026-11-13 | [[BW]] | [[Tato Joseph A]] | $53K | 45 | – | pending |
| 2026-11-13 | [[AKAM]] | [[LEIGHTON F THOMSON]] | $2.6M | 52 | – | pending |
| 2026-11-13 | [[CAT]] | [[MacLennan David]] | $209K | 43 | – | pending |
| 2026-11-13 | [[IONS]] | [[Hayden Michael R]] | $148K | 37 | – | pending |
| 2026-11-13 | [[FF]] | [[Bedell Donald C]] | $113K | 68 | – | pending |
| 2026-11-13 | [[FF]] | [[Butcher Pamela R]] | $28K | 62 | – | pending |
| 2026-11-13 | [[FF]] | [[Polet Roeland]] | $136K | 81 | – | pending |
| 2026-11-13 | [[KGS]] | [[Holloway Gretchen Lynn]] | $50K | 46 | – | pending |
| 2026-11-13 | [[FF]] | [[SPARKS ROSE]] | $30K | 71 | – | pending |
| 2026-11-13 | [[KGS]] | [[Darden Alexander Newsom]] | $450K | 69 | – | pending |
| 2026-11-13 | [[HPP]] | [[LAMMAS MARK T]] | $44K | 62 | – | pending |
| 2026-11-13 | [[BW]] | [[Young Kenneth M]] | $44K | 54 | – | pending |
| 2026-11-12 | [[LRMR]] | [[Hamilton Thomas Edward]] | $187K | 70 | +1.1% | open |
| 2026-11-12 | [[HPP]] | [[BORTZ JON E]] | $680K | 62 | -5.2% | open |
| 2026-11-12 | [[HPP]] | [[COLEMAN VICTOR J]] | $182K | 62 | -5.2% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "contrarian")
SORT filed DESC
```

Back to [[What Works]].
