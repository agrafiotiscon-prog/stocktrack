---
type: "strategy"
key: "momentum_buy"
signals: 3924
cagr: 0.201426
spy_cagr: 0.110525
sharpe: 0.831829
max_drawdown: 0.401829
holdout_excess: 0.218881
---

# Insider buying after a 30%+ run-up (post-hoc)

Rule key: `momentum_buy`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

> [!warning] Post-hoc idea
> This rule was written after seeing the backtest, so the backtest numbers below are in-sample and can't confirm it. Only the live forward test counts. See [[Findings]] and `data/backtest/hypotheses.json`.

## Backtest

| Measure | Value |
|---|---|
| Signals | 3,924 |
| 3-month excess vs SPY (mean / median) | +2.7% / -1.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +2.2% |
| vs surviving stocks | +3.2% |
| 2006-2015 excess /yr | +9.6% (p 0.163) |
| 2016+ excess /yr | +21.9% (p 0.020) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +12.1% | +11.1% | 0.66 | 0.55 | 47% | 0.47 | +6.3% | 29% | 2,007 | 6.5% | +8.4% / 0.59 / 31% |
| 63d | +20.1% | +11.1% | 0.83 | 0.55 | 40% | 0.93 | +10.4% | 52% | 1,231 | 3.1% | +13.6% / 0.78 / 26% |
| 126d | +14.4% | +11.1% | 0.56 | 0.55 | 56% | 1.17 | +3.6% | 52% | 748 | 2.1% | +7.7% / 0.41 / 38% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +22.2%/yr, double costs +17.5%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +10.8% | +13.3% | -2.5% |
| 2007 | +14.0% | +5.1% | +8.8% |
| 2008 | -18.6% | -36.8% | +18.2% |
| 2009 | +76.5% | +26.4% | +50.2% |
| 2010 | +12.7% | +15.1% | -2.4% |
| 2011 | -6.4% | +1.9% | -8.3% |
| 2012 | +13.3% | +16.0% | -2.7% |
| 2013 | +54.5% | +32.3% | +22.2% |
| 2014 | -3.7% | +13.5% | -17.1% |
| 2015 | -11.1% | +1.2% | -12.3% |
| 2016 | +7.3% | +12.0% | -4.7% |
| 2017 | +31.3% | +21.7% | +9.6% |
| 2018 | +29.9% | -4.6% | +34.5% |
| 2019 | +25.5% | +31.2% | -5.7% |
| 2020 | +131.0% | +18.3% | +112.7% |
| 2021 | +32.6% | +28.7% | +3.9% |
| 2022 | -6.0% | -18.2% | +12.1% |
| 2023 | +0.8% | +26.2% | -25.4% |
| 2024 | +6.4% | +24.9% | -18.5% |
| 2025 | +88.8% | +17.7% | +71.1% |
| 2026 | +17.7% | +13.7% | +4.0% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 1 | +4.5% | +4.5% | 100% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-29 | [[AEYE]] | [[HAWKINS JAMES B]] | $37K | 21 | – | pending |
| 2026-10-28 | [[ACN]] | [[Sweet Julie Spellman]] | $3.0M | 78 | +3.2% | open |
| 2026-10-28 | [[ACN]] | [[Price Paula A]] | $200K | 46 | +3.2% | open |
| 2026-10-23 | [[BZUN]] | [[Qiu Wenbin]] | $40K | 33 | -6.8% | open |
| 2026-10-20 | [[XGN]] | [[Chernett Jorey]] | $104K | 20 | +16.9% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "momentum_buy")
SORT filed DESC
```

Back to [[What Works]].
