---
type: "strategy"
key: "score_40"
signals: 33069
cagr: 0.0570607
spy_cagr: 0.110724
sharpe: 0.278065
max_drawdown: 0.615685
holdout_excess: 0.0169971
---

# Live score 40+ (notable)

Rule key: `score_40`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 33,069 |
| 3-month excess vs SPY (mean / median) | +1.1% / -0.5% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +0.9% |
| vs surviving stocks | +0.5% |
| 2006-2015 excess /yr | +8.0% (p 0.012) |
| 2016+ excess /yr | +1.7% (p 0.686) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Years beating SPY | Trades | Costs/yr |
|---|---|---|---|---|---|---|---|---|---|
| 21d | +8.7% | +11.1% | 0.38 | 0.56 | 56% | 1.14 | 38% | 4,855 | 8.5% |
| 63d | +5.7% | +11.1% | 0.28 | 0.56 | 62% | 1.17 | 38% | 1,660 | 2.7% |
| 126d | +5.5% | +11.1% | 0.27 | 0.56 | 66% | 1.15 | 29% | 840 | 1.4% |


Cost sensitivity (63-session hold): no costs +8.5%/yr, double costs +3.1%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +10.2% | +13.8% | -3.7% |
| 2007 | -11.7% | +5.1% | -16.8% |
| 2008 | -26.9% | -36.8% | +9.9% |
| 2009 | +33.7% | +26.4% | +7.4% |
| 2010 | +31.3% | +15.1% | +16.2% |
| 2011 | -6.6% | +1.9% | -8.5% |
| 2012 | +23.0% | +16.0% | +7.0% |
| 2013 | +41.8% | +32.3% | +9.5% |
| 2014 | +3.4% | +13.5% | -10.1% |
| 2015 | -9.9% | +1.2% | -11.2% |
| 2016 | +20.3% | +12.0% | +8.3% |
| 2017 | +21.4% | +21.7% | -0.3% |
| 2018 | -22.8% | -4.6% | -18.2% |
| 2019 | +42.2% | +31.2% | +10.9% |
| 2020 | +17.9% | +18.3% | -0.5% |
| 2021 | +8.4% | +28.7% | -20.3% |
| 2022 | -31.6% | -18.2% | -13.4% |
| 2023 | +32.8% | +26.2% | +6.6% |
| 2024 | -3.9% | +24.9% | -28.8% |
| 2025 | -12.8% | +17.7% | -30.5% |
| 2026 | +7.1% | +13.4% | -6.3% |


## Live forward test

5 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-16 | [[PEP]] | [[POHLAD ROBERT C]] | $23.7M | 62 | +1.7% | open |
| 2026-10-16 | [[BYRN]] | [[Roth Adam L]] | $70K | 40 | +0.7% | open |
| 2026-10-16 | [[PAM]] | [[Mindlin Marcos Marcelo]] | $35.1M | 49 | -2.5% | open |
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | $1.5M | 72 | -1.5% | open |
| 2026-10-16 | [[BORR]] | [[Troim Tor Olav]] | $2.3M | 51 | -1.5% | open |
| 2026-10-15 | [[BPRE]] | [[Ruddy Jordan B]] | $44K | 63 | -1.5% | open |
| 2026-10-15 | [[IMSR]] | [[Pardee Charles G]] | $22K | 55 | -10.4% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -0.9% | open |
| 2026-10-15 | [[TRXB]] | [[Alexandria Venture Investments, LLC]] | $2.5M | 55 | +3.1% | open |
| 2026-10-15 | [[CXM]] | [[WARD JR STEPHEN M]] | $850K | 51 | +0.1% | open |
| 2026-10-15 | [[GOLD]] | [[Tether Global Investments Fund, S.I.C.A.F., S.A]] | $2.7M | 45 | -2.4% | open |
| 2026-10-15 | [[BORR]] | [[Troim Tor Olav]] | $3.5M | 41 | -8.1% | open |
| 2026-10-14 | [[INBX]] | [[Lappe Mark]] | $849K | 47 | +2.0% | open |
| 2026-10-14 | [[BPRE]] | [[KAMFAR RAMIN]] | $5.5M | 73 | -2.7% | open |
| 2026-10-14 | [[QVCG]] | [[GOLDENTREE ASSET MANAGEMENT LP]] | $16.7M | 48 | -15.1% | open |
| 2026-10-14 | [[BORR]] | [[Troim Tor Olav]] | $7.4M | 46 | -8.9% | open |
| 2026-10-14 | [[KIO]] | [[Pimentel Rudy]] | $41K | 45 | +0.2% | open |
| 2026-10-14 | [[TDIC]] | [[Seto Wai Yue]] | $600K | 58 | -6.2% | open |
| 2026-10-14 | [[IMSR]] | [[Irish Simon]] | $51K | 46 | +0.5% | open |
| 2026-10-13 | [[CTNT]] | [[Liu Huan]] | $330K | 49 | +13.5% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_40")
SORT filed DESC
```

Back to [[What Works]].
