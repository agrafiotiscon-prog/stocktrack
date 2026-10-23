---
type: "strategy"
key: "proven_insider"
signals: 20153
cagr: 0.10422
spy_cagr: 0.112598
sharpe: 0.444537
max_drawdown: 0.609637
holdout_excess: 0.00621904
---

# Insiders whose earlier buys beat SPY

Rule key: `proven_insider`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 20,153 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +0.6% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +5.8% (p 0.023) |
| 2016+ excess /yr | +0.6% (p 0.850) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +8.1% | +11.3% | 0.37 | 0.56 | 52% | 1.10 | -2.8% | 24% | 4,539 | 8.7% | +0.1% / -0.09 / 43% |
| 63d | +10.4% | +11.3% | 0.44 | 0.56 | 61% | 1.20 | -1.2% | 43% | 1,613 | 3.1% | +2.1% / 0.09 / 34% |
| 126d | +9.3% | +11.3% | 0.41 | 0.56 | 56% | 1.10 | -1.5% | 43% | 817 | 1.6% | +0.7% / -0.02 / 35% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +14.1%/yr, double costs +7.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.1% | +13.0% | +3.1% |
| 2007 | -0.0% | +5.1% | -5.1% |
| 2008 | -20.0% | -36.8% | +16.8% |
| 2009 | +15.4% | +26.4% | -11.0% |
| 2010 | +44.4% | +15.1% | +29.3% |
| 2011 | +4.5% | +1.9% | +2.6% |
| 2012 | +25.5% | +16.0% | +9.5% |
| 2013 | +38.7% | +32.3% | +6.4% |
| 2014 | +18.2% | +13.5% | +4.7% |
| 2015 | -13.0% | +1.2% | -14.2% |
| 2016 | +17.3% | +12.0% | +5.3% |
| 2017 | +18.2% | +21.7% | -3.6% |
| 2018 | -14.3% | -4.6% | -9.7% |
| 2019 | +26.6% | +31.2% | -4.7% |
| 2020 | +22.2% | +18.3% | +3.9% |
| 2021 | +5.4% | +28.7% | -23.3% |
| 2022 | -20.5% | -18.2% | -2.4% |
| 2023 | +25.9% | +26.2% | -0.2% |
| 2024 | +21.4% | +24.9% | -3.5% |
| 2025 | +15.7% | +17.7% | -2.0% |
| 2026 | -4.4% | +13.7% | -18.0% |


## Live forward test

8 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-21 | [[LEO]] | [[Saba Capital Management, L.P]] | $44K | 15 | – | pending |
| 2026-10-21 | [[DX]] | [[BOSTON BYRON L]] | $100K | 50 | – | pending |
| 2026-10-21 | [[DSM]] | [[Saba Capital Management, L.P]] | $78K | 18 | – | pending |
| 2026-10-20 | [[DX]] | [[Popenoe Smriti Laxman]] | $106K | 39 | -1.1% | open |
| 2026-10-20 | [[LEO]] | [[Saba Capital Management, L.P]] | $1.9M | 37 | -1.3% | open |
| 2026-10-20 | [[AYI]] | [[O'Shaughnessy Laura]] | $22K | 20 | +3.0% | open |
| 2026-10-20 | [[DSM]] | [[Saba Capital Management, L.P]] | $1.1M | 34 | -0.8% | open |
| 2026-10-20 | [[NXG]] | [[Sunderland Todd]] | $46K | 26 | -0.4% | open |
| 2026-10-20 | [[XGN]] | [[Chernett Jorey]] | $104K | 20 | +5.4% | open |
| 2026-10-19 | [[DSM]] | [[Saba Capital Management, L.P]] | $72K | 18 | -0.6% | open |
| 2026-10-19 | [[EQBK]] | [[Borck Leon]] | $19K | 16 | -0.9% | open |
| 2026-10-19 | [[APLD]] | [[Cummins Wes]] | $1.0M | 60 | +11.8% | open |
| 2026-10-16 | [[SAH]] | [[Rusnak Paul P]] | $752K | 28 | -6.8% | open |
| 2026-10-16 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | -2.5% | open |
| 2026-10-13 | [[GME]] | [[Cohen Ryan]] | $22.8M | 71 | -4.9% | open |
| 2026-10-13 | [[HEI]] | [[CULLIGAN THOMAS M]] | $175K | 57 | +0.6% | open |
| 2026-10-13 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | +1.0% | open |
| 2026-10-13 | [[HEI]] | [[Hildebrandt Mark H]] | $175K | 53 | +0.6% | open |
| 2026-10-13 | [[HEI]] | [[SCHRIESHEIM ALAN]] | $175K | 69 | +0.6% | open |
| 2026-10-13 | [[HEI]] | [[HENRIQUES ADOLFO]] | $175K | 55 | +0.6% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "proven_insider")
SORT filed DESC
```

Back to [[What Works]].
