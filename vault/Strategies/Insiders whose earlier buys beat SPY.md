---
type: "strategy"
key: "proven_insider"
signals: 20084
cagr: 0.129009
spy_cagr: 0.11135
sharpe: 0.527923
max_drawdown: 0.601494
holdout_excess: 0.00385895
---

# Insiders whose earlier buys beat SPY

Rule key: `proven_insider`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 20,084 |
| 3-month excess vs SPY (mean / median) | +0.7% / -0.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +0.5% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +6.0% (p 0.022) |
| 2016+ excess /yr | +0.4% (p 0.906) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +7.6% | +11.1% | 0.35 | 0.56 | 52% | 1.09 | -3.0% | 29% | 4,538 | 8.6% | -0.5% / -0.14 / 45% |
| 63d | +12.9% | +11.1% | 0.53 | 0.56 | 60% | 1.22 | +0.9% | 48% | 1,612 | 3.1% | +4.3% / 0.27 / 30% |
| 126d | +9.1% | +11.1% | 0.41 | 0.56 | 57% | 1.12 | -1.8% | 43% | 817 | 1.5% | +0.5% / -0.04 / 39% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +16.3%/yr, double costs +9.4%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +15.5% | +13.9% | +1.7% |
| 2007 | +4.3% | +5.1% | -0.8% |
| 2008 | -19.2% | -36.8% | +17.6% |
| 2009 | +24.8% | +26.4% | -1.6% |
| 2010 | +42.2% | +15.1% | +27.1% |
| 2011 | +7.7% | +1.9% | +5.8% |
| 2012 | +14.9% | +16.0% | -1.1% |
| 2013 | +39.1% | +32.3% | +6.8% |
| 2014 | +13.8% | +13.5% | +0.3% |
| 2015 | -13.8% | +1.2% | -15.0% |
| 2016 | +25.3% | +12.0% | +13.3% |
| 2017 | +11.2% | +21.7% | -10.5% |
| 2018 | -12.9% | -4.6% | -8.3% |
| 2019 | +30.6% | +31.2% | -0.6% |
| 2020 | +38.8% | +18.3% | +20.5% |
| 2021 | +14.5% | +28.7% | -14.2% |
| 2022 | -25.4% | -18.2% | -7.2% |
| 2023 | +40.3% | +26.2% | +14.1% |
| 2024 | +15.7% | +24.9% | -9.2% |
| 2025 | +25.0% | +17.7% | +7.3% |
| 2026 | +6.9% | +10.8% | -3.9% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 56 | +2.5% | +2.6% | 75% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-10 | [[ETRA]] | [[ORBIMED ADVISORS LLC]] | $745K | 37 | – | pending |
| 2026-11-10 | [[XGN]] | [[Chernett Jorey]] | $91K | 20 | – | pending |
| 2026-11-10 | [[STLN]] | [[Chernett Jorey]] | $176K | 23 | – | pending |
| 2026-11-10 | [[NVT]] | [[Parker Herbert K]] | $339K | 39 | – | pending |
| 2026-11-10 | [[EGBN]] | [[Newell Eric R]] | $50K | 41 | – | pending |
| 2026-11-10 | [[TXO]] | [[SIMPSON BOB R]] | $3.1M | 41 | – | pending |
| 2026-11-10 | [[MCY]] | [[Braunegg George Gwyer]] | $50K | 43 | – | pending |
| 2026-11-10 | [[SPXC]] | [[Deck Brian A]] | $141K | 38 | – | pending |
| 2026-11-10 | [[BOLT]] | [[Coastlands Capital LP]] | $319K | 33 | – | pending |
| 2026-11-10 | [[OBK]] | [[Crotwell Jim]] | $107K | 36 | – | pending |
| 2026-11-10 | [[STRA]] | [[Thawley Michael]] | $98K | 45 | – | pending |
| 2026-11-10 | [[OSBC]] | [[Lyons Billy J Jr]] | $572 | 13 | – | pending |
| 2026-11-10 | [[BOTJ]] | [[ADDISON LEWIS C]] | $2K | 14 | – | pending |
| 2026-11-10 | [[GOOD]] | [[Gerson Gary]] | $86K | 60 | – | pending |
| 2026-11-10 | [[MTDR]] | [[Ehrman Monika U]] | $17K | 42 | – | pending |
| 2026-11-10 | [[CRH]] | [[FEARON RICHARD H]] | $570K | 47 | – | pending |
| 2026-11-10 | [[LBTYA]] | [[MALONE JOHN C]] | $1.5M | 53 | – | pending |
| 2026-11-09 | [[NXRT]] | [[McGraner Matt]] | $199K | 44 | -0.5% | open |
| 2026-11-09 | [[NXRT]] | [[Richards Paul]] | $103K | 49 | -0.5% | open |
| 2026-11-09 | [[GFS]] | [[LAZAR JACK R]] | $380K | 57 | +1.3% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "proven_insider")
SORT filed DESC
```

Back to [[What Works]].
