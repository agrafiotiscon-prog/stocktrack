---
type: "strategy"
key: "big_stake_up"
signals: 11413
cagr: 0.0892515
spy_cagr: 0.107784
sharpe: 0.388164
max_drawdown: 0.669115
holdout_excess: 0.0172159
---

# Exec/director growing stake 25%+ with $100K+

Rule key: `big_stake_up`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 11,413 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.5% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.5% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +6.3% (p 0.035) |
| 2016+ excess /yr | +1.7% (p 0.668) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.6% | +10.8% | 0.20 | 0.54 | 54% | 1.05 | -6.1% | 19% | 4,269 | 6.3% | -2.2% / -0.26 / 52% |
| 63d | +8.9% | +10.8% | 0.39 | 0.54 | 67% | 1.29 | -2.8% | 52% | 1,657 | 2.7% | +0.8% / -0.00 / 36% |
| 126d | +7.6% | +10.8% | 0.34 | 0.54 | 66% | 1.26 | -3.8% | 48% | 840 | 1.3% | -0.2% / -0.08 / 47% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +11.6%/yr, double costs +6.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +14.2% | +13.8% | +0.3% |
| 2007 | -5.6% | +5.1% | -10.8% |
| 2008 | -43.3% | -36.8% | -6.5% |
| 2009 | +57.3% | +26.4% | +30.9% |
| 2010 | +35.2% | +15.1% | +20.1% |
| 2011 | +3.3% | +1.9% | +1.4% |
| 2012 | +17.9% | +16.0% | +1.9% |
| 2013 | +50.3% | +32.3% | +17.9% |
| 2014 | +17.2% | +13.5% | +3.8% |
| 2015 | -6.5% | +1.2% | -7.7% |
| 2016 | +17.1% | +12.0% | +5.1% |
| 2017 | +17.5% | +21.7% | -4.2% |
| 2018 | -16.8% | -4.6% | -12.2% |
| 2019 | +48.2% | +31.2% | +16.9% |
| 2020 | +21.5% | +18.3% | +3.2% |
| 2021 | -6.3% | +28.7% | -35.1% |
| 2022 | -16.6% | -18.2% | +1.6% |
| 2023 | +20.4% | +26.2% | -5.8% |
| 2024 | +5.8% | +24.9% | -19.1% |
| 2025 | +11.7% | +17.7% | -6.0% |
| 2026 | -0.6% | +8.2% | -8.9% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 58 | +0.7% | +0.6% | 55% |
| 21 sessions | 1 | -8.5% | -8.5% | 0% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-18 | [[TSM]] | [[BURNS URSULA M]] | $500K | 60 | – | pending |
| 2026-11-17 | [[RMIX]] | [[Fleming Ned N III]] | $238K | 46 | – | pending |
| 2026-11-17 | [[STUB]] | [[Bhargava Sameer]] | $1.5M | 66 | – | pending |
| 2026-11-17 | [[STUB]] | [[Raab Andrew John]] | $2.0M | 67 | – | pending |
| 2026-11-17 | [[PRAA]] | [[FREDRICKSON STEVEN D]] | $295K | 57 | – | pending |
| 2026-11-17 | [[UPST]] | [[Gu Paul]] | $950K | 60 | – | pending |
| 2026-11-17 | [[ITG]] | [[Giacalone Peter]] | $509K | 69 | – | pending |
| 2026-11-17 | [[ANGX]] | [[Sarowitz Steven I]] | $4.6M | 59 | – | pending |
| 2026-11-17 | [[PEPG]] | [[RA CAPITAL MANAGEMENT, L.P]] | $43.1M | 61 | – | pending |
| 2026-11-17 | [[HNRG]] | [[Wesley Charles Ray IV]] | $1.1M | 48 | – | pending |
| 2026-11-16 | [[SKYD]] | [[Cardinale Gerald J]] | $1.0M | 52 | -0.9% | open |
| 2026-11-16 | [[KTOS]] | [[King David Arnold]] | $201K | 45 | -1.2% | open |
| 2026-11-16 | [[KURA]] | [[WILSON TROY EDWARD]] | $1.5M | 66 | -1.7% | open |
| 2026-11-16 | [[HL]] | [[Andres Dale]] | $125K | 43 | +1.0% | open |
| 2026-11-16 | [[FPS]] | [[Hottinger Tyson]] | $245K | 77 | -0.6% | open |
| 2026-11-16 | [[BRK-B]] | [[O'Sullivan Michael J]] | $250K | 45 | +0.3% | open |
| 2026-11-16 | [[CNH]] | [[Simonelli Lorenzo]] | $567K | 50 | -0.6% | open |
| 2026-11-16 | [[AMG]] | [[Cates G. Staley]] | $1.0M | 50 | -0.5% | open |
| 2026-11-16 | [[CTVA]] | [[PAGE GREGORY R]] | $185K | 57 | -3.8% | open |
| 2026-11-16 | [[NSLR]] | [[Klein Mark D]] | $994K | 85 | -0.8% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "big_stake_up")
SORT filed DESC
```

Back to [[What Works]].
