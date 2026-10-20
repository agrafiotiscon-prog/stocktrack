---
type: "strategy"
key: "contrarian"
signals: 7998
cagr: 0.0114138
spy_cagr: 0.110142
sharpe: 0.159026
max_drawdown: 0.738712
holdout_excess: -0.0523548
---

# Insider buying after a 30%+ drop

Rule key: `contrarian`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,998 |
| 3-month excess vs SPY (mean / median) | +5.3% / +2.1% |
| Beat SPY over 3 months | 53% |
| Entering one session later | +4.9% |
| vs surviving stocks | +2.1% |
| 2006-2015 excess /yr | +13.1% (p 0.169) |
| 2016+ excess /yr | -5.2% (p 0.441) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Years beating SPY | Trades | Costs/yr |
|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.3% | +11.0% | 0.20 | 0.55 | 69% | 1.04 | 33% | 2,213 | 6.1% |
| 63d | +1.1% | +11.0% | 0.16 | 0.55 | 74% | 1.30 | 29% | 1,169 | 3.2% |
| 126d | +6.7% | +11.0% | 0.31 | 0.55 | 69% | 1.30 | 43% | 708 | 2.0% |


Cost sensitivity (63-session hold): no costs +4.4%/yr, double costs -2.0%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +22.1% | +9.7% | +12.4% |
| 2007 | +6.6% | +5.1% | +1.4% |
| 2008 | -47.8% | -36.8% | -11.0% |
| 2009 | +19.7% | +26.4% | -6.7% |
| 2010 | +18.3% | +15.1% | +3.2% |
| 2011 | -8.2% | +1.9% | -10.1% |
| 2012 | +27.8% | +16.0% | +11.8% |
| 2013 | +24.2% | +32.3% | -8.1% |
| 2014 | -1.4% | +13.5% | -14.9% |
| 2015 | -24.4% | +1.2% | -25.6% |
| 2016 | +29.7% | +12.0% | +17.7% |
| 2017 | +15.8% | +21.7% | -5.9% |
| 2018 | -11.8% | -4.6% | -7.2% |
| 2019 | +33.7% | +31.2% | +2.5% |
| 2020 | +15.0% | +18.3% | -3.4% |
| 2021 | -11.5% | +28.7% | -40.3% |
| 2022 | -48.6% | -18.2% | -30.4% |
| 2023 | +13.2% | +26.2% | -13.0% |
| 2024 | -5.8% | +24.9% | -30.7% |
| 2025 | +11.7% | +17.7% | -6.0% |
| 2026 | +9.6% | +13.4% | -3.8% |


## Live forward test

1 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-16 | [[SAH]] | [[Rusnak Paul P]] | $752K | 28 | -2.3% | open |
| 2026-10-15 | [[IMSR]] | [[Pardee Charles G]] | $22K | 55 | -10.4% | open |
| 2026-10-14 | [[TDIC]] | [[Seto Wai Yue]] | $600K | 58 | -6.2% | open |
| 2026-10-14 | [[IMSR]] | [[Irish Simon]] | $51K | 46 | +0.5% | open |
| 2026-10-13 | [[CTNT]] | [[Liu Huan]] | $330K | 49 | +13.5% | open |
| 2026-10-13 | [[IMSR]] | [[BUCKMAN FREDERICK W]] | $39K | 38 | -4.6% | open |
| 2026-10-09 | [[SAH]] | [[Rusnak Paul P]] | $819K | 29 | +5.1% | open |
| 2026-10-08 | [[AVR]] | [[L1 Capital Pty Ltd]] | $2.0M | 37 | -6.9% | open |
| 2026-10-07 | [[SAH]] | [[Rusnak Paul P]] | $67K | 17 | +4.9% | open |
| 2026-10-07 | [[AGMB]] | [[Epstein David R]] | $86K | 53 | -4.0% | open |
| 2026-10-07 | [[AGMB]] | [[Knotnerus Tim Jasper]] | $94K | 67 | -4.0% | open |
| 2026-10-06 | [[LWAY]] | [[Divisadero Street Capital Management, LP]] | $2.2M | 37 | +4.0% | open |
| 2026-10-06 | [[SAH]] | [[Rusnak Paul P]] | $1.7M | 32 | +4.0% | open |
| 2026-10-06 | [[DYN]] | [[Posner Brian S]] | $40K | 27 | -1.8% | open |
| 2026-10-06 | [[SAH]] | [[Rusnak Paul P]] | $1.3M | 31 | +4.0% | open |
| 2026-10-05 | [[NXRT]] | [[McGraner Matt]] | $201K | 32 | -4.4% | open |
| 2026-10-02 | [[NYAX]] | [[Nechmad Yair]] | $2.1M | 62 | -6.0% | open |
| 2026-10-01 | [[ASPI]] | [[Ryan Robert John Andrew]] | $40K | 22 | -33.6% | open |
| 2026-10-01 | [[DKS]] | [[Barnes Matthew]] | $500K | 78 | +6.8% | open |
| 2026-10-01 | [[XENE]] | [[Kelly Thomas Patrick]] | $560K | 71 | -10.7% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "contrarian")
SORT filed DESC
```

Back to [[What Works]].
