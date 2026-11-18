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
| 5 sessions | 33 | +1.6% | +1.8% | 67% |
| 21 sessions | 1 | +4.6% | +4.6% | 100% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-17 | [[MP]] | [[Corbett Ryan]] | $92K | 56 | – | pending |
| 2026-11-17 | [[ITG]] | [[Parrott Andrew]] | $98K | 75 | – | pending |
| 2026-11-17 | [[ITG]] | [[Braun III Francis A]] | $19K | 58 | – | pending |
| 2026-11-17 | [[ITG]] | [[Giacalone Peter]] | $509K | 69 | – | pending |
| 2026-11-17 | [[ITG]] | [[LAPERCH WILLIAM G]] | $50K | 59 | – | pending |
| 2026-11-17 | [[TH]] | [[PATENAUDE PAMELA H]] | $46K | 45 | – | pending |
| 2026-11-17 | [[UPBD]] | [[Jain Charu]] | $49K | 64 | – | pending |
| 2026-11-17 | [[DKNG]] | [[Kalish Matthew]] | $1.0M | 55 | – | pending |
| 2026-11-17 | [[PAM]] | [[Mariani Gustavo]] | $169K | 56 | – | pending |
| 2026-11-17 | [[PAM]] | [[Mindlin Marcos Marcelo]] | $541K | 55 | – | pending |
| 2026-11-17 | [[NGS]] | [[Jacobs Justin]] | $86K | 64 | – | pending |
| 2026-11-17 | [[NGS]] | [[TRINGALI DONALD J]] | $49K | 54 | – | pending |
| 2026-11-17 | [[VISN]] | [[Gilstrap Charles A]] | $20K | 45 | – | pending |
| 2026-11-17 | [[BW]] | [[BRC Group Holdings, Inc]] | $212K | 66 | – | pending |
| 2026-11-16 | [[MP]] | [[Corbett Ryan]] | $129K | 58 | -4.3% | open |
| 2026-11-16 | [[ADIG]] | [[Carlet Michael]] | $100K | 71 | -4.0% | open |
| 2026-11-16 | [[ADIG]] | [[Cardazzi Marco]] | $25K | 61 | -4.0% | open |
| 2026-11-16 | [[ADIG]] | [[Lane Jeannine J]] | $50K | 57 | -4.0% | open |
| 2026-11-16 | [[ADIG]] | [[Aarnes Robert B]] | $100K | 68 | -4.0% | open |
| 2026-11-16 | [[ADIG]] | [[Copeland Alicia Crispin]] | $51K | 70 | -4.0% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "cluster_3")
SORT filed DESC
```

Back to [[What Works]].
