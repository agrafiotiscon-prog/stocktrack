---
type: "strategy"
key: "score_60"
signals: 7212
cagr: 0.105251
spy_cagr: 0.107555
sharpe: 0.439872
max_drawdown: 0.612357
holdout_excess: 0.0166326
---

# Live score 60+ (strong)

Rule key: `score_60`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,212 |
| 3-month excess vs SPY (mean / median) | +1.5% / -0.7% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +1.3% |
| vs surviving stocks | +1.7% |
| 2006-2015 excess /yr | +6.8% (p 0.101) |
| 2016+ excess /yr | +1.7% (p 0.754) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.3% | +10.8% | 0.22 | 0.54 | 63% | 0.92 | -4.2% | 33% | 3,303 | 6.1% | +0.0% / -0.08 / 59% |
| 63d | +10.5% | +10.8% | 0.44 | 0.54 | 61% | 1.22 | -0.4% | 52% | 1,590 | 2.9% | +3.0% / 0.16 / 31% |
| 126d | +12.2% | +10.8% | 0.50 | 0.54 | 63% | 1.12 | +1.7% | 57% | 825 | 1.6% | +4.3% / 0.25 / 44% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +13.6%/yr, double costs +7.6%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.4% | +13.3% | +3.1% |
| 2007 | -11.8% | +5.1% | -16.9% |
| 2008 | -29.0% | -36.8% | +7.8% |
| 2009 | +41.3% | +26.4% | +14.9% |
| 2010 | +30.2% | +15.1% | +15.1% |
| 2011 | -0.5% | +1.9% | -2.4% |
| 2012 | +13.4% | +16.0% | -2.6% |
| 2013 | +48.3% | +32.3% | +16.0% |
| 2014 | +6.1% | +13.5% | -7.3% |
| 2015 | -12.7% | +1.2% | -13.9% |
| 2016 | +28.9% | +12.0% | +16.9% |
| 2017 | +28.0% | +21.7% | +6.3% |
| 2018 | -10.8% | -4.6% | -6.3% |
| 2019 | +47.2% | +31.2% | +16.0% |
| 2020 | +16.2% | +18.3% | -2.2% |
| 2021 | -1.8% | +28.7% | -30.5% |
| 2022 | -6.9% | -18.2% | +11.3% |
| 2023 | +35.5% | +26.2% | +9.3% |
| 2024 | +1.6% | +24.9% | -23.3% |
| 2025 | +19.6% | +17.7% | +1.9% |
| 2026 | +2.2% | +8.2% | -6.1% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 45 | +0.2% | +1.1% | 60% |
| 21 sessions | 2 | -1.9% | +4.6% | 50% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-18 | [[TSM]] | [[BURNS URSULA M]] | $500K | 60 | – | pending |
| 2026-11-17 | [[STUB]] | [[Bhargava Sameer]] | $1.5M | 66 | – | pending |
| 2026-11-17 | [[STUB]] | [[Raab Andrew John]] | $2.0M | 67 | – | pending |
| 2026-11-17 | [[UPST]] | [[Gu Paul]] | $950K | 60 | – | pending |
| 2026-11-17 | [[ITG]] | [[Parrott Andrew]] | $98K | 75 | – | pending |
| 2026-11-17 | [[ITG]] | [[Giacalone Peter]] | $509K | 69 | – | pending |
| 2026-11-17 | [[UPBD]] | [[Jain Charu]] | $49K | 64 | – | pending |
| 2026-11-17 | [[PEPG]] | [[RA CAPITAL MANAGEMENT, L.P]] | $43.1M | 61 | – | pending |
| 2026-11-17 | [[NGS]] | [[Jacobs Justin]] | $86K | 64 | – | pending |
| 2026-11-17 | [[BW]] | [[BRC Group Holdings, Inc]] | $212K | 66 | – | pending |
| 2026-11-16 | [[MX]] | [[LEE CHAE]] | $218K | 63 | -2.9% | open |
| 2026-11-16 | [[KURA]] | [[WILSON TROY EDWARD]] | $1.5M | 66 | -1.7% | open |
| 2026-11-16 | [[ADIG]] | [[Carlet Michael]] | $100K | 71 | -4.0% | open |
| 2026-11-16 | [[ADIG]] | [[Cardazzi Marco]] | $25K | 61 | -4.0% | open |
| 2026-11-16 | [[ADIG]] | [[Aarnes Robert B]] | $100K | 68 | -4.0% | open |
| 2026-11-16 | [[ADIG]] | [[Copeland Alicia Crispin]] | $51K | 70 | -4.0% | open |
| 2026-11-16 | [[FPS]] | [[Hottinger Tyson]] | $245K | 77 | -0.6% | open |
| 2026-11-16 | [[FPS]] | [[Bhatia Neel]] | $199K | 61 | -0.6% | open |
| 2026-11-16 | [[FPS]] | [[Niederpruem Gary John]] | $334K | 77 | -0.6% | open |
| 2026-11-16 | [[FPS]] | [[Ard Amy E]] | $300K | 75 | -0.6% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_60")
SORT filed DESC
```

Back to [[What Works]].
