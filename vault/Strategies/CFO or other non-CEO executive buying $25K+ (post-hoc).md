---
type: "strategy"
key: "cfo_exec_25k"
signals: 8023
cagr: 0.137792
spy_cagr: 0.109148
sharpe: 0.548309
max_drawdown: 0.564709
holdout_excess: 0.0500228
---

# CFO or other non-CEO executive buying $25K+ (post-hoc)

Rule key: `cfo_exec_25k`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

> [!warning] Post-hoc idea
> This rule was written after seeing the backtest, so the backtest numbers below are in-sample and can't confirm it. Only the live forward test counts. See [[Findings]] and `data/backtest/hypotheses.json`.

## Backtest

| Measure | Value |
|---|---|
| Signals | 8,023 |
| 3-month excess vs SPY (mean / median) | +2.0% / -0.1% |
| Beat SPY over 3 months | 50% |
| Entering one session later | +1.6% |
| vs surviving stocks | +2.2% |
| 2006-2015 excess /yr | +8.8% (p 0.040) |
| 2016+ excess /yr | +5.0% (p 0.179) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.9% | +10.9% | 0.33 | 0.55 | 50% | 0.92 | -2.2% | 29% | 3,684 | 6.6% | +1.4% / 0.03 / 38% |
| 63d | +13.8% | +10.9% | 0.55 | 0.55 | 56% | 1.22 | +2.0% | 57% | 1,636 | 3.1% | +5.4% / 0.34 / 20% |
| 126d | +12.3% | +10.9% | 0.50 | 0.55 | 59% | 1.20 | +0.9% | 48% | 831 | 1.5% | +3.8% / 0.22 / 22% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +16.6%/yr, double costs +11.0%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +19.2% | +13.8% | +5.4% |
| 2007 | +0.7% | +5.1% | -4.4% |
| 2008 | -32.0% | -36.8% | +4.8% |
| 2009 | +91.1% | +26.4% | +64.7% |
| 2010 | +30.2% | +15.1% | +15.2% |
| 2011 | -12.3% | +1.9% | -14.2% |
| 2012 | +22.1% | +16.0% | +6.1% |
| 2013 | +43.2% | +32.3% | +10.9% |
| 2014 | +1.6% | +13.5% | -11.9% |
| 2015 | -2.8% | +1.2% | -4.0% |
| 2016 | +22.5% | +12.0% | +10.5% |
| 2017 | +17.3% | +21.7% | -4.4% |
| 2018 | -12.6% | -4.6% | -8.1% |
| 2019 | +43.3% | +31.2% | +12.1% |
| 2020 | +17.3% | +18.3% | -1.0% |
| 2021 | +29.1% | +28.7% | +0.4% |
| 2022 | -10.6% | -18.2% | +7.5% |
| 2023 | +19.8% | +26.2% | -6.4% |
| 2024 | +32.7% | +24.9% | +7.8% |
| 2025 | +20.4% | +17.7% | +2.7% |
| 2026 | +2.5% | +10.8% | -8.3% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 10 | +2.9% | +3.4% | 80% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-10 | [[EGBN]] | [[Newell Eric R]] | $50K | 41 | – | pending |
| 2026-11-10 | [[UPBD]] | [[Young Scott A]] | $150K | 75 | – | pending |
| 2026-11-10 | [[EMN]] | [[McAlindon Julie A]] | $160K | 36 | – | pending |
| 2026-11-10 | [[OBK]] | [[Crotwell Jim]] | $107K | 36 | – | pending |
| 2026-11-10 | [[GOOD]] | [[Gerson Gary]] | $86K | 60 | – | pending |
| 2026-11-09 | [[NXRT]] | [[McGraner Matt]] | $199K | 44 | -0.5% | open |
| 2026-11-09 | [[NXRT]] | [[Richards Paul]] | $103K | 49 | -0.5% | open |
| 2026-11-09 | [[ADTN]] | [[Santo Timothy P]] | $74K | 58 | -3.6% | open |
| 2026-11-09 | [[MTDR]] | [[Stetson Glenn W]] | $51K | 53 | +2.8% | open |
| 2026-11-09 | [[WCC]] | [[Marino Anthony S]] | $100K | 52 | -1.0% | open |
| 2026-11-09 | [[WCC]] | [[Dev Indraneel]] | $504K | 60 | -1.0% | open |
| 2026-11-09 | [[FUN]] | [[Bennett Christopher Lawrence]] | $47K | 34 | -5.8% | open |
| 2026-11-09 | [[OBIO]] | [[Hochman David P]] | $25K | 41 | -2.0% | open |
| 2026-11-09 | [[DKNG]] | [[Ellingson Alan Wayne]] | $350K | 46 | +3.7% | open |
| 2026-11-09 | [[AN]] | [[Szlosek Thomas A]] | $200K | 67 | -1.5% | open |
| 2026-11-09 | [[SOPH]] | [[CARDOZA GEORGE]] | $141K | 53 | -0.8% | open |
| 2026-11-09 | [[PAM]] | [[Mindlin Damian Miguel]] | $1.3M | 52 | -1.3% | open |
| 2026-11-09 | [[KMT]] | [[Watson Patrick S]] | $47K | 45 | -0.0% | open |
| 2026-11-06 | [[CVS]] | [[Shah Prem S]] | $2.0M | 54 | +4.1% | open |
| 2026-11-06 | [[KYN]] | [[Little Harrison James]] | $52K | 45 | +1.3% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "cfo_exec_25k")
SORT filed DESC
```

Back to [[What Works]].
