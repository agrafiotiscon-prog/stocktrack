---
type: "strategy"
key: "score_40"
signals: 32360
cagr: 0.0581472
spy_cagr: 0.110668
sharpe: 0.281738
max_drawdown: 0.585572
holdout_excess: 0.0146921
---

# Live score 40+ (notable)

Rule key: `score_40`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 32,360 |
| 3-month excess vs SPY (mean / median) | +1.1% / -0.6% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.8% |
| vs surviving stocks | +0.3% |
| 2006-2015 excess /yr | +7.9% (p 0.011) |
| 2016+ excess /yr | +1.5% (p 0.726) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.4% | +11.1% | 0.30 | 0.55 | 59% | 1.25 | -4.9% | 33% | 4,855 | 8.6% | -1.0% / -0.12 / 63% |
| 63d | +5.8% | +11.1% | 0.28 | 0.55 | 59% | 1.25 | -5.4% | 38% | 1,660 | 2.6% | -1.9% / -0.19 / 57% |
| 126d | +5.4% | +11.1% | 0.27 | 0.55 | 68% | 1.16 | -5.1% | 33% | 840 | 1.3% | -2.4% / -0.25 / 49% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +8.6%/yr, double costs +3.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +12.7% | +13.8% | -1.1% |
| 2007 | -8.7% | +5.1% | -13.9% |
| 2008 | -21.6% | -36.8% | +15.2% |
| 2009 | +36.1% | +26.4% | +9.8% |
| 2010 | +31.7% | +15.1% | +16.7% |
| 2011 | -13.7% | +1.9% | -15.6% |
| 2012 | +21.3% | +16.0% | +5.3% |
| 2013 | +34.7% | +32.3% | +2.4% |
| 2014 | +2.1% | +13.5% | -11.4% |
| 2015 | -7.8% | +1.2% | -9.0% |
| 2016 | +23.2% | +12.0% | +11.2% |
| 2017 | +19.4% | +21.7% | -2.3% |
| 2018 | -20.2% | -4.6% | -15.6% |
| 2019 | +42.2% | +31.2% | +10.9% |
| 2020 | +11.0% | +18.3% | -7.3% |
| 2021 | +6.0% | +28.7% | -22.7% |
| 2022 | -21.1% | -18.2% | -2.9% |
| 2023 | +29.4% | +26.2% | +3.3% |
| 2024 | -14.1% | +24.9% | -38.9% |
| 2025 | -5.7% | +17.7% | -23.4% |
| 2026 | +3.6% | +13.3% | -9.7% |


## Live forward test

5 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-19 | [[IAM]] | [[Rachlin Evan Lockwood]] | $11.5M | 60 | – | pending |
| 2026-10-19 | [[CTY]] | [[NELSEN ROBERT]] | $3.1M | 40 | – | pending |
| 2026-10-19 | [[BPRE]] | [[KAMFAR RAMIN]] | $2.4M | 64 | – | pending |
| 2026-10-16 | [[PEP]] | [[POHLAD ROBERT C]] | $23.7M | 62 | +2.2% | open |
| 2026-10-16 | [[BYRN]] | [[Roth Adam L]] | $70K | 40 | +2.7% | open |
| 2026-10-16 | [[PAM]] | [[Mindlin Marcos Marcelo]] | $35.1M | 49 | -2.6% | open |
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | $1.5M | 72 | +1.7% | open |
| 2026-10-16 | [[BORR]] | [[Troim Tor Olav]] | $2.3M | 51 | +1.7% | open |
| 2026-10-15 | [[BPRE]] | [[Ruddy Jordan B]] | $44K | 63 | -1.5% | open |
| 2026-10-15 | [[IMSR]] | [[Pardee Charles G]] | $22K | 55 | -11.2% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -2.0% | open |
| 2026-10-15 | [[TRXB]] | [[Alexandria Venture Investments, LLC]] | $2.5M | 55 | +5.3% | open |
| 2026-10-15 | [[CXM]] | [[WARD JR STEPHEN M]] | $850K | 51 | +0.5% | open |
| 2026-10-15 | [[GOLD]] | [[Tether Global Investments Fund, S.I.C.A.F., S.A]] | $2.7M | 45 | -3.3% | open |
| 2026-10-15 | [[BORR]] | [[Troim Tor Olav]] | $3.5M | 41 | -5.1% | open |
| 2026-10-14 | [[INBX]] | [[Lappe Mark]] | $849K | 47 | +2.5% | open |
| 2026-10-14 | [[BPRE]] | [[KAMFAR RAMIN]] | $5.5M | 73 | -2.7% | open |
| 2026-10-14 | [[QVCG]] | [[GOLDENTREE ASSET MANAGEMENT LP]] | $16.7M | 48 | -13.5% | open |
| 2026-10-14 | [[BORR]] | [[Troim Tor Olav]] | $7.4M | 46 | -5.8% | open |
| 2026-10-14 | [[KIO]] | [[Pimentel Rudy]] | $41K | 45 | +1.0% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_40")
SORT filed DESC
```

Back to [[What Works]].
