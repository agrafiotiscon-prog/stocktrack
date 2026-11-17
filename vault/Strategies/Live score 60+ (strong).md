---
type: "strategy"
key: "score_60"
signals: 7191
cagr: 0.106573
spy_cagr: 0.108918
sharpe: 0.443859
max_drawdown: 0.612357
holdout_excess: 0.0176435
---

# Live score 60+ (strong)

Rule key: `score_60`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,191 |
| 3-month excess vs SPY (mean / median) | +1.6% / -0.6% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +1.3% |
| vs surviving stocks | +1.8% |
| 2006-2015 excess /yr | +6.7% (p 0.104) |
| 2016+ excess /yr | +1.8% (p 0.740) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.7% | +10.9% | 0.24 | 0.55 | 62% | 0.93 | -3.9% | 29% | 3,301 | 6.2% | +0.3% / -0.05 / 59% |
| 63d | +10.7% | +10.9% | 0.44 | 0.55 | 61% | 1.21 | -0.4% | 57% | 1,587 | 2.9% | +3.0% / 0.16 / 31% |
| 126d | +11.5% | +10.9% | 0.47 | 0.55 | 65% | 1.11 | +1.0% | 57% | 823 | 1.6% | +3.5% / 0.19 / 41% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +13.7%/yr, double costs +7.8%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +14.4% | +13.3% | +1.1% |
| 2007 | -11.8% | +5.1% | -16.9% |
| 2008 | -29.0% | -36.8% | +7.8% |
| 2009 | +41.3% | +26.4% | +14.9% |
| 2010 | +29.0% | +15.1% | +13.9% |
| 2011 | -2.9% | +1.9% | -4.8% |
| 2012 | +14.5% | +16.0% | -1.4% |
| 2013 | +48.3% | +32.3% | +16.0% |
| 2014 | +7.4% | +13.5% | -6.1% |
| 2015 | -12.7% | +1.2% | -13.9% |
| 2016 | +28.9% | +12.0% | +16.9% |
| 2017 | +28.0% | +21.7% | +6.3% |
| 2018 | -10.8% | -4.6% | -6.3% |
| 2019 | +47.3% | +31.2% | +16.1% |
| 2020 | +18.4% | +18.3% | +0.1% |
| 2021 | -1.5% | +28.7% | -30.2% |
| 2022 | -7.0% | -18.2% | +11.2% |
| 2023 | +34.4% | +26.2% | +8.3% |
| 2024 | +2.3% | +24.9% | -22.6% |
| 2025 | +23.2% | +17.7% | +5.5% |
| 2026 | +2.3% | +10.8% | -8.5% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 40 | +0.8% | +1.3% | 60% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-17 | [[BW]] | [[BRC Group Holdings, Inc]] | $212K | 66 | – | pending |
| 2026-11-16 | [[MX]] | [[LEE CHAE]] | $218K | 63 | – | pending |
| 2026-11-16 | [[KURA]] | [[WILSON TROY EDWARD]] | $1.5M | 66 | – | pending |
| 2026-11-16 | [[ADIG]] | [[Carlet Michael]] | $100K | 71 | – | pending |
| 2026-11-16 | [[ADIG]] | [[Cardazzi Marco]] | $25K | 61 | – | pending |
| 2026-11-16 | [[ADIG]] | [[Aarnes Robert B]] | $100K | 68 | – | pending |
| 2026-11-16 | [[ADIG]] | [[Copeland Alicia Crispin]] | $51K | 70 | – | pending |
| 2026-11-16 | [[FPS]] | [[Hottinger Tyson]] | $245K | 77 | – | pending |
| 2026-11-16 | [[FPS]] | [[Bhatia Neel]] | $199K | 61 | – | pending |
| 2026-11-16 | [[FPS]] | [[Niederpruem Gary John]] | $334K | 77 | – | pending |
| 2026-11-16 | [[FPS]] | [[Ard Amy E]] | $300K | 75 | – | pending |
| 2026-11-16 | [[CTVA]] | [[KISSAM LUTHER C IV]] | $300K | 65 | – | pending |
| 2026-11-16 | [[NSLR]] | [[Klein Mark D]] | $994K | 85 | – | pending |
| 2026-11-16 | [[FF]] | [[KRUSZEWSKI RONALD J]] | $284K | 72 | – | pending |
| 2026-11-16 | [[DOX]] | [[Gardner Adrian]] | $215K | 64 | – | pending |
| 2026-11-16 | [[GOOD]] | [[Cooper Arthur S]] | $100K | 60 | – | pending |
| 2026-11-16 | [[CSQR]] | [[PIZZUTO TERRI]] | $34K | 62 | – | pending |
| 2026-11-16 | [[HUBS]] | [[Halligan Brian]] | $5.0M | 70 | – | pending |
| 2026-11-13 | [[STWD]] | [[Pollack Jonathan Lee]] | $2.0M | 67 | +1.3% | open |
| 2026-11-13 | [[STWD]] | [[STERNLICHT BARRY S]] | $14.7M | 87 | +1.3% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_60")
SORT filed DESC
```

Back to [[What Works]].
