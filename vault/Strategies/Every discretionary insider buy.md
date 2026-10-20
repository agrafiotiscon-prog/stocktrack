---
type: "strategy"
key: "all_liquid"
signals: 67505
cagr: 0.0546596
spy_cagr: 0.110668
sharpe: 0.269767
max_drawdown: 0.593095
holdout_excess: 0.00270363
---

# Every discretionary insider buy

Rule key: `all_liquid`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 67,505 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.7% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.6% |
| vs surviving stocks | +0.1% |
| 2006-2015 excess /yr | +6.4% (p 0.017) |
| 2016+ excess /yr | +0.3% (p 0.940) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.7% | +11.1% | 0.31 | 0.55 | 61% | 1.22 | -4.2% | 38% | 4,963 | 9.1% | -1.5% / -0.16 / 68% |
| 63d | +5.5% | +11.1% | 0.27 | 0.55 | 59% | 1.18 | -5.6% | 43% | 1,660 | 2.7% | -2.8% / -0.29 / 66% |
| 126d | +5.1% | +11.1% | 0.25 | 0.55 | 55% | 1.15 | -5.7% | 29% | 840 | 1.4% | -3.3% / -0.35 / 69% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +8.4%/yr, double costs +2.7%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +22.9% | +13.8% | +9.0% |
| 2007 | -4.6% | +5.1% | -9.8% |
| 2008 | -27.7% | -36.8% | +9.1% |
| 2009 | +54.7% | +26.4% | +28.3% |
| 2010 | +22.9% | +15.1% | +7.9% |
| 2011 | -9.5% | +1.9% | -11.3% |
| 2012 | +21.8% | +16.0% | +5.8% |
| 2013 | +36.2% | +32.3% | +3.9% |
| 2014 | +5.3% | +13.5% | -8.2% |
| 2015 | +7.0% | +1.2% | +5.8% |
| 2016 | +18.2% | +12.0% | +6.2% |
| 2017 | +15.2% | +21.7% | -6.5% |
| 2018 | -13.7% | -4.6% | -9.1% |
| 2019 | +14.0% | +31.2% | -17.2% |
| 2020 | +40.6% | +18.3% | +22.2% |
| 2021 | +0.6% | +28.7% | -28.2% |
| 2022 | -41.0% | -18.2% | -22.8% |
| 2023 | +23.7% | +26.2% | -2.4% |
| 2024 | -14.9% | +24.9% | -39.8% |
| 2025 | -4.2% | +17.7% | -21.9% |
| 2026 | -1.8% | +13.3% | -15.1% |


## Live forward test

13 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-19 | [[IAM]] | [[Rachlin Evan Lockwood]] | $11.5M | 60 | – | pending |
| 2026-10-19 | [[DSM]] | [[Saba Capital Management, L.P]] | $72K | 18 | – | pending |
| 2026-10-19 | [[CTY]] | [[NELSEN ROBERT]] | $3.1M | 40 | – | pending |
| 2026-10-19 | [[HQY]] | [[Rajasekar Sunil]] | $12K | 20 | – | pending |
| 2026-10-19 | [[EME]] | [[MCEVOY M KEVIN]] | $2K | 2 | – | pending |
| 2026-10-19 | [[BPRE]] | [[KAMFAR RAMIN]] | $2.4M | 64 | – | pending |
| 2026-10-19 | [[CNXU]] | [[Purcell Lynn Sebastian]] | $500K | 36 | – | pending |
| 2026-10-19 | [[CRBG]] | [[NIPPON LIFE INSURANCE CO]] | $17.1M | 25 | – | pending |
| 2026-10-19 | [[XFOR]] | [[Craig Adam R]] | $12K | 26 | – | pending |
| 2026-10-19 | [[EQBK]] | [[Borck Leon]] | $19K | 16 | – | pending |
| 2026-10-19 | [[FUL]] | [[Malik Muhammad Shahbaz]] | $25K | 35 | – | pending |
| 2026-10-16 | [[SAH]] | [[Rusnak Paul P]] | $752K | 28 | -2.8% | open |
| 2026-10-16 | [[NAD]] | [[TOTH TERENCE J]] | $72K | 33 | -0.4% | open |
| 2026-10-16 | [[CRBG]] | [[NIPPON LIFE INSURANCE CO]] | $20.5M | 25 | +0.1% | open |
| 2026-10-16 | [[FIS]] | [[Goldstein Jeffrey A]] | $58K | 13 | +0.8% | open |
| 2026-10-16 | [[NBIS]] | [[Grimme Arne]] | $50K | 10 | -3.5% | open |
| 2026-10-16 | [[PEP]] | [[POHLAD ROBERT C]] | $23.7M | 62 | +2.2% | open |
| 2026-10-16 | [[BYRN]] | [[Roth Adam L]] | $70K | 40 | +2.7% | open |
| 2026-10-16 | [[PAM]] | [[Mindlin Marcos Marcelo]] | $35.1M | 49 | -2.6% | open |
| 2026-10-16 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | -1.8% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "all_liquid")
SORT filed DESC
```

Back to [[What Works]].
