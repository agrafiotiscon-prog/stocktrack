---
type: "strategy"
key: "momentum_buy"
signals: 3921
cagr: 0.199353
spy_cagr: 0.109342
sharpe: 0.823839
max_drawdown: 0.401829
holdout_excess: 0.207925
---

# Insider buying after a 30%+ run-up (post-hoc)

Rule key: `momentum_buy`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

> [!warning] Post-hoc idea
> This rule was written after seeing the backtest, so the backtest numbers below are in-sample and can't confirm it. Only the live forward test counts. See [[Findings]] and `data/backtest/hypotheses.json`.

## Backtest

| Measure | Value |
|---|---|
| Signals | 3,921 |
| 3-month excess vs SPY (mean / median) | +2.6% / -1.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +2.2% |
| vs surviving stocks | +3.2% |
| 2006-2015 excess /yr | +9.3% (p 0.173) |
| 2016+ excess /yr | +20.8% (p 0.027) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +12.2% | +10.9% | 0.66 | 0.55 | 47% | 0.48 | +6.4% | 33% | 2,006 | 6.5% | +8.4% / 0.60 / 31% |
| 63d | +19.9% | +10.9% | 0.82 | 0.55 | 40% | 0.93 | +10.2% | 52% | 1,229 | 3.1% | +13.4% / 0.77 / 26% |
| 126d | +14.0% | +10.9% | 0.54 | 0.55 | 56% | 1.17 | +3.3% | 52% | 747 | 2.1% | +7.3% / 0.39 / 37% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +22.0%/yr, double costs +17.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +12.1% | +13.3% | -1.2% |
| 2007 | +15.2% | +5.1% | +10.1% |
| 2008 | -18.6% | -36.8% | +18.2% |
| 2009 | +78.3% | +26.4% | +52.0% |
| 2010 | +11.2% | +15.1% | -3.8% |
| 2011 | -6.4% | +1.9% | -8.3% |
| 2012 | +13.3% | +16.0% | -2.7% |
| 2013 | +54.5% | +32.3% | +22.2% |
| 2014 | -5.7% | +13.5% | -19.1% |
| 2015 | -11.4% | +1.2% | -12.6% |
| 2016 | +7.9% | +12.0% | -4.1% |
| 2017 | +31.3% | +21.7% | +9.6% |
| 2018 | +29.9% | -4.6% | +34.5% |
| 2019 | +25.5% | +31.2% | -5.7% |
| 2020 | +131.0% | +18.3% | +112.7% |
| 2021 | +31.0% | +28.7% | +2.3% |
| 2022 | -7.1% | -18.2% | +11.1% |
| 2023 | +0.5% | +26.2% | -25.7% |
| 2024 | +6.4% | +24.9% | -18.5% |
| 2025 | +90.1% | +17.7% | +72.4% |
| 2026 | +16.2% | +11.5% | +4.7% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 4 | -0.6% | +4.5% | 50% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-06 | [[KOD]] | [[BAKER BROS. ADVISORS LP]] | $24.3M | 45 | – | pending |
| 2026-11-04 | [[AEYE]] | [[HAWKINS JAMES B]] | $38K | 21 | -0.2% | open |
| 2026-11-02 | [[AEYE]] | [[HAWKINS JAMES B]] | $53K | 23 | -5.2% | open |
| 2026-10-29 | [[AEYE]] | [[HAWKINS JAMES B]] | $37K | 21 | -8.0% | open |
| 2026-10-28 | [[ACN]] | [[Sweet Julie Spellman]] | $3.0M | 78 | +13.2% | open |
| 2026-10-28 | [[ACN]] | [[Price Paula A]] | $200K | 46 | +13.2% | open |
| 2026-10-23 | [[BZUN]] | [[Qiu Wenbin]] | $40K | 33 | +0.5% | open |
| 2026-10-20 | [[XGN]] | [[Chernett Jorey]] | $104K | 20 | -17.5% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "momentum_buy")
SORT filed DESC
```

Back to [[What Works]].
