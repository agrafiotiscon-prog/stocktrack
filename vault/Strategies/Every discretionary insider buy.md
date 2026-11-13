---
type: "strategy"
key: "all_liquid"
signals: 67450
cagr: 0.0493045
spy_cagr: 0.109148
sharpe: 0.249961
max_drawdown: 0.610006
holdout_excess: 0.00144513
---

# Every discretionary insider buy

Rule key: `all_liquid`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 67,450 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.8% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.6% |
| vs surviving stocks | +1.0% |
| 2006-2015 excess /yr | +6.3% (p 0.019) |
| 2016+ excess /yr | +0.1% (p 0.968) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.9% | +10.9% | 0.32 | 0.55 | 61% | 1.22 | -3.9% | 38% | 4,991 | 9.2% | -1.5% / -0.16 / 68% |
| 63d | +4.9% | +10.9% | 0.25 | 0.55 | 61% | 1.15 | -5.7% | 48% | 1,677 | 2.7% | -3.4% / -0.35 / 70% |
| 126d | +7.0% | +10.9% | 0.33 | 0.55 | 54% | 1.15 | -3.8% | 33% | 840 | 1.5% | -1.8% / -0.19 / 57% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +7.9%/yr, double costs +2.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +24.3% | +13.8% | +10.4% |
| 2007 | -7.8% | +5.1% | -13.0% |
| 2008 | -22.2% | -36.8% | +14.6% |
| 2009 | +52.7% | +26.4% | +26.4% |
| 2010 | +21.7% | +15.1% | +6.6% |
| 2011 | -10.5% | +1.9% | -12.4% |
| 2012 | +21.5% | +16.0% | +5.6% |
| 2013 | +38.8% | +32.3% | +6.5% |
| 2014 | +1.8% | +13.5% | -11.7% |
| 2015 | +6.1% | +1.2% | +4.8% |
| 2016 | +15.1% | +12.0% | +3.1% |
| 2017 | +23.8% | +21.7% | +2.1% |
| 2018 | -10.3% | -4.6% | -5.7% |
| 2019 | +8.0% | +31.2% | -23.2% |
| 2020 | +36.1% | +18.3% | +17.8% |
| 2021 | -9.4% | +28.7% | -38.2% |
| 2022 | -35.7% | -18.2% | -17.6% |
| 2023 | +24.8% | +26.2% | -1.3% |
| 2024 | -15.1% | +24.9% | -40.0% |
| 2025 | -14.4% | +17.7% | -32.1% |
| 2026 | +1.6% | +10.8% | -9.2% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 234 | +1.1% | +1.5% | 63% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-12 | [[ASR]] | [[Perez Anton Jose Antonio]] | $498K | 49 | – | pending |
| 2026-11-12 | [[LRMR]] | [[Hamilton Thomas Edward]] | $187K | 70 | – | pending |
| 2026-11-12 | [[HPP]] | [[BORTZ JON E]] | $680K | 62 | – | pending |
| 2026-11-12 | [[HPP]] | [[COLEMAN VICTOR J]] | $182K | 62 | – | pending |
| 2026-11-12 | [[VISN]] | [[Watts Claudius E. IV]] | $198K | 30 | – | pending |
| 2026-11-12 | [[VISN]] | [[Watts Claudius E. IV]] | $831K | 42 | – | pending |
| 2026-11-12 | [[FNRN]] | [[Servat Jean-Luc]] | $5K | 19 | – | pending |
| 2026-11-12 | [[ENOV]] | [[Wienbar Sharon L]] | $50K | 37 | – | pending |
| 2026-11-12 | [[ENOV]] | [[Lalor Angela S]] | $50K | 38 | – | pending |
| 2026-11-12 | [[IOSP]] | [[PARRETTE LESLIE J]] | $27K | 23 | – | pending |
| 2026-11-12 | [[EQPT]] | [[Schlacks Jabbok]] | $250K | 61 | – | pending |
| 2026-11-12 | [[BKD]] | [[WINKLE C CHRISTIAN]] | $358K | 48 | – | pending |
| 2026-11-12 | [[BLMN]] | [[Spanos Mike]] | $502K | 55 | – | pending |
| 2026-11-12 | [[MTDR]] | [[Foran Joseph Wm]] | $123K | 75 | – | pending |
| 2026-11-12 | [[LRMR]] | [[BEN-MAIMON CAROLE]] | $50K | 63 | – | pending |
| 2026-11-12 | [[LRMR]] | [[THOMAS FRANK E]] | $22K | 60 | – | pending |
| 2026-11-12 | [[LRMR]] | [[Truitt Joseph]] | $10K | 57 | – | pending |
| 2026-11-12 | [[LRMR]] | [[Harlow John B. Jr]] | $50K | 71 | – | pending |
| 2026-11-12 | [[LRMR]] | [[Celano Michael]] | $50K | 62 | – | pending |
| 2026-11-12 | [[JOF]] | [[Saba Capital Management, L.P]] | $14K | 10 | – | pending |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "all_liquid")
SORT filed DESC
```

Back to [[What Works]].
