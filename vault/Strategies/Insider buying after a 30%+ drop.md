---
type: "strategy"
key: "contrarian"
signals: 8148
cagr: 0.0192422
spy_cagr: 0.110244
sharpe: 0.181578
max_drawdown: 0.738498
holdout_excess: -0.0516017
---

# Insider buying after a 30%+ drop

Rule key: `contrarian`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 8,148 |
| 3-month excess vs SPY (mean / median) | +5.2% / +2.1% |
| Beat SPY over 3 months | 53% |
| Entering one session later | +4.8% |
| vs surviving stocks | +3.9% |
| 2006-2015 excess /yr | +13.4% (p 0.157) |
| 2016+ excess /yr | -5.2% (p 0.456) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +2.7% | +11.0% | 0.18 | 0.55 | 72% | 1.14 | -6.8% | 33% | 2,239 | 6.1% | +1.3% / 0.07 / 65% |
| 63d | +1.9% | +11.0% | 0.18 | 0.55 | 74% | 1.58 | -9.6% | 24% | 1,180 | 3.3% | -1.8% / -0.07 / 66% |
| 126d | +6.2% | +11.0% | 0.30 | 0.55 | 67% | 1.62 | -6.1% | 48% | 716 | 2.0% | +0.7% / 0.05 / 67% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +5.3%/yr, double costs -1.3%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +22.1% | +9.7% | +12.4% |
| 2007 | +6.6% | +5.1% | +1.4% |
| 2008 | -47.6% | -36.8% | -10.8% |
| 2009 | +24.2% | +26.4% | -2.1% |
| 2010 | +21.5% | +15.1% | +6.4% |
| 2011 | -8.2% | +1.9% | -10.1% |
| 2012 | +28.4% | +16.0% | +12.4% |
| 2013 | +26.1% | +32.3% | -6.2% |
| 2014 | -2.0% | +13.5% | -15.5% |
| 2015 | -21.6% | +1.2% | -22.8% |
| 2016 | +38.9% | +12.0% | +26.9% |
| 2017 | +14.8% | +21.7% | -6.9% |
| 2018 | -11.8% | -4.6% | -7.2% |
| 2019 | +30.6% | +31.2% | -0.6% |
| 2020 | +14.9% | +18.3% | -3.4% |
| 2021 | -12.3% | +28.7% | -41.0% |
| 2022 | -47.2% | -18.2% | -29.0% |
| 2023 | +11.8% | +26.2% | -14.4% |
| 2024 | -2.1% | +24.9% | -26.9% |
| 2025 | +8.3% | +17.7% | -9.4% |
| 2026 | +8.8% | +13.7% | -4.9% |


## Live forward test

4 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-23 | [[RAPP]] | [[Sanchez Ramiro]] | $98K | 67 | – | pending |
| 2026-10-22 | [[RAPP]] | [[Silva Paul M]] | $100K | 67 | -5.9% | open |
| 2026-10-22 | [[RAPP]] | [[Young Wendy B]] | $100K | 65 | -5.9% | open |
| 2026-10-22 | [[RAPP]] | [[PAUL STEVEN M]] | $974K | 77 | -5.9% | open |
| 2026-10-22 | [[RAPP]] | [[MARAGANORE JOHN]] | $249K | 71 | -5.9% | open |
| 2026-10-21 | [[RAPP]] | [[Ignelzi Troy A]] | $144K | 54 | -0.1% | open |
| 2026-10-20 | [[NVA]] | [[Geller Avi]] | $5K | 32 | -9.4% | open |
| 2026-10-20 | [[NVA]] | [[Gerteisen Christopher]] | $22K | 35 | -9.4% | open |
| 2026-10-19 | [[CNXU]] | [[Purcell Lynn Sebastian]] | $500K | 36 | -6.1% | open |
| 2026-10-19 | [[APLD]] | [[Cummins Wes]] | $1.0M | 60 | -1.1% | open |
| 2026-10-19 | [[APLD]] | [[Zhang Jason Gechen]] | $5.7M | 71 | -1.1% | open |
| 2026-10-16 | [[SAH]] | [[Rusnak Paul P]] | $752K | 28 | -4.2% | open |
| 2026-10-15 | [[IMSR]] | [[Pardee Charles G]] | $22K | 55 | -11.9% | open |
| 2026-10-14 | [[TDIC]] | [[Seto Wai Yue]] | $600K | 58 | -17.6% | open |
| 2026-10-14 | [[IMSR]] | [[Irish Simon]] | $51K | 46 | -1.3% | open |
| 2026-10-13 | [[CTNT]] | [[Liu Huan]] | $330K | 49 | -4.7% | open |
| 2026-10-13 | [[IMSR]] | [[BUCKMAN FREDERICK W]] | $39K | 38 | -6.3% | open |
| 2026-10-09 | [[SAH]] | [[Rusnak Paul P]] | $819K | 29 | +3.0% | open |
| 2026-10-08 | [[AVR]] | [[L1 Capital Pty Ltd]] | $2.0M | 37 | -10.7% | open |
| 2026-10-07 | [[SAH]] | [[Rusnak Paul P]] | $67K | 17 | +2.8% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "contrarian")
SORT filed DESC
```

Back to [[What Works]].
