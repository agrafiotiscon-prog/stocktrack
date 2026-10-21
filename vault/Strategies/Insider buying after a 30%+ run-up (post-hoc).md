---
type: "strategy"
key: "momentum_buy"
signals: 3936
cagr: 0.201758
spy_cagr: 0.110437
sharpe: 0.834081
max_drawdown: 0.401829
holdout_excess: 0.217221
---

# Insider buying after a 30%+ run-up (post-hoc)

Rule key: `momentum_buy`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

> [!warning] Post-hoc idea
> This rule was written after seeing the backtest, so the backtest numbers below are in-sample and can't confirm it. Only the live forward test counts. See [[Findings]] and `data/backtest/hypotheses.json`.

## Backtest

| Measure | Value |
|---|---|
| Signals | 3,936 |
| 3-month excess vs SPY (mean / median) | +2.7% / -1.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +2.2% |
| vs surviving stocks | +3.4% |
| 2006-2015 excess /yr | +10.9% (p 0.117) |
| 2016+ excess /yr | +21.7% (p 0.021) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +12.0% | +11.0% | 0.65 | 0.55 | 47% | 0.47 | +6.3% | 33% | 2,009 | 6.5% | +8.3% / 0.59 / 31% |
| 63d | +20.2% | +11.0% | 0.83 | 0.55 | 40% | 0.92 | +10.5% | 57% | 1,236 | 3.1% | +13.7% / 0.80 / 25% |
| 126d | +17.3% | +11.0% | 0.62 | 0.55 | 56% | 1.14 | +7.5% | 57% | 749 | 2.0% | +10.4% / 0.49 / 38% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +22.3%/yr, double costs +17.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +9.9% | +13.3% | -3.4% |
| 2007 | +14.0% | +5.1% | +8.8% |
| 2008 | -18.6% | -36.8% | +18.2% |
| 2009 | +78.1% | +26.4% | +51.7% |
| 2010 | +16.1% | +15.1% | +1.0% |
| 2011 | -6.4% | +1.9% | -8.3% |
| 2012 | +13.0% | +16.0% | -3.0% |
| 2013 | +59.6% | +32.3% | +27.3% |
| 2014 | -3.7% | +13.5% | -17.2% |
| 2015 | -11.1% | +1.2% | -12.3% |
| 2016 | +8.5% | +12.0% | -3.4% |
| 2017 | +31.3% | +21.7% | +9.5% |
| 2018 | +29.9% | -4.6% | +34.5% |
| 2019 | +25.2% | +31.2% | -6.0% |
| 2020 | +129.7% | +18.3% | +111.3% |
| 2021 | +30.3% | +28.7% | +1.6% |
| 2022 | -8.4% | -18.2% | +9.8% |
| 2023 | +1.0% | +26.2% | -25.2% |
| 2024 | +6.4% | +24.9% | -18.5% |
| 2025 | +88.1% | +17.7% | +70.4% |
| 2026 | +15.9% | +13.3% | +2.6% |


## Live forward test

0 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-20 | [[XGN]] | [[Chernett Jorey]] | $104K | 20 | – | pending |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "momentum_buy")
SORT filed DESC
```

Back to [[What Works]].
