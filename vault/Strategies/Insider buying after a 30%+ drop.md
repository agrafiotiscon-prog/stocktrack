---
type: "strategy"
key: "contrarian"
signals: 8130
cagr: 0.0198328
spy_cagr: 0.110174
sharpe: 0.183214
max_drawdown: 0.72189
holdout_excess: -0.0473747
---

# Insider buying after a 30%+ drop

Rule key: `contrarian`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 8,130 |
| 3-month excess vs SPY (mean / median) | +5.3% / +2.1% |
| Beat SPY over 3 months | 53% |
| Entering one session later | +4.8% |
| vs surviving stocks | +3.9% |
| 2006-2015 excess /yr | +12.9% (p 0.170) |
| 2016+ excess /yr | -4.7% (p 0.498) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +2.4% | +11.0% | 0.17 | 0.55 | 72% | 1.13 | -7.0% | 33% | 2,242 | 6.1% | +0.9% / 0.04 / 67% |
| 63d | +2.0% | +11.0% | 0.18 | 0.55 | 72% | 1.57 | -9.5% | 24% | 1,181 | 3.3% | -1.9% / -0.07 / 68% |
| 126d | +5.8% | +11.0% | 0.29 | 0.55 | 67% | 1.65 | -6.6% | 48% | 714 | 2.0% | +0.2% / 0.03 / 69% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +5.3%/yr, double costs -1.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +22.1% | +9.7% | +12.4% |
| 2007 | +6.6% | +5.1% | +1.4% |
| 2008 | -44.2% | -36.8% | -7.5% |
| 2009 | +25.0% | +26.4% | -1.4% |
| 2010 | +21.5% | +15.1% | +6.4% |
| 2011 | -8.2% | +1.9% | -10.1% |
| 2012 | +28.4% | +16.0% | +12.4% |
| 2013 | +26.1% | +32.3% | -6.2% |
| 2014 | -2.0% | +13.5% | -15.5% |
| 2015 | -21.6% | +1.2% | -22.8% |
| 2016 | +40.0% | +12.0% | +28.0% |
| 2017 | +15.0% | +21.7% | -6.7% |
| 2018 | -12.1% | -4.6% | -7.5% |
| 2019 | +30.5% | +31.2% | -0.7% |
| 2020 | +14.9% | +18.3% | -3.4% |
| 2021 | -10.2% | +28.7% | -38.9% |
| 2022 | -47.2% | -18.2% | -29.0% |
| 2023 | +10.3% | +26.2% | -15.9% |
| 2024 | -5.1% | +24.9% | -29.9% |
| 2025 | +4.6% | +17.7% | -13.1% |
| 2026 | +8.1% | +13.7% | -5.7% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 5 | -8.7% | -11.6% | 0% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-30 | [[RAPP]] | [[HEALY JAMES]] | $20.4M | 87 | – | pending |
| 2026-10-27 | [[STC]] | [[Matz Deborah Jane]] | $44K | 63 | +3.4% | open |
| 2026-10-27 | [[STC]] | [[EPPINGER FREDERICK H]] | $133K | 65 | +3.4% | open |
| 2026-10-26 | [[GPI]] | [[Conifer Management, L.L.C]] | $24.2M | 44 | +6.8% | open |
| 2026-10-26 | [[STC]] | [[Apel Thomas G]] | $95K | 48 | +2.9% | open |
| 2026-10-26 | [[STC]] | [[Corey William S. Jr]] | $94K | 54 | +2.9% | open |
| 2026-10-26 | [[STC]] | [[BRADLEY C ALLEN JR]] | $95K | 50 | +2.9% | open |
| 2026-10-23 | [[RAPP]] | [[Sanchez Ramiro]] | $98K | 67 | -2.9% | open |
| 2026-10-22 | [[RAPP]] | [[Silva Paul M]] | $100K | 67 | -8.5% | open |
| 2026-10-22 | [[RAPP]] | [[Young Wendy B]] | $100K | 65 | -8.5% | open |
| 2026-10-22 | [[RAPP]] | [[PAUL STEVEN M]] | $974K | 77 | -8.5% | open |
| 2026-10-22 | [[RAPP]] | [[MARAGANORE JOHN]] | $249K | 71 | -8.5% | open |
| 2026-10-21 | [[RAPP]] | [[Ignelzi Troy A]] | $144K | 54 | -2.9% | open |
| 2026-10-20 | [[NVA]] | [[Geller Avi]] | $5K | 32 | +20.3% | open |
| 2026-10-20 | [[NVA]] | [[Gerteisen Christopher]] | $22K | 35 | +20.3% | open |
| 2026-10-19 | [[CNXU]] | [[Purcell Lynn Sebastian]] | $500K | 36 | -22.4% | open |
| 2026-10-19 | [[APLD]] | [[Cummins Wes]] | $1.0M | 60 | -2.9% | open |
| 2026-10-19 | [[APLD]] | [[Zhang Jason Gechen]] | $5.7M | 71 | -2.9% | open |
| 2026-10-16 | [[SAH]] | [[Rusnak Paul P]] | $752K | 28 | -0.6% | open |
| 2026-10-15 | [[IMSR]] | [[Pardee Charles G]] | $22K | 55 | +1.6% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "contrarian")
SORT filed DESC
```

Back to [[What Works]].
