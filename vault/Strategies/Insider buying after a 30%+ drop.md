---
type: "strategy"
key: "contrarian"
signals: 8184
cagr: 0.0164114
spy_cagr: 0.107169
sharpe: 0.173855
max_drawdown: 0.72189
holdout_excess: -0.0580197
---

# Insider buying after a 30%+ drop

Rule key: `contrarian`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 8,184 |
| 3-month excess vs SPY (mean / median) | +5.2% / +2.0% |
| Beat SPY over 3 months | 53% |
| Entering one session later | +4.7% |
| vs surviving stocks | +3.8% |
| 2006-2015 excess /yr | +14.0% (p 0.144) |
| 2016+ excess /yr | -5.8% (p 0.408) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +1.9% | +10.7% | 0.16 | 0.54 | 72% | 1.14 | -7.2% | 33% | 2,247 | 6.1% | +0.6% / 0.02 / 69% |
| 63d | +1.6% | +10.7% | 0.17 | 0.54 | 72% | 1.57 | -9.5% | 29% | 1,186 | 3.4% | -2.0% / -0.08 / 66% |
| 126d | +5.9% | +10.7% | 0.29 | 0.54 | 67% | 1.63 | -5.9% | 43% | 715 | 2.0% | +0.5% / 0.04 / 69% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +5.0%/yr, double costs -1.6%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +22.1% | +9.7% | +12.4% |
| 2007 | +6.6% | +5.1% | +1.4% |
| 2008 | -44.2% | -36.8% | -7.5% |
| 2009 | +25.0% | +26.4% | -1.4% |
| 2010 | +21.5% | +15.1% | +6.4% |
| 2011 | -8.2% | +1.9% | -10.1% |
| 2012 | +29.1% | +16.0% | +13.1% |
| 2013 | +24.0% | +32.3% | -8.3% |
| 2014 | -4.1% | +13.5% | -17.5% |
| 2015 | -21.6% | +1.2% | -22.8% |
| 2016 | +38.0% | +12.0% | +26.0% |
| 2017 | +15.0% | +21.7% | -6.7% |
| 2018 | -10.5% | -4.6% | -5.9% |
| 2019 | +34.4% | +31.2% | +3.2% |
| 2020 | +14.9% | +18.3% | -3.4% |
| 2021 | -7.5% | +28.7% | -36.2% |
| 2022 | -44.4% | -18.2% | -26.2% |
| 2023 | +11.6% | +26.2% | -14.5% |
| 2024 | -7.9% | +24.9% | -32.7% |
| 2025 | +4.6% | +17.7% | -13.1% |
| 2026 | -5.4% | +8.2% | -13.6% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 50 | -1.9% | +0.3% | 52% |
| 21 sessions | 1 | -35.6% | -35.6% | 0% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-17 | [[MP]] | [[Corbett Ryan]] | $92K | 56 | – | pending |
| 2026-11-17 | [[RMIX]] | [[Fleming Ned N III]] | $238K | 46 | – | pending |
| 2026-11-17 | [[RMIX]] | [[Wentroth Thomas G]] | $995 | 54 | – | pending |
| 2026-11-17 | [[ECC]] | [[Onorio Kenneth P]] | $104K | 45 | – | pending |
| 2026-11-17 | [[STUB]] | [[Bhargava Sameer]] | $1.5M | 66 | – | pending |
| 2026-11-17 | [[STUB]] | [[Raab Andrew John]] | $2.0M | 67 | – | pending |
| 2026-11-17 | [[FISN]] | [[JANOVER BLAKE]] | $11K | 44 | – | pending |
| 2026-11-17 | [[FISN]] | [[Peres Mark Wayne]] | $5K | 35 | – | pending |
| 2026-11-17 | [[FISN]] | [[Muller Richard]] | $32K | 43 | – | pending |
| 2026-11-17 | [[PRAA]] | [[FREDRICKSON STEVEN D]] | $295K | 57 | – | pending |
| 2026-11-17 | [[RDW]] | [[Cannito Peter Anthony Jr]] | $100K | 39 | – | pending |
| 2026-11-17 | [[NPCE]] | [[Williams Patrick F]] | $99K | 56 | – | pending |
| 2026-11-17 | [[NPCE]] | [[Becker Joel]] | $99K | 55 | – | pending |
| 2026-11-17 | [[UPST]] | [[Gu Paul]] | $950K | 60 | – | pending |
| 2026-11-17 | [[ITG]] | [[Parrott Andrew]] | $98K | 75 | – | pending |
| 2026-11-17 | [[ITG]] | [[Braun III Francis A]] | $19K | 58 | – | pending |
| 2026-11-17 | [[ITG]] | [[Giacalone Peter]] | $509K | 69 | – | pending |
| 2026-11-17 | [[ITG]] | [[LAPERCH WILLIAM G]] | $50K | 59 | – | pending |
| 2026-11-17 | [[UAMY]] | [[Bardswich Lloyd]] | $12K | 21 | – | pending |
| 2026-11-17 | [[GLXY]] | [[DEASON DOUGLAS R]] | $201K | 50 | – | pending |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "contrarian")
SORT filed DESC
```

Back to [[What Works]].
