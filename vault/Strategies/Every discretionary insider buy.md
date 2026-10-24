---
type: "strategy"
key: "all_liquid"
signals: 67489
cagr: 0.0556971
spy_cagr: 0.110825
sharpe: 0.27353
max_drawdown: 0.584268
holdout_excess: 0.0031164
---

# Every discretionary insider buy

Rule key: `all_liquid`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 67,489 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.7% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.6% |
| vs surviving stocks | +1.0% |
| 2006-2015 excess /yr | +6.4% (p 0.018) |
| 2016+ excess /yr | +0.3% (p 0.932) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +7.2% | +11.1% | 0.33 | 0.56 | 61% | 1.21 | -3.7% | 38% | 4,977 | 9.2% | -1.0% / -0.12 / 67% |
| 63d | +5.6% | +11.1% | 0.27 | 0.56 | 58% | 1.18 | -5.5% | 43% | 1,660 | 2.7% | -2.7% / -0.28 / 65% |
| 126d | +6.6% | +11.1% | 0.31 | 0.56 | 54% | 1.15 | -4.3% | 33% | 840 | 1.5% | -1.9% / -0.21 / 58% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +8.5%/yr, double costs +2.9%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +22.9% | +13.8% | +9.0% |
| 2007 | -5.0% | +5.1% | -10.1% |
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
| 2023 | +25.4% | +26.2% | -0.8% |
| 2024 | -14.2% | +24.9% | -39.1% |
| 2025 | -4.2% | +17.7% | -21.9% |
| 2026 | -1.6% | +13.7% | -15.2% |


## Live forward test

42 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-23 | [[BPRE]] | [[Ruddy Jordan B]] | $25K | 48 | – | pending |
| 2026-10-23 | [[NXG]] | [[Swank Jerry V]] | $439K | 64 | – | pending |
| 2026-10-23 | [[NXG]] | [[Nelson Blake]] | $40K | 68 | – | pending |
| 2026-10-23 | [[CRBG]] | [[NIPPON LIFE INSURANCE CO]] | $7.7M | 23 | – | pending |
| 2026-10-23 | [[CHCO]] | [[STRONG-TREISTER DIANE W]] | $17K | 4 | – | pending |
| 2026-10-23 | [[CHCO]] | [[Reyes Javier A]] | $14K | 4 | – | pending |
| 2026-10-23 | [[CHCO]] | [[Hoyer James A]] | $14K | 9 | – | pending |
| 2026-10-23 | [[CHCO]] | [[FISHER ROBERT D]] | $23K | 2 | – | pending |
| 2026-10-23 | [[MSM]] | [[Slone Reuben E]] | $50K | 39 | – | pending |
| 2026-10-23 | [[RAPP]] | [[Sanchez Ramiro]] | $98K | 67 | – | pending |
| 2026-10-23 | [[THFF]] | [[McDonald James O]] | $6K | 14 | – | pending |
| 2026-10-23 | [[CLF]] | [[Camara Edilson]] | $100K | 32 | – | pending |
| 2026-10-23 | [[BZUN]] | [[Qiu Wenbin]] | $40K | 33 | – | pending |
| 2026-10-22 | [[DOLE]] | [[Pale Fire Capital SE]] | $8.6M | 45 | -0.8% | open |
| 2026-10-22 | [[LEO]] | [[Saba Capital Management, L.P]] | $263K | 25 | -1.1% | open |
| 2026-10-22 | [[CRBG]] | [[NIPPON LIFE INSURANCE CO]] | $6.8M | 22 | -2.5% | open |
| 2026-10-22 | [[RAPP]] | [[Silva Paul M]] | $100K | 67 | -5.9% | open |
| 2026-10-22 | [[RAPP]] | [[Young Wendy B]] | $100K | 65 | -5.9% | open |
| 2026-10-22 | [[RAPP]] | [[PAUL STEVEN M]] | $974K | 77 | -5.9% | open |
| 2026-10-22 | [[RAPP]] | [[MARAGANORE JOHN]] | $249K | 71 | -5.9% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "all_liquid")
SORT filed DESC
```

Back to [[What Works]].
