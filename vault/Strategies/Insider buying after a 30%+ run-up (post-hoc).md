---
type: "strategy"
key: "momentum_buy"
signals: 3929
cagr: 0.19979
spy_cagr: 0.108918
sharpe: 0.823622
max_drawdown: 0.401829
holdout_excess: 0.208759
---

# Insider buying after a 30%+ run-up (post-hoc)

Rule key: `momentum_buy`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

> [!warning] Post-hoc idea
> This rule was written after seeing the backtest, so the backtest numbers below are in-sample and can't confirm it. Only the live forward test counts. See [[Findings]] and `data/backtest/hypotheses.json`.

## Backtest

| Measure | Value |
|---|---|
| Signals | 3,929 |
| 3-month excess vs SPY (mean / median) | +2.6% / -1.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +2.2% |
| vs surviving stocks | +3.2% |
| 2006-2015 excess /yr | +9.3% (p 0.173) |
| 2016+ excess /yr | +20.9% (p 0.027) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +11.9% | +10.9% | 0.65 | 0.55 | 48% | 0.48 | +6.1% | 33% | 2,010 | 6.5% | +8.2% / 0.58 / 31% |
| 63d | +20.0% | +10.9% | 0.82 | 0.55 | 40% | 0.94 | +10.3% | 52% | 1,232 | 3.1% | +13.4% / 0.77 / 26% |
| 126d | +14.0% | +10.9% | 0.54 | 0.55 | 56% | 1.17 | +3.4% | 52% | 747 | 2.0% | +7.3% / 0.39 / 37% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +22.2%/yr, double costs +17.3%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +11.9% | +13.3% | -1.4% |
| 2007 | +14.2% | +5.1% | +9.1% |
| 2008 | -18.6% | -36.8% | +18.2% |
| 2009 | +78.3% | +26.4% | +52.0% |
| 2010 | +11.4% | +15.1% | -3.7% |
| 2011 | -6.4% | +1.9% | -8.3% |
| 2012 | +13.0% | +16.0% | -3.0% |
| 2013 | +54.5% | +32.3% | +22.2% |
| 2014 | -5.7% | +13.5% | -19.1% |
| 2015 | -11.4% | +1.2% | -12.6% |
| 2016 | +7.9% | +12.0% | -4.1% |
| 2017 | +31.3% | +21.7% | +9.6% |
| 2018 | +29.9% | -4.6% | +34.5% |
| 2019 | +25.5% | +31.2% | -5.7% |
| 2020 | +131.3% | +18.3% | +112.9% |
| 2021 | +31.2% | +28.7% | +2.5% |
| 2022 | -7.1% | -18.2% | +11.1% |
| 2023 | +0.4% | +26.2% | -25.8% |
| 2024 | +6.4% | +24.9% | -18.5% |
| 2025 | +90.6% | +17.7% | +72.9% |
| 2026 | +18.4% | +10.8% | +7.6% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 6 | +0.3% | +4.5% | 50% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-10 | [[UPBD]] | [[Young Scott A]] | $150K | 75 | +1.6% | open |
| 2026-11-10 | [[BOLT]] | [[Coastlands Capital LP]] | $319K | 33 | -2.3% | open |
| 2026-11-09 | [[LAW]] | [[Friedrichsen Eric]] | $24K | 30 | +6.7% | open |
| 2026-11-09 | [[UPBD]] | [[Karam Fahmi]] | $300K | 71 | -0.1% | open |
| 2026-11-09 | [[EAF]] | [[Shivaram Sachin M]] | $50K | 39 | +6.2% | open |
| 2026-11-06 | [[KOD]] | [[BAKER BROS. ADVISORS LP]] | $24.3M | 45 | +5.1% | open |
| 2026-11-04 | [[AEYE]] | [[HAWKINS JAMES B]] | $38K | 21 | +7.4% | open |
| 2026-11-02 | [[AEYE]] | [[HAWKINS JAMES B]] | $53K | 23 | +2.1% | open |
| 2026-10-29 | [[AEYE]] | [[HAWKINS JAMES B]] | $37K | 21 | -1.2% | open |
| 2026-10-28 | [[ACN]] | [[Sweet Julie Spellman]] | $3.0M | 78 | +7.2% | open |
| 2026-10-28 | [[ACN]] | [[Price Paula A]] | $200K | 46 | +7.2% | open |
| 2026-10-23 | [[BZUN]] | [[Qiu Wenbin]] | $40K | 33 | +1.3% | open |
| 2026-10-20 | [[XGN]] | [[Chernett Jorey]] | $104K | 20 | -31.0% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "momentum_buy")
SORT filed DESC
```

Back to [[What Works]].
