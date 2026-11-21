---
type: "strategy"
key: "cluster_3"
signals: 7460
cagr: 0.0561341
spy_cagr: 0.107555
sharpe: 0.27469
max_drawdown: 0.59275
holdout_excess: 0.0065984
---

# 3+ insiders buying within 14 days

Rule key: `cluster_3`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,460 |
| 3-month excess vs SPY (mean / median) | +2.0% / +0.0% |
| Beat SPY over 3 months | 50% |
| Entering one session later | +2.0% |
| vs surviving stocks | +2.0% |
| 2006-2015 excess /yr | +8.4% (p 0.039) |
| 2016+ excess /yr | +0.7% (p 0.898) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.3% | +10.8% | 0.31 | 0.54 | 52% | 0.75 | -1.2% | 24% | 2,854 | 6.0% | +1.8% / 0.06 / 35% |
| 63d | +5.6% | +10.8% | 0.27 | 0.54 | 59% | 1.14 | -4.6% | 33% | 1,543 | 2.9% | -1.4% / -0.15 / 55% |
| 126d | +10.5% | +10.8% | 0.44 | 0.54 | 67% | 1.13 | +0.1% | 52% | 821 | 1.6% | +2.8% / 0.15 / 34% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +8.6%/yr, double costs +2.7%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +17.2% | +13.3% | +3.9% |
| 2007 | -8.7% | +5.1% | -13.9% |
| 2008 | -27.5% | -36.8% | +9.3% |
| 2009 | +27.1% | +26.4% | +0.7% |
| 2010 | +30.2% | +15.1% | +15.1% |
| 2011 | -1.9% | +1.9% | -3.8% |
| 2012 | +24.5% | +16.0% | +8.5% |
| 2013 | +30.0% | +32.3% | -2.4% |
| 2014 | +2.0% | +13.5% | -11.4% |
| 2015 | -9.9% | +1.2% | -11.2% |
| 2016 | +26.3% | +12.0% | +14.3% |
| 2017 | +18.8% | +21.7% | -2.9% |
| 2018 | -15.7% | -4.6% | -11.1% |
| 2019 | +19.5% | +31.2% | -11.7% |
| 2020 | +35.1% | +18.3% | +16.8% |
| 2021 | +8.4% | +28.7% | -20.3% |
| 2022 | -38.0% | -18.2% | -19.8% |
| 2023 | +17.5% | +26.2% | -8.7% |
| 2024 | +2.9% | +24.9% | -22.0% |
| 2025 | +5.9% | +17.7% | -11.8% |
| 2026 | -5.2% | +8.2% | -13.4% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 47 | +1.1% | +1.5% | 64% |
| 21 sessions | 2 | -1.1% | +4.6% | 50% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-20 | [[CRMD]] | [[Blum Susan]] | $23K | 56 | – | pending |
| 2026-11-20 | [[EQPT]] | [[Schlacks Jabbok]] | $180K | 65 | – | pending |
| 2026-11-20 | [[UPBD]] | [[LEWIS HAROLD G]] | $399K | 73 | – | pending |
| 2026-11-20 | [[HPP]] | [[COLEMAN VICTOR J]] | $75K | 62 | – | pending |
| 2026-11-20 | [[OFRM]] | [[Garner Jennifer Anne]] | $118K | 50 | – | pending |
| 2026-11-20 | [[OFRM]] | [[Morris Scott James]] | $142K | 69 | – | pending |
| 2026-11-20 | [[SEI]] | [[TEAGUE AJ]] | $31K | 47 | – | pending |
| 2026-11-20 | [[SEI]] | [[Ramachandran Kyle S]] | $160K | 61 | – | pending |
| 2026-11-20 | [[SEI]] | [[Brock Amanda M]] | $269K | 68 | – | pending |
| 2026-11-20 | [[SEI]] | [[Zartler William A]] | $212K | 65 | – | pending |
| 2026-11-20 | [[CRMD]] | [[Lefkowitz Steven W]] | $52K | 48 | – | pending |
| 2026-11-20 | [[PICS]] | [[Costa de Moura Mauricio]] | $25K | 56 | – | pending |
| 2026-11-20 | [[CTGO]] | [[JUNEAU JOHN B]] | $97K | 46 | – | pending |
| 2026-11-20 | [[CTGO]] | [[Nauman Clynton R]] | $75K | 54 | – | pending |
| 2026-11-20 | [[MTDR]] | [[Foran Joseph Wm]] | $123K | 73 | – | pending |
| 2026-11-19 | [[RMIX]] | [[HEYER ANDREW R]] | $183K | 70 | -4.1% | open |
| 2026-11-19 | [[PAL]] | [[Schraudenbach John]] | $78K | 66 | -0.5% | open |
| 2026-11-19 | [[PAL]] | [[COL DOUGLAS L]] | $84K | 66 | -0.5% | open |
| 2026-11-19 | [[HPP]] | [[COLEMAN VICTOR J]] | $81K | 62 | -3.2% | open |
| 2026-11-19 | [[SRTS]] | [[Cornish Megan]] | $5K | 39 | -2.1% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "cluster_3")
SORT filed DESC
```

Back to [[What Works]].
