---
type: "strategy"
key: "cluster_3"
signals: 7434
cagr: 0.058292
spy_cagr: 0.108918
sharpe: 0.282277
max_drawdown: 0.592749
holdout_excess: 0.00686121
---

# 3+ insiders buying within 14 days

Rule key: `cluster_3`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,434 |
| 3-month excess vs SPY (mean / median) | +2.1% / +0.0% |
| Beat SPY over 3 months | 50% |
| Entering one session later | +2.0% |
| vs surviving stocks | +2.0% |
| 2006-2015 excess /yr | +8.4% (p 0.039) |
| 2016+ excess /yr | +0.7% (p 0.895) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.4% | +10.9% | 0.32 | 0.55 | 52% | 0.75 | -1.1% | 24% | 2,854 | 6.0% | +1.8% / 0.06 / 35% |
| 63d | +5.8% | +10.9% | 0.28 | 0.55 | 59% | 1.13 | -4.5% | 33% | 1,542 | 2.9% | -1.3% / -0.14 / 55% |
| 126d | +11.2% | +10.9% | 0.46 | 0.55 | 66% | 1.14 | +0.5% | 48% | 821 | 1.6% | +3.4% / 0.18 / 40% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +8.9%/yr, double costs +2.9%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +15.9% | +13.3% | +2.6% |
| 2007 | -8.7% | +5.1% | -13.9% |
| 2008 | -27.5% | -36.8% | +9.3% |
| 2009 | +27.1% | +26.4% | +0.7% |
| 2010 | +30.2% | +15.1% | +15.1% |
| 2011 | -2.6% | +1.9% | -4.5% |
| 2012 | +25.6% | +16.0% | +9.6% |
| 2013 | +30.0% | +32.3% | -2.4% |
| 2014 | +2.0% | +13.5% | -11.4% |
| 2015 | -10.5% | +1.2% | -11.8% |
| 2016 | +26.4% | +12.0% | +14.4% |
| 2017 | +18.8% | +21.7% | -2.9% |
| 2018 | -15.3% | -4.6% | -10.7% |
| 2019 | +19.5% | +31.2% | -11.7% |
| 2020 | +35.1% | +18.3% | +16.7% |
| 2021 | +8.5% | +28.7% | -20.2% |
| 2022 | -38.0% | -18.2% | -19.8% |
| 2023 | +15.6% | +26.2% | -10.6% |
| 2024 | +3.6% | +24.9% | -21.3% |
| 2025 | +6.3% | +17.7% | -11.4% |
| 2026 | +0.4% | +10.8% | -10.4% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 19 | +1.2% | +1.5% | 63% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-12 | [[MP]] | [[Rosenthal Michael Stuart]] | $1.2M | 63 | – | pending |
| 2026-11-12 | [[MP]] | [[WEISENBURGER RANDALL J]] | $2.0M | 72 | – | pending |
| 2026-11-12 | [[MP]] | [[Corbett Ryan]] | $199K | 61 | – | pending |
| 2026-11-12 | [[GSM]] | [[Girardeau David Marie, Gabriel]] | $41K | 55 | – | pending |
| 2026-11-12 | [[GSM]] | [[CROCKETT BRUCE LARMOUR]] | $21K | 52 | – | pending |
| 2026-11-12 | [[GSM]] | [[Lopez Madrid Javier]] | $75K | 66 | – | pending |
| 2026-11-12 | [[GSM]] | [[Levi Marco]] | $51K | 56 | – | pending |
| 2026-11-10 | [[FUN]] | [[JAFFER REHAN]] | $14.9M | 77 | -0.2% | open |
| 2026-11-10 | [[FUN]] | [[HADDRILL RICHARD M]] | $91K | 57 | -0.2% | open |
| 2026-11-10 | [[UPBD]] | [[Young Scott A]] | $150K | 75 | +1.6% | open |
| 2026-11-10 | [[MTDR]] | [[Ehrman Monika U]] | $17K | 42 | +1.3% | open |
| 2026-11-10 | [[LBTYA]] | [[MALONE JOHN C]] | $1.5M | 53 | +4.2% | open |
| 2026-11-09 | [[MTDR]] | [[Stetson Glenn W]] | $51K | 53 | +5.0% | open |
| 2026-11-09 | [[MTDR]] | [[Appel Shelley F]] | $68K | 60 | +5.0% | open |
| 2026-11-09 | [[OBIO]] | [[Fain Eric S]] | $100K | 55 | +1.5% | open |
| 2026-11-09 | [[OBIO]] | [[Pacitti David]] | $100K | 59 | +1.5% | open |
| 2026-11-09 | [[OBIO]] | [[Hochman David P]] | $25K | 41 | +1.5% | open |
| 2026-11-09 | [[OBIO]] | [[Taylor Andrew Lawrence]] | $5K | 48 | +1.5% | open |
| 2026-11-09 | [[FLOC]] | [[Chmelev Alexander]] | $13K | 38 | -2.1% | open |
| 2026-11-09 | [[UPBD]] | [[Karam Fahmi]] | $300K | 71 | -0.1% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "cluster_3")
SORT filed DESC
```

Back to [[What Works]].
