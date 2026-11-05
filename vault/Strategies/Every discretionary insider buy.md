---
type: "strategy"
key: "all_liquid"
signals: 67450
cagr: 0.0488947
spy_cagr: 0.109572
sharpe: 0.248503
max_drawdown: 0.595342
holdout_excess: 0.00124979
---

# Every discretionary insider buy

Rule key: `all_liquid`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 67,450 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.8% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.6% |
| vs surviving stocks | +1.0% |
| 2006-2015 excess /yr | +6.4% (p 0.018) |
| 2016+ excess /yr | +0.1% (p 0.972) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.4% | +11.0% | 0.30 | 0.55 | 61% | 1.25 | -4.6% | 38% | 4,984 | 9.1% | -1.9% / -0.19 / 68% |
| 63d | +4.9% | +11.0% | 0.25 | 0.55 | 60% | 1.15 | -5.8% | 48% | 1,668 | 2.6% | -3.4% / -0.35 / 69% |
| 126d | +7.1% | +11.0% | 0.33 | 0.55 | 54% | 1.15 | -3.8% | 33% | 840 | 1.5% | -1.7% / -0.18 / 56% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +7.9%/yr, double costs +2.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +24.3% | +13.8% | +10.4% |
| 2007 | -7.9% | +5.1% | -13.0% |
| 2008 | -24.8% | -36.8% | +12.0% |
| 2009 | +53.0% | +26.4% | +26.7% |
| 2010 | +20.4% | +15.1% | +5.4% |
| 2011 | -10.5% | +1.9% | -12.4% |
| 2012 | +23.7% | +16.0% | +7.7% |
| 2013 | +39.0% | +32.3% | +6.7% |
| 2014 | +1.8% | +13.5% | -11.7% |
| 2015 | +6.1% | +1.2% | +4.8% |
| 2016 | +15.1% | +12.0% | +3.1% |
| 2017 | +23.8% | +21.7% | +2.1% |
| 2018 | -10.3% | -4.6% | -5.7% |
| 2019 | +8.0% | +31.2% | -23.2% |
| 2020 | +36.1% | +18.3% | +17.8% |
| 2021 | -6.1% | +28.7% | -34.9% |
| 2022 | -36.1% | -18.2% | -17.9% |
| 2023 | +25.3% | +26.2% | -0.9% |
| 2024 | -15.0% | +24.9% | -39.9% |
| 2025 | -14.4% | +17.7% | -32.1% |
| 2026 | -0.5% | +11.5% | -12.0% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 106 | +0.9% | +1.7% | 65% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-04 | [[ASPE]] | [[ORBIMED ADVISORS LLC]] | $15.0M | 80 | – | pending |
| 2026-11-04 | [[PAM]] | [[Zuberbuhler Adolfo Fernando]] | $207K | 55 | – | pending |
| 2026-11-04 | [[CRBG]] | [[NIPPON LIFE INSURANCE CO]] | $6.7M | 22 | – | pending |
| 2026-11-04 | [[JBSS]] | [[Finn Michael J]] | $16K | 22 | – | pending |
| 2026-11-04 | [[LRN]] | [[Shepherd Brian A]] | $1.7M | 66 | – | pending |
| 2026-11-04 | [[LYCA]] | [[Venrock Healthcare Capital Partners III, L.P]] | $224K | 22 | – | pending |
| 2026-11-04 | [[DOLE]] | [[Pale Fire Capital SE]] | $12.9M | 47 | – | pending |
| 2026-11-04 | [[HGV]] | [[Potter Leonard]] | $104K | 39 | – | pending |
| 2026-11-04 | [[HGV]] | [[Wang Mark D]] | $499K | 46 | – | pending |
| 2026-11-04 | [[JBLU]] | [[Mittal Nik]] | $324K | 59 | – | pending |
| 2026-11-04 | [[PRLB]] | [[Krishna Suresh]] | $52K | 49 | – | pending |
| 2026-11-04 | [[PRLB]] | [[Gawlick Rainer]] | $49K | 34 | – | pending |
| 2026-11-04 | [[UPBD]] | [[Khouri Halim]] | $251K | 70 | – | pending |
| 2026-11-04 | [[UPBD]] | [[MARINO GLENN P]] | $393K | 73 | – | pending |
| 2026-11-04 | [[FBRT]] | [[ORTALE BUFORD H]] | $5K | 15 | – | pending |
| 2026-11-04 | [[UPBD]] | [[Wooters Rebecca]] | $99K | 67 | – | pending |
| 2026-11-04 | [[UPBD]] | [[Kumar Balaji]] | $50K | 61 | – | pending |
| 2026-11-04 | [[UPBD]] | [[BROWN JEFFREY J]] | $400K | 65 | – | pending |
| 2026-11-04 | [[UPBD]] | [[LANGENSTEIN MOLLY]] | $50K | 64 | – | pending |
| 2026-11-04 | [[AEYE]] | [[HAWKINS JAMES B]] | $38K | 21 | – | pending |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "all_liquid")
SORT filed DESC
```

Back to [[What Works]].
