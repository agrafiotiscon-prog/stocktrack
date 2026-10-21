---
type: "strategy"
key: "contrarian"
signals: 8146
cagr: 0.0204412
spy_cagr: 0.110085
sharpe: 0.185313
max_drawdown: 0.738498
holdout_excess: -0.050839
---

# Insider buying after a 30%+ drop

Rule key: `contrarian`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 8,146 |
| 3-month excess vs SPY (mean / median) | +5.2% / +2.1% |
| Beat SPY over 3 months | 53% |
| Entering one session later | +4.8% |
| vs surviving stocks | +4.0% |
| 2006-2015 excess /yr | +13.4% (p 0.157) |
| 2016+ excess /yr | -5.1% (p 0.464) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +2.7% | +11.0% | 0.18 | 0.55 | 72% | 1.14 | -6.8% | 33% | 2,237 | 6.1% | +1.3% / 0.06 / 65% |
| 63d | +2.0% | +11.0% | 0.19 | 0.55 | 74% | 1.59 | -9.5% | 24% | 1,180 | 3.3% | -1.7% / -0.06 / 66% |
| 126d | +6.9% | +11.0% | 0.32 | 0.55 | 67% | 1.63 | -5.3% | 48% | 717 | 2.0% | +1.3% / 0.09 / 63% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +5.4%/yr, double costs -1.2%/yr.


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
| 2019 | +30.6% | +31.2% | -0.7% |
| 2020 | +17.3% | +18.3% | -1.0% |
| 2021 | -12.3% | +28.7% | -41.0% |
| 2022 | -47.2% | -18.2% | -29.0% |
| 2023 | +11.8% | +26.2% | -14.4% |
| 2024 | -2.1% | +24.9% | -26.9% |
| 2025 | +8.3% | +17.7% | -9.4% |
| 2026 | +9.1% | +13.3% | -4.2% |


## Live forward test

1 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-20 | [[NVA]] | [[Geller Avi]] | $5K | 32 | – | pending |
| 2026-10-20 | [[NVA]] | [[Gerteisen Christopher]] | $22K | 35 | – | pending |
| 2026-10-19 | [[CNXU]] | [[Purcell Lynn Sebastian]] | $500K | 36 | -10.6% | open |
| 2026-10-19 | [[APLD]] | [[Cummins Wes]] | $1.0M | 60 | +3.5% | open |
| 2026-10-19 | [[APLD]] | [[Zhang Jason Gechen]] | $5.7M | 71 | +3.5% | open |
| 2026-10-16 | [[SAH]] | [[Rusnak Paul P]] | $752K | 28 | -1.1% | open |
| 2026-10-15 | [[IMSR]] | [[Pardee Charles G]] | $22K | 55 | -13.0% | open |
| 2026-10-14 | [[TDIC]] | [[Seto Wai Yue]] | $600K | 58 | -9.8% | open |
| 2026-10-14 | [[IMSR]] | [[Irish Simon]] | $51K | 46 | -2.5% | open |
| 2026-10-13 | [[CTNT]] | [[Liu Huan]] | $330K | 49 | +7.0% | open |
| 2026-10-13 | [[IMSR]] | [[BUCKMAN FREDERICK W]] | $39K | 38 | -7.4% | open |
| 2026-10-09 | [[SAH]] | [[Rusnak Paul P]] | $819K | 29 | +6.4% | open |
| 2026-10-08 | [[AVR]] | [[L1 Capital Pty Ltd]] | $2.0M | 37 | -5.6% | open |
| 2026-10-07 | [[SAH]] | [[Rusnak Paul P]] | $67K | 17 | +6.1% | open |
| 2026-10-07 | [[AGMB]] | [[Epstein David R]] | $86K | 53 | -0.9% | open |
| 2026-10-07 | [[AGMB]] | [[Knotnerus Tim Jasper]] | $94K | 67 | -0.9% | open |
| 2026-10-06 | [[LWAY]] | [[Divisadero Street Capital Management, LP]] | $2.2M | 37 | +4.8% | open |
| 2026-10-06 | [[SAH]] | [[Rusnak Paul P]] | $1.7M | 32 | +5.2% | open |
| 2026-10-06 | [[DYN]] | [[Posner Brian S]] | $40K | 27 | +6.5% | open |
| 2026-10-06 | [[SAH]] | [[Rusnak Paul P]] | $1.3M | 31 | +5.2% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "contrarian")
SORT filed DESC
```

Back to [[What Works]].
