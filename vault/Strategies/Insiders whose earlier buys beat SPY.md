---
type: "strategy"
key: "proven_insider"
signals: 20163
cagr: 0.0985475
spy_cagr: 0.109955
sharpe: 0.425576
max_drawdown: 0.614364
holdout_excess: 0.00444686
---

# Insiders whose earlier buys beat SPY

Rule key: `proven_insider`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 20,163 |
| 3-month excess vs SPY (mean / median) | +0.7% / -0.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +0.5% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +6.0% (p 0.019) |
| 2016+ excess /yr | +0.4% (p 0.892) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.5% | +11.0% | 0.31 | 0.55 | 52% | 1.07 | -3.7% | 24% | 4,543 | 8.4% | -1.2% / -0.20 / 51% |
| 63d | +9.9% | +11.0% | 0.43 | 0.55 | 61% | 1.19 | -1.4% | 48% | 1,617 | 3.2% | +1.8% / 0.07 / 43% |
| 126d | +8.3% | +11.0% | 0.38 | 0.55 | 57% | 1.17 | -2.8% | 33% | 820 | 1.5% | -0.1% / -0.09 / 39% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +13.6%/yr, double costs +6.6%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.9% | +13.9% | +3.0% |
| 2007 | +1.5% | +5.1% | -3.6% |
| 2008 | -22.3% | -36.8% | +14.5% |
| 2009 | +23.9% | +26.4% | -2.5% |
| 2010 | +41.5% | +15.1% | +26.4% |
| 2011 | +11.8% | +1.9% | +9.9% |
| 2012 | +15.2% | +16.0% | -0.8% |
| 2013 | +35.5% | +32.3% | +3.2% |
| 2014 | +15.1% | +13.5% | +1.7% |
| 2015 | -15.6% | +1.2% | -16.8% |
| 2016 | +23.4% | +12.0% | +11.4% |
| 2017 | +9.6% | +21.7% | -12.1% |
| 2018 | -18.5% | -4.6% | -14.0% |
| 2019 | +15.0% | +31.2% | -16.2% |
| 2020 | +28.3% | +18.3% | +10.0% |
| 2021 | +6.0% | +28.7% | -22.7% |
| 2022 | -24.5% | -18.2% | -6.3% |
| 2023 | +23.8% | +26.2% | -2.4% |
| 2024 | +8.1% | +24.9% | -16.8% |
| 2025 | +21.4% | +17.7% | +3.6% |
| 2026 | +18.0% | +8.2% | +9.7% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 101 | +1.3% | +1.7% | 64% |
| 21 sessions | 8 | -1.1% | +6.1% | 75% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-18 | [[LEO]] | [[Saba Capital Management, L.P]] | $204K | 23 | – | pending |
| 2026-11-18 | [[HFRO]] | [[Saba Capital Management, L.P]] | $1.3M | 35 | – | pending |
| 2026-11-18 | [[ECC]] | [[Majewski Thomas P]] | $118K | 68 | – | pending |
| 2026-11-18 | [[GLP]] | [[Global GP LLC]] | $312K | 25 | – | pending |
| 2026-11-18 | [[SJT]] | [[OLIVER ERIC L]] | $2.6M | 41 | – | pending |
| 2026-11-18 | [[FRPH]] | [[BAKER JOHN D II]] | $96K | 20 | – | pending |
| 2026-11-18 | [[CCAP]] | [[Breaux Jason]] | $50K | 41 | – | pending |
| 2026-11-18 | [[CCAP]] | [[Lombard Gerhard]] | $20K | 43 | – | pending |
| 2026-11-18 | [[SLRC]] | [[GROSS MICHAEL S]] | $226K | 30 | – | pending |
| 2026-11-18 | [[FFIN]] | [[Davis Sally Pope]] | $51K | 29 | – | pending |
| 2026-11-18 | [[EFC]] | [[Penn Laurence]] | $107K | 44 | – | pending |
| 2026-11-18 | [[RILY]] | [[RILEY BRYANT R]] | $117K | 38 | – | pending |
| 2026-11-18 | [[DGICA]] | [[DONEGAL MUTUAL INSURANCE CO]] | $263K | 23 | – | pending |
| 2026-11-18 | [[TSM]] | [[BURNS URSULA M]] | $500K | 60 | – | pending |
| 2026-11-17 | [[HFRO]] | [[Saba Capital Management, L.P]] | $6K | 8 | +1.6% | open |
| 2026-11-17 | [[JOF]] | [[Saba Capital Management, L.P]] | $6K | 8 | -0.4% | open |
| 2026-11-17 | [[BOLT]] | [[Coastlands Capital LP]] | $310K | 32 | -9.0% | open |
| 2026-11-17 | [[LEO]] | [[Saba Capital Management, L.P]] | $272K | 25 | -0.1% | open |
| 2026-11-17 | [[ECC]] | [[Onorio Kenneth P]] | $104K | 45 | +0.4% | open |
| 2026-11-17 | [[STUB]] | [[Raab Andrew John]] | $2.0M | 67 | +0.4% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "proven_insider")
SORT filed DESC
```

Back to [[What Works]].
