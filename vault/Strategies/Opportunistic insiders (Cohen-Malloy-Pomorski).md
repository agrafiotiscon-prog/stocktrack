---
type: "strategy"
key: "opportunistic"
signals: 9649
cagr: 0.12216
spy_cagr: 0.114568
sharpe: 0.54767
max_drawdown: 0.493905
holdout_excess: -0.0285455
---

# Opportunistic insiders (Cohen-Malloy-Pomorski)

Rule key: `opportunistic`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 9,649 |
| 3-month excess vs SPY (mean / median) | +0.3% / -1.1% |
| Beat SPY over 3 months | 46% |
| Entering one session later | +0.2% |
| vs surviving stocks | +0.8% |
| 2006-2015 excess /yr | +6.6% (p 0.052) |
| 2016+ excess /yr | -2.9% (p 0.434) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.0% | +11.5% | 0.23 | 0.58 | 52% | 0.81 | -4.4% | 32% | 3,630 | 8.0% | -3.9% / -0.47 / 60% |
| 63d | +12.2% | +11.5% | 0.55 | 0.58 | 49% | 1.08 | +1.1% | 47% | 1,446 | 3.5% | +1.7% / 0.09 / 35% |
| 126d | +10.1% | +11.5% | 0.45 | 0.58 | 52% | 1.08 | -0.9% | 47% | 741 | 1.7% | +0.5% / -0.01 / 35% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +15.9%/yr, double costs +8.9%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2008 | -2.4% | -34.6% | +32.2% |
| 2009 | +22.7% | +26.4% | -3.7% |
| 2010 | +29.8% | +15.1% | +14.7% |
| 2011 | +4.0% | +1.9% | +2.1% |
| 2012 | +17.1% | +16.0% | +1.1% |
| 2013 | +41.1% | +32.3% | +8.8% |
| 2014 | +10.1% | +13.5% | -3.3% |
| 2015 | -8.8% | +1.2% | -10.0% |
| 2016 | +18.2% | +12.0% | +6.2% |
| 2017 | +5.2% | +21.7% | -16.5% |
| 2018 | -9.1% | -4.6% | -4.5% |
| 2019 | +28.9% | +31.2% | -2.3% |
| 2020 | +4.4% | +18.3% | -13.9% |
| 2021 | +35.5% | +28.7% | +6.7% |
| 2022 | -24.0% | -18.2% | -5.8% |
| 2023 | +36.0% | +26.2% | +9.8% |
| 2024 | +8.0% | +24.9% | -16.9% |
| 2025 | -3.0% | +17.7% | -20.7% |
| 2026 | +45.4% | +13.7% | +31.7% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 2 | +5.0% | +6.1% | 100% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-27 | [[SRRK]] | [[AKKARAJU SRINIVAS]] | $12.0M | 48 | – | pending |
| 2026-10-27 | [[PEBO]] | [[Smith Dwight Eric]] | $12K | 17 | – | pending |
| 2026-10-27 | [[FFIN]] | [[Nickles Robert Clark Jr]] | $25K | 19 | – | pending |
| 2026-10-26 | [[TCBX]] | [[Bobbora William]] | $40K | 24 | -1.4% | open |
| 2026-10-22 | [[VKI]] | [[BANK OF AMERICA CORP -DE-]] | $843 | 28 | -1.5% | open |
| 2026-10-22 | [[NMCO]] | [[BANK OF AMERICA CORP -DE-]] | $974 | 40 | -0.6% | open |
| 2026-10-22 | [[NBH]] | [[BANK OF AMERICA CORP -DE-]] | $845 | 28 | +1.0% | open |
| 2026-10-22 | [[LEO]] | [[BANK OF AMERICA CORP -DE-]] | $1K | 40 | +1.7% | open |
| 2026-10-22 | [[DSM]] | [[BANK OF AMERICA CORP -DE-]] | $1K | 40 | +1.3% | open |
| 2026-10-22 | [[NMCO]] | [[Jones Nathaniel T]] | $4K | 40 | -0.6% | open |
| 2026-10-20 | [[NXG]] | [[Sunderland Todd]] | $46K | 26 | +6.1% | open |
| 2026-10-20 | [[ISBA]] | [[Bourland Jill]] | $300 | 13 | +3.9% | open |
| 2026-10-16 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | +1.7% | open |
| 2026-10-13 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | +5.3% | open |
| 2026-10-13 | [[HEI]] | [[Hildebrandt Mark H]] | $175K | 53 | +4.6% | open |
| 2026-10-13 | [[HEI]] | [[SCHRIESHEIM ALAN]] | $175K | 69 | +4.6% | open |
| 2026-10-08 | [[IMMR]] | [[Singer Eric]] | $293K | 44 | +0.1% | open |
| 2026-10-08 | [[CET]] | [[Hill John C]] | $28K | 32 | +1.8% | open |
| 2026-10-06 | [[AEF]] | [[Clark Anthony S]] | $19K | 31 | -11.5% | open |
| 2026-10-05 | [[LEN]] | [[BERKSHIRE HATHAWAY INC]] | $192.6M | 70 | +14.7% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "opportunistic")
SORT filed DESC
```

Back to [[What Works]].
