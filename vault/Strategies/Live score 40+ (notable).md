---
type: "strategy"
key: "score_40"
signals: 32319
cagr: 0.0600963
spy_cagr: 0.110756
sharpe: 0.288261
max_drawdown: 0.574297
holdout_excess: 0.0154221
---

# Live score 40+ (notable)

Rule key: `score_40`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 32,319 |
| 3-month excess vs SPY (mean / median) | +1.1% / -0.6% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.8% |
| vs surviving stocks | +1.2% |
| 2006-2015 excess /yr | +8.0% (p 0.010) |
| 2016+ excess /yr | +1.5% (p 0.714) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.6% | +11.1% | 0.31 | 0.56 | 59% | 1.26 | -4.7% | 33% | 4,873 | 8.6% | -0.9% / -0.12 / 59% |
| 63d | +6.0% | +11.1% | 0.29 | 0.56 | 57% | 1.24 | -5.2% | 38% | 1,660 | 2.6% | -1.9% / -0.19 / 57% |
| 126d | +5.1% | +11.1% | 0.26 | 0.56 | 68% | 1.19 | -5.7% | 33% | 840 | 1.4% | -2.9% / -0.27 / 57% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +8.8%/yr, double costs +3.3%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +12.7% | +13.8% | -1.1% |
| 2007 | -11.1% | +5.1% | -16.2% |
| 2008 | -19.3% | -36.8% | +17.5% |
| 2009 | +36.1% | +26.4% | +9.7% |
| 2010 | +31.8% | +15.1% | +16.8% |
| 2011 | -13.7% | +1.9% | -15.6% |
| 2012 | +22.0% | +16.0% | +6.0% |
| 2013 | +35.5% | +32.3% | +3.2% |
| 2014 | +0.7% | +13.5% | -12.8% |
| 2015 | -10.7% | +1.2% | -11.9% |
| 2016 | +21.1% | +12.0% | +9.1% |
| 2017 | +19.2% | +21.7% | -2.5% |
| 2018 | -19.6% | -4.6% | -15.0% |
| 2019 | +45.6% | +31.2% | +14.4% |
| 2020 | +10.3% | +18.3% | -8.1% |
| 2021 | +3.2% | +28.7% | -25.6% |
| 2022 | -20.4% | -18.2% | -2.3% |
| 2023 | +30.0% | +26.2% | +3.8% |
| 2024 | -10.3% | +24.9% | -35.2% |
| 2025 | -7.5% | +17.7% | -25.2% |
| 2026 | +9.3% | +13.7% | -4.5% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 18 | -3.3% | -1.7% | 22% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-30 | [[RAPP]] | [[HEALY JAMES]] | $20.4M | 87 | – | pending |
| 2026-10-30 | [[FFIN]] | [[Denny Michael B]] | $100K | 42 | – | pending |
| 2026-10-30 | [[BBT]] | [[Charnley Nina A]] | $11K | 57 | – | pending |
| 2026-10-29 | [[DINO]] | [[MYERS FRANKLIN]] | $1.1M | 52 | +1.8% | open |
| 2026-10-29 | [[PNFP]] | [[INGRAM DAVID B]] | $992K | 43 | -0.6% | open |
| 2026-10-29 | [[HBAN]] | [[TORGOW GARY]] | $200K | 40 | -0.7% | open |
| 2026-10-29 | [[XYL]] | [[KOCH D CHRISTIAN]] | $986K | 52 | +1.1% | open |
| 2026-10-29 | [[NPB]] | [[Chaudhary Rajeev Kumar]] | $47K | 64 | -2.3% | open |
| 2026-10-29 | [[TFC]] | [[Lyons Michael P]] | $1.2M | 66 | -0.8% | open |
| 2026-10-29 | [[BBT]] | [[Callahan Mary Anne]] | $97K | 54 | -0.4% | open |
| 2026-10-28 | [[TTMI]] | [[Roks Edwin]] | $440K | 62 | -6.8% | open |
| 2026-10-28 | [[TTMI]] | [[Ali Wajid]] | $902K | 61 | -6.8% | open |
| 2026-10-28 | [[BPRE]] | [[KAMFAR RAMIN]] | $2.2M | 55 | +1.5% | open |
| 2026-10-28 | [[GOLD]] | [[Tether Global Investments Fund, S.I.C.A.F., S.A]] | $3.9M | 48 | -2.0% | open |
| 2026-10-28 | [[HXL]] | [[KEATING NEAL J]] | $242K | 46 | -0.5% | open |
| 2026-10-28 | [[BBT]] | [[Polito Karyn]] | $31K | 49 | +0.6% | open |
| 2026-10-28 | [[WS]] | [[Ganem George John III]] | $31K | 40 | -4.0% | open |
| 2026-10-28 | [[BBT]] | [[Rosengren Eric S]] | $21K | 44 | +0.6% | open |
| 2026-10-28 | [[HBAN]] | [[ROLLINS JAMES D III]] | $254K | 46 | +0.6% | open |
| 2026-10-28 | [[ACN]] | [[Sweet Julie Spellman]] | $3.0M | 78 | +9.6% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_40")
SORT filed DESC
```

Back to [[What Works]].
