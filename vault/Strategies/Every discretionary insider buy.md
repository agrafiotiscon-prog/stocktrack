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

21 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-21 | [[FBK]] | [[INGRAM ORRIN H II]] | $1.5M | 49 | – | pending |
| 2026-10-21 | [[BPRE]] | [[KAMFAR RAMIN]] | $3.3M | 59 | – | pending |
| 2026-10-21 | [[RAPP]] | [[Ignelzi Troy A]] | $144K | 54 | – | pending |
| 2026-10-21 | [[CRF]] | [[Bradshaw Joshua]] | $118K | 53 | – | pending |
| 2026-10-21 | [[CLM]] | [[Bradshaw Joshua]] | $97K | 52 | – | pending |
| 2026-10-21 | [[CRBG]] | [[NIPPON LIFE INSURANCE CO]] | $5.6M | 21 | – | pending |
| 2026-10-21 | [[NBIS]] | [[Grimme Arne]] | $50K | 10 | – | pending |
| 2026-10-21 | [[LEO]] | [[Saba Capital Management, L.P]] | $44K | 15 | – | pending |
| 2026-10-21 | [[DX]] | [[BOSTON BYRON L]] | $100K | 50 | – | pending |
| 2026-10-21 | [[DSM]] | [[Saba Capital Management, L.P]] | $78K | 18 | – | pending |
| 2026-10-21 | [[YORW]] | [[Velazquez David M]] | $40K | 38 | – | pending |
| 2026-10-21 | [[YORW]] | [[Brossman Douglas S]] | $1,000 | 31 | – | pending |
| 2026-10-20 | [[DX]] | [[Popenoe Smriti Laxman]] | $106K | 39 | -1.1% | open |
| 2026-10-20 | [[DX]] | [[Sartori Michael Andrew]] | $11K | 39 | -1.1% | open |
| 2026-10-20 | [[CRBG]] | [[NIPPON LIFE INSURANCE CO]] | $12.1M | 24 | -0.8% | open |
| 2026-10-20 | [[LEO]] | [[Saba Capital Management, L.P]] | $1.9M | 37 | -1.3% | open |
| 2026-10-20 | [[NVA]] | [[Geller Avi]] | $5K | 32 | -0.2% | open |
| 2026-10-20 | [[NVA]] | [[Gerteisen Christopher]] | $22K | 35 | -0.2% | open |
| 2026-10-20 | [[AYI]] | [[O'Shaughnessy Laura]] | $22K | 20 | +3.0% | open |
| 2026-10-20 | [[DSM]] | [[Saba Capital Management, L.P]] | $1.1M | 34 | -0.8% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "all_liquid")
SORT filed DESC
```

Back to [[What Works]].
