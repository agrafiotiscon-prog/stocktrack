---
type: "strategy"
key: "proven_insider"
signals: 20425
cagr: 0.108304
spy_cagr: 0.112438
sharpe: 0.455883
max_drawdown: 0.534823
holdout_excess: 0.00662708
---

# Insiders whose earlier buys beat SPY

Rule key: `proven_insider`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 20,425 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +0.6% |
| vs surviving stocks | +0.3% |
| 2006-2015 excess /yr | +5.3% (p 0.030) |
| 2016+ excess /yr | +0.7% (p 0.840) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +7.1% | +11.2% | 0.34 | 0.56 | 52% | 1.10 | -3.6% | 29% | 4,559 | 8.4% | -0.7% / -0.15 / 48% |
| 63d | +10.8% | +11.2% | 0.46 | 0.56 | 53% | 1.19 | -0.9% | 48% | 1,612 | 3.0% | +2.5% / 0.13 / 39% |
| 126d | +12.3% | +11.2% | 0.52 | 0.56 | 51% | 1.14 | +0.9% | 43% | 817 | 1.6% | +3.8% / 0.24 / 35% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +14.4%/yr, double costs +7.8%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +13.5% | +13.0% | +0.5% |
| 2007 | -7.6% | +5.1% | -12.7% |
| 2008 | -13.6% | -36.8% | +23.2% |
| 2009 | +48.0% | +26.4% | +21.7% |
| 2010 | +23.7% | +15.1% | +8.7% |
| 2011 | -0.6% | +1.9% | -2.5% |
| 2012 | +21.0% | +16.0% | +5.0% |
| 2013 | +32.9% | +32.3% | +0.6% |
| 2014 | +12.2% | +13.5% | -1.3% |
| 2015 | -11.8% | +1.2% | -13.1% |
| 2016 | +12.0% | +12.0% | +0.0% |
| 2017 | +6.1% | +21.7% | -15.6% |
| 2018 | -8.1% | -4.6% | -3.5% |
| 2019 | +30.1% | +31.2% | -1.2% |
| 2020 | +31.2% | +18.3% | +12.8% |
| 2021 | +37.7% | +28.7% | +9.0% |
| 2022 | -33.2% | -18.2% | -15.0% |
| 2023 | +20.7% | +26.2% | -5.5% |
| 2024 | +9.8% | +24.9% | -15.1% |
| 2025 | +14.7% | +17.7% | -3.0% |
| 2026 | +18.9% | +13.3% | +5.6% |


## Live forward test

2 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-19 | [[DSM]] | [[Saba Capital Management, L.P]] | $72K | 18 | – | pending |
| 2026-10-19 | [[EQBK]] | [[Borck Leon]] | $19K | 16 | – | pending |
| 2026-10-16 | [[SAH]] | [[Rusnak Paul P]] | $752K | 28 | -2.8% | open |
| 2026-10-16 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | -1.8% | open |
| 2026-10-13 | [[GME]] | [[Cohen Ryan]] | $22.8M | 71 | -3.5% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[CULLIGAN THOMAS M]] | $175K | 57 | +4.8% | open |
| 2026-10-13 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | +1.7% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[Hildebrandt Mark H]] | $175K | 53 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[SCHRIESHEIM ALAN]] | $175K | 69 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[HENRIQUES ADOLFO]] | $175K | 55 | +4.8% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | +0.5% | open |
| 2026-10-09 | [[NEOG]] | [[Nassif Mikheal]] | $6K | 44 | -1.4% | open |
| 2026-10-09 | [[MWA]] | [[Healy Brian C]] | $30K | 8 | +2.0% | open |
| 2026-10-09 | [[SAH]] | [[Rusnak Paul P]] | $819K | 29 | +4.6% | open |
| 2026-10-08 | [[CET]] | [[Hill John C]] | $28K | 32 | +1.5% | open |
| 2026-10-07 | [[SAH]] | [[Rusnak Paul P]] | $67K | 17 | +4.3% | open |
| 2026-10-06 | [[SAH]] | [[Rusnak Paul P]] | $1.7M | 32 | +3.4% | open |
| 2026-10-06 | [[DYN]] | [[Posner Brian S]] | $40K | 27 | +0.1% | open |
| 2026-10-06 | [[SAH]] | [[Rusnak Paul P]] | $1.3M | 31 | +3.4% | open |
| 2026-10-06 | [[AEF]] | [[Clark Anthony S]] | $19K | 31 | -8.1% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "proven_insider")
SORT filed DESC
```

Back to [[What Works]].
