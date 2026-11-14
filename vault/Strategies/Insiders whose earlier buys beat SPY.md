---
type: "strategy"
key: "proven_insider"
signals: 20084
cagr: 0.129009
spy_cagr: 0.11135
sharpe: 0.527923
max_drawdown: 0.601494
holdout_excess: 0.00385895
---

# Insiders whose earlier buys beat SPY

Rule key: `proven_insider`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 20,084 |
| 3-month excess vs SPY (mean / median) | +0.7% / -0.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +0.5% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +6.0% (p 0.022) |
| 2016+ excess /yr | +0.4% (p 0.906) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +7.6% | +11.1% | 0.35 | 0.56 | 52% | 1.09 | -3.0% | 29% | 4,538 | 8.6% | -0.5% / -0.14 / 45% |
| 63d | +12.9% | +11.1% | 0.53 | 0.56 | 60% | 1.22 | +0.9% | 48% | 1,612 | 3.1% | +4.3% / 0.27 / 30% |
| 126d | +9.1% | +11.1% | 0.41 | 0.56 | 57% | 1.12 | -1.8% | 43% | 817 | 1.5% | +0.5% / -0.04 / 39% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +16.3%/yr, double costs +9.4%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +15.5% | +13.9% | +1.7% |
| 2007 | +4.3% | +5.1% | -0.8% |
| 2008 | -19.2% | -36.8% | +17.6% |
| 2009 | +24.8% | +26.4% | -1.6% |
| 2010 | +42.2% | +15.1% | +27.1% |
| 2011 | +7.7% | +1.9% | +5.8% |
| 2012 | +14.9% | +16.0% | -1.1% |
| 2013 | +39.1% | +32.3% | +6.8% |
| 2014 | +13.8% | +13.5% | +0.3% |
| 2015 | -13.8% | +1.2% | -15.0% |
| 2016 | +25.3% | +12.0% | +13.3% |
| 2017 | +11.2% | +21.7% | -10.5% |
| 2018 | -12.9% | -4.6% | -8.3% |
| 2019 | +30.6% | +31.2% | -0.6% |
| 2020 | +38.8% | +18.3% | +20.5% |
| 2021 | +14.5% | +28.7% | -14.2% |
| 2022 | -25.4% | -18.2% | -7.2% |
| 2023 | +40.3% | +26.2% | +14.1% |
| 2024 | +15.7% | +24.9% | -9.2% |
| 2025 | +25.0% | +17.7% | +7.3% |
| 2026 | +6.9% | +10.8% | -3.9% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 73 | +2.7% | +2.5% | 73% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-13 | [[STWD]] | [[STERNLICHT BARRY S]] | $14.7M | 87 | – | pending |
| 2026-11-13 | [[FRPH]] | [[Baker John D. III]] | $930 | 10 | – | pending |
| 2026-11-13 | [[TRS]] | [[Tredwell Daniel P]] | $3K | 13 | – | pending |
| 2026-11-13 | [[CTEV]] | [[Dalton Travis]] | $150K | 58 | – | pending |
| 2026-11-13 | [[GLP]] | [[Global GP LLC]] | $442K | 27 | – | pending |
| 2026-11-13 | [[NXRT]] | [[McGraner Matt]] | $100K | 40 | – | pending |
| 2026-11-13 | [[BW]] | [[Moeller Philip D]] | $14K | 42 | – | pending |
| 2026-11-13 | [[BW]] | [[Tato Joseph A]] | $53K | 45 | – | pending |
| 2026-11-13 | [[TRIN]] | [[Brown Kyle Steven]] | $58K | 35 | – | pending |
| 2026-11-13 | [[AKAM]] | [[LEIGHTON F THOMSON]] | $2.6M | 52 | – | pending |
| 2026-11-13 | [[FF]] | [[Bedell Donald C]] | $113K | 68 | – | pending |
| 2026-11-13 | [[TXO]] | [[SIMPSON BOB R]] | $945K | 34 | – | pending |
| 2026-11-13 | [[FF]] | [[Polet Roeland]] | $136K | 81 | – | pending |
| 2026-11-13 | [[NGS]] | [[JACKSON JOHN EARL]] | $58K | 40 | – | pending |
| 2026-11-13 | [[BW]] | [[Young Kenneth M]] | $44K | 54 | – | pending |
| 2026-11-13 | [[ABCL]] | [[Booth Andrew]] | $97K | 48 | – | pending |
| 2026-11-12 | [[HPP]] | [[COLEMAN VICTOR J]] | $182K | 62 | -5.2% | open |
| 2026-11-12 | [[FNRN]] | [[Servat Jean-Luc]] | $5K | 19 | +2.0% | open |
| 2026-11-12 | [[BLMN]] | [[Spanos Mike]] | $502K | 55 | -0.2% | open |
| 2026-11-12 | [[MTDR]] | [[Foran Joseph Wm]] | $123K | 75 | +0.5% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "proven_insider")
SORT filed DESC
```

Back to [[What Works]].
