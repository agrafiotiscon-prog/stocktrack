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
| 5 sessions | 41 | -1.3% | +0.9% | 54% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-04 | [[ASPE]] | [[ORBIMED ADVISORS LLC]] | $15.0M | 80 | – | pending |
| 2026-11-04 | [[PAM]] | [[Zuberbuhler Adolfo Fernando]] | $207K | 55 | – | pending |
| 2026-11-04 | [[LRN]] | [[Shepherd Brian A]] | $1.7M | 66 | – | pending |
| 2026-11-04 | [[DOLE]] | [[Pale Fire Capital SE]] | $12.9M | 47 | – | pending |
| 2026-11-04 | [[HGV]] | [[Wang Mark D]] | $499K | 46 | – | pending |
| 2026-11-04 | [[JBLU]] | [[Mittal Nik]] | $324K | 59 | – | pending |
| 2026-11-04 | [[PRLB]] | [[Krishna Suresh]] | $52K | 49 | – | pending |
| 2026-11-04 | [[UPBD]] | [[Khouri Halim]] | $251K | 70 | – | pending |
| 2026-11-04 | [[UPBD]] | [[MARINO GLENN P]] | $393K | 73 | – | pending |
| 2026-11-04 | [[UPBD]] | [[Wooters Rebecca]] | $99K | 67 | – | pending |
| 2026-11-04 | [[UPBD]] | [[Kumar Balaji]] | $50K | 61 | – | pending |
| 2026-11-04 | [[UPBD]] | [[BROWN JEFFREY J]] | $400K | 65 | – | pending |
| 2026-11-04 | [[UPBD]] | [[LANGENSTEIN MOLLY]] | $50K | 64 | – | pending |
| 2026-11-04 | [[AN]] | [[EDMUNDS C COLEMAN]] | $101K | 48 | – | pending |
| 2026-11-04 | [[AN]] | [[Szlosek Thomas A]] | $300K | 65 | – | pending |
| 2026-11-04 | [[AN]] | [[Manley Michael Mark]] | $1.0M | 71 | – | pending |
| 2026-11-04 | [[CACC]] | [[TRYFOROS THOMAS N]] | $1.5M | 54 | – | pending |
| 2026-11-04 | [[LSCC]] | [[Tamer Ford]] | $1.0M | 65 | – | pending |
| 2026-11-04 | [[INTC]] | [[TAN LIP BU]] | $9.7M | 64 | – | pending |
| 2026-11-04 | [[SPTX]] | [[Torres Denice]] | $99K | 42 | – | pending |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_40")
SORT filed DESC
```

Back to [[What Works]].
