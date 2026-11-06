---
type: "strategy"
key: "score_40"
signals: 32309
cagr: 0.0587494
spy_cagr: 0.109572
sharpe: 0.283645
max_drawdown: 0.574297
holdout_excess: 0.0134349
---

# Live score 40+ (notable)

Rule key: `score_40`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 32,309 |
| 3-month excess vs SPY (mean / median) | +1.1% / -0.6% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.8% |
| vs surviving stocks | +1.2% |
| 2006-2015 excess /yr | +7.9% (p 0.011) |
| 2016+ excess /yr | +1.3% (p 0.749) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.5% | +11.0% | 0.31 | 0.55 | 57% | 1.26 | -4.6% | 33% | 4,878 | 8.6% | -1.0% / -0.12 / 61% |
| 63d | +5.9% | +11.0% | 0.28 | 0.55 | 57% | 1.24 | -5.2% | 38% | 1,660 | 2.6% | -2.0% / -0.20 / 59% |
| 126d | +4.9% | +11.0% | 0.25 | 0.55 | 68% | 1.20 | -5.7% | 29% | 840 | 1.3% | -3.1% / -0.29 / 57% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +8.6%/yr, double costs +3.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +12.7% | +13.8% | -1.1% |
| 2007 | -11.1% | +5.1% | -16.2% |
| 2008 | -19.3% | -36.8% | +17.5% |
| 2009 | +36.1% | +26.4% | +9.7% |
| 2010 | +31.8% | +15.1% | +16.8% |
| 2011 | -13.7% | +1.9% | -15.6% |
| 2012 | +17.5% | +16.0% | +1.5% |
| 2013 | +35.5% | +32.3% | +3.2% |
| 2014 | +1.1% | +13.5% | -12.3% |
| 2015 | -10.7% | +1.2% | -11.9% |
| 2016 | +21.1% | +12.0% | +9.1% |
| 2017 | +19.2% | +21.7% | -2.5% |
| 2018 | -19.5% | -4.6% | -15.0% |
| 2019 | +45.6% | +31.2% | +14.4% |
| 2020 | +10.3% | +18.3% | -8.1% |
| 2021 | +4.0% | +28.7% | -24.7% |
| 2022 | -20.6% | -18.2% | -2.5% |
| 2023 | +30.0% | +26.2% | +3.8% |
| 2024 | -10.3% | +24.9% | -35.2% |
| 2025 | -7.5% | +17.7% | -25.2% |
| 2026 | +9.4% | +11.5% | -2.1% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 48 | -0.8% | +1.5% | 58% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-06 | [[AGMB]] | [[Epstein David R]] | $104K | 42 | – | pending |
| 2026-11-05 | [[FLOC]] | [[Fairbanks Jonathan B]] | $293K | 47 | – | pending |
| 2026-11-05 | [[MTDR]] | [[Colodney Benjamin T]] | $26K | 40 | – | pending |
| 2026-11-05 | [[MTDR]] | [[Calvert Christopher P]] | $105K | 50 | – | pending |
| 2026-11-05 | [[BXMT]] | [[NASSAU HENRY N]] | $114K | 41 | – | pending |
| 2026-11-05 | [[BXMT]] | [[Johnson Timothy Steven]] | $1.0M | 69 | – | pending |
| 2026-11-05 | [[ETRA]] | [[ORBIMED ADVISORS LLC]] | $3.6M | 53 | – | pending |
| 2026-11-05 | [[LYEL]] | [[ARCH Venture Fund XIII, L.P]] | $25.0M | 58 | – | pending |
| 2026-11-05 | [[COUR]] | [[Pale Fire Capital SE]] | $31.5M | 53 | – | pending |
| 2026-11-05 | [[LBRT]] | [[Gosney Ryan T]] | $45K | 48 | – | pending |
| 2026-11-05 | [[LBRT]] | [[Gusek Ron]] | $377K | 65 | – | pending |
| 2026-11-05 | [[GLXY]] | [[Novogratz Michael]] | $9.9M | 75 | – | pending |
| 2026-11-05 | [[FBRT]] | [[Byrne Richard J]] | $998K | 65 | – | pending |
| 2026-11-05 | [[UPBD]] | [[Karam Fahmi]] | $100K | 64 | – | pending |
| 2026-11-05 | [[SYY]] | [[Ondrof Thomas Gerard]] | $192K | 45 | – | pending |
| 2026-11-05 | [[CLX]] | [[Breber Pierre R]] | $400K | 41 | – | pending |
| 2026-11-05 | [[SPXC]] | [[Deck Brian A]] | $493K | 49 | – | pending |
| 2026-11-05 | [[BKR]] | [[RICE JOHN G]] | $531K | 40 | – | pending |
| 2026-11-05 | [[TTMI]] | [[Ali Wajid]] | $632K | 57 | – | pending |
| 2026-11-05 | [[PAM]] | [[Mindlin Damian Miguel]] | $2.6M | 57 | – | pending |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_40")
SORT filed DESC
```

Back to [[What Works]].
