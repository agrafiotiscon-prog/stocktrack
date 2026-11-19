---
type: "strategy"
key: "momentum_buy"
signals: 3931
cagr: 0.196106
spy_cagr: 0.107555
sharpe: 0.809048
max_drawdown: 0.401829
holdout_excess: 0.211818
---

# Insider buying after a 30%+ run-up (post-hoc)

Rule key: `momentum_buy`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

> [!warning] Post-hoc idea
> This rule was written after seeing the backtest, so the backtest numbers below are in-sample and can't confirm it. Only the live forward test counts. See [[Findings]] and `data/backtest/hypotheses.json`.

## Backtest

| Measure | Value |
|---|---|
| Signals | 3,931 |
| 3-month excess vs SPY (mean / median) | +2.6% / -2.0% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +2.1% |
| vs surviving stocks | +3.1% |
| 2006-2015 excess /yr | +9.6% (p 0.161) |
| 2016+ excess /yr | +21.2% (p 0.027) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +11.2% | +10.8% | 0.61 | 0.54 | 48% | 0.48 | +5.5% | 29% | 2,015 | 6.4% | +7.7% / 0.54 / 31% |
| 63d | +19.6% | +10.8% | 0.81 | 0.54 | 40% | 0.95 | +10.0% | 52% | 1,235 | 3.1% | +13.2% / 0.76 / 27% |
| 126d | +14.4% | +10.8% | 0.55 | 0.54 | 56% | 1.17 | +3.9% | 52% | 747 | 2.0% | +7.9% / 0.42 / 38% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +21.8%/yr, double costs +16.5%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +12.1% | +13.3% | -1.2% |
| 2007 | +15.2% | +5.1% | +10.1% |
| 2008 | -18.6% | -36.8% | +18.2% |
| 2009 | +76.4% | +26.4% | +50.1% |
| 2010 | +11.3% | +15.1% | -3.8% |
| 2011 | -6.4% | +1.9% | -8.3% |
| 2012 | +13.0% | +16.0% | -3.0% |
| 2013 | +54.5% | +32.3% | +22.2% |
| 2014 | -3.7% | +13.5% | -17.1% |
| 2015 | -11.1% | +1.2% | -12.3% |
| 2016 | +6.3% | +12.0% | -5.7% |
| 2017 | +31.3% | +21.7% | +9.6% |
| 2018 | +29.9% | -4.6% | +34.5% |
| 2019 | +25.5% | +31.2% | -5.7% |
| 2020 | +124.2% | +18.3% | +105.8% |
| 2021 | +31.3% | +28.7% | +2.6% |
| 2022 | -7.1% | -18.2% | +11.1% |
| 2023 | +1.4% | +26.2% | -24.7% |
| 2024 | +6.4% | +24.9% | -18.5% |
| 2025 | +91.2% | +17.7% | +73.5% |
| 2026 | +12.5% | +8.2% | +4.2% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 12 | +0.9% | +3.0% | 58% |
| 21 sessions | 1 | -42.4% | -42.4% | 0% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-18 | [[SJT]] | [[OLIVER ERIC L]] | $2.6M | 41 | – | pending |
| 2026-11-17 | [[BOLT]] | [[Coastlands Capital LP]] | $310K | 32 | -9.0% | open |
| 2026-11-12 | [[OBIO]] | [[RTW INVESTMENTS, LP]] | $6.0M | 71 | +23.3% | open |
| 2026-11-10 | [[UPBD]] | [[Young Scott A]] | $150K | 75 | +10.0% | open |
| 2026-11-10 | [[BOLT]] | [[Coastlands Capital LP]] | $319K | 33 | -16.5% | open |
| 2026-11-09 | [[LAW]] | [[Friedrichsen Eric]] | $24K | 30 | +7.9% | open |
| 2026-11-09 | [[UPBD]] | [[Karam Fahmi]] | $300K | 71 | +8.3% | open |
| 2026-11-09 | [[EAF]] | [[Shivaram Sachin M]] | $50K | 39 | -18.8% | open |
| 2026-11-06 | [[KOD]] | [[BAKER BROS. ADVISORS LP]] | $24.3M | 45 | -2.3% | open |
| 2026-11-04 | [[AEYE]] | [[HAWKINS JAMES B]] | $38K | 21 | -10.2% | open |
| 2026-11-02 | [[AEYE]] | [[HAWKINS JAMES B]] | $53K | 23 | -14.7% | open |
| 2026-10-29 | [[AEYE]] | [[HAWKINS JAMES B]] | $37K | 21 | -17.2% | open |
| 2026-10-28 | [[ACN]] | [[Sweet Julie Spellman]] | $3.0M | 78 | +0.1% | open |
| 2026-10-28 | [[ACN]] | [[Price Paula A]] | $200K | 46 | +0.1% | open |
| 2026-10-23 | [[BZUN]] | [[Qiu Wenbin]] | $40K | 33 | -3.6% | open |
| 2026-10-20 | [[XGN]] | [[Chernett Jorey]] | $104K | 20 | -42.4% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "momentum_buy")
SORT filed DESC
```

Back to [[What Works]].
