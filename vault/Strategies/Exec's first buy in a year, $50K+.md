---
type: "strategy"
key: "first_buy_exec"
signals: 5625
cagr: 0.0936239
spy_cagr: 0.10945
sharpe: 0.411933
max_drawdown: 0.54717
holdout_excess: 0.00634005
---

# Exec's first buy in a year, $50K+

Rule key: `first_buy_exec`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 5,625 |
| 3-month excess vs SPY (mean / median) | +1.4% / -0.3% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +1.0% |
| vs surviving stocks | +1.7% |
| 2006-2015 excess /yr | +11.4% (p 0.011) |
| 2016+ excess /yr | +0.6% (p 0.884) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.8% | +10.9% | 0.21 | 0.55 | 54% | 0.88 | -4.8% | 20% | 3,211 | 5.4% | -0.6% / -0.16 / 49% |
| 63d | +9.4% | +10.9% | 0.41 | 0.55 | 55% | 1.21 | -2.0% | 55% | 1,527 | 2.6% | +2.1% / 0.10 / 42% |
| 126d | +10.5% | +10.9% | 0.45 | 0.55 | 57% | 1.21 | -1.1% | 45% | 784 | 1.3% | +2.5% / 0.13 / 41% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +12.1%/yr, double costs +6.8%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2007 | +4.1% | +5.3% | -1.2% |
| 2008 | -29.1% | -36.8% | +7.7% |
| 2009 | +54.2% | +26.4% | +27.8% |
| 2010 | +25.5% | +15.1% | +10.4% |
| 2011 | -6.5% | +1.9% | -8.4% |
| 2012 | +30.1% | +16.0% | +14.1% |
| 2013 | +34.4% | +32.3% | +2.1% |
| 2014 | +6.6% | +13.5% | -6.9% |
| 2015 | +3.4% | +1.2% | +2.2% |
| 2016 | +1.3% | +12.0% | -10.7% |
| 2017 | +25.2% | +21.7% | +3.5% |
| 2018 | -5.8% | -4.6% | -1.3% |
| 2019 | +32.5% | +31.2% | +1.3% |
| 2020 | +29.1% | +18.3% | +10.7% |
| 2021 | -4.2% | +28.7% | -32.9% |
| 2022 | -5.6% | -18.2% | +12.5% |
| 2023 | +22.6% | +26.2% | -3.6% |
| 2024 | +31.0% | +24.9% | +6.1% |
| 2025 | -10.8% | +17.7% | -28.6% |
| 2026 | -13.6% | +13.7% | -27.4% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 4 | -5.9% | -2.6% | 0% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-29 | [[UTMD]] | [[CORNWELL KEVIN L]] | $67K | 35 | – | pending |
| 2026-10-28 | [[ACN]] | [[Sweet Julie Spellman]] | $3.0M | 78 | +3.2% | open |
| 2026-10-27 | [[STC]] | [[EPPINGER FREDERICK H]] | $133K | 65 | +3.8% | open |
| 2026-10-27 | [[TIPT]] | [[Barnes Michael Gene]] | $502K | 29 | +3.1% | open |
| 2026-10-27 | [[KIO]] | [[Takao Justin]] | $78K | 51 | +2.2% | open |
| 2026-10-26 | [[THRM]] | [[Presley William T]] | $130K | 53 | +7.8% | open |
| 2026-10-21 | [[RAPP]] | [[Ignelzi Troy A]] | $144K | 54 | -7.9% | open |
| 2026-10-21 | [[CRF]] | [[Bradshaw Joshua]] | $118K | 53 | -0.6% | open |
| 2026-10-21 | [[CLM]] | [[Bradshaw Joshua]] | $97K | 52 | -2.7% | open |
| 2026-10-21 | [[DX]] | [[BOSTON BYRON L]] | $100K | 50 | -0.8% | open |
| 2026-10-19 | [[APLD]] | [[Cummins Wes]] | $1.0M | 60 | +3.9% | open |
| 2026-10-19 | [[APLD]] | [[Zhang Jason Gechen]] | $5.7M | 71 | +3.9% | open |
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | $1.5M | 72 | -7.4% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -3.1% | open |
| 2026-10-14 | [[IMSR]] | [[Irish Simon]] | $51K | 46 | +20.4% | open |
| 2026-10-13 | [[RTSN]] | [[Keller Eric L]] | $250K | 57 | +2.4% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | -6.3% | open |
| 2026-10-08 | [[IMMR]] | [[Singer Eric]] | $293K | 44 | +1.5% | open |
| 2026-10-07 | [[AGMB]] | [[Knotnerus Tim Jasper]] | $94K | 67 | -9.8% | open |
| 2026-10-06 | [[HRL]] | [[Newlands William A]] | $201K | 46 | +6.2% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "first_buy_exec")
SORT filed DESC
```

Back to [[What Works]].
