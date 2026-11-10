---
type: "strategy"
key: "contrarian"
signals: 8129
cagr: 0.0201999
spy_cagr: 0.108977
sharpe: 0.184406
max_drawdown: 0.72189
holdout_excess: -0.0582479
---

# Insider buying after a 30%+ drop

Rule key: `contrarian`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 8,129 |
| 3-month excess vs SPY (mean / median) | +5.2% / +2.1% |
| Beat SPY over 3 months | 53% |
| Entering one session later | +4.8% |
| vs surviving stocks | +3.9% |
| 2006-2015 excess /yr | +14.1% (p 0.139) |
| 2016+ excess /yr | -5.8% (p 0.406) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +2.5% | +10.9% | 0.18 | 0.55 | 72% | 1.14 | -6.9% | 33% | 2,244 | 6.1% | +1.0% / 0.05 / 67% |
| 63d | +2.0% | +10.9% | 0.18 | 0.55 | 72% | 1.58 | -9.4% | 29% | 1,181 | 3.3% | -1.8% / -0.07 / 66% |
| 126d | +6.9% | +10.9% | 0.32 | 0.55 | 67% | 1.62 | -5.4% | 48% | 715 | 2.0% | +1.3% / 0.08 / 67% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +5.3%/yr, double costs -1.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +22.1% | +9.7% | +12.4% |
| 2007 | +6.6% | +5.1% | +1.4% |
| 2008 | -44.2% | -36.8% | -7.5% |
| 2009 | +25.0% | +26.4% | -1.4% |
| 2010 | +21.5% | +15.1% | +6.4% |
| 2011 | -8.2% | +1.9% | -10.1% |
| 2012 | +29.1% | +16.0% | +13.1% |
| 2013 | +24.0% | +32.3% | -8.3% |
| 2014 | -2.0% | +13.5% | -15.5% |
| 2015 | -21.6% | +1.2% | -22.8% |
| 2016 | +38.9% | +12.0% | +26.9% |
| 2017 | +15.0% | +21.7% | -6.7% |
| 2018 | -12.1% | -4.6% | -7.5% |
| 2019 | +40.5% | +31.2% | +9.3% |
| 2020 | +11.1% | +18.3% | -7.3% |
| 2021 | -10.2% | +28.7% | -38.9% |
| 2022 | -45.3% | -18.2% | -27.1% |
| 2023 | +10.2% | +26.2% | -15.9% |
| 2024 | -5.1% | +24.9% | -29.9% |
| 2025 | +4.6% | +17.7% | -13.1% |
| 2026 | +2.9% | +11.5% | -8.6% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 14 | +0.0% | +1.6% | 57% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-10 | [[MX]] | [[LEE CHAE]] | $155K | 49 | – | pending |
| 2026-11-09 | [[NXRT]] | [[McGraner Matt]] | $199K | 44 | – | pending |
| 2026-11-09 | [[NXRT]] | [[Richards Paul]] | $103K | 49 | – | pending |
| 2026-11-09 | [[ADTN]] | [[Santo Timothy P]] | $74K | 58 | – | pending |
| 2026-11-09 | [[ADTN]] | [[STANTON THOMAS R]] | $601K | 65 | – | pending |
| 2026-11-09 | [[NATR]] | [[PRESCOTT GROUP CAPITAL MANAGEMENT, L.L.C]] | $2.8M | 44 | – | pending |
| 2026-11-09 | [[FUN]] | [[Bennett Christopher Lawrence]] | $47K | 34 | – | pending |
| 2026-11-09 | [[LUMN]] | [[Johnson Kathleen E]] | $397K | 73 | – | pending |
| 2026-11-09 | [[LUMN]] | [[GOLDBERG MICHELLE J]] | $98K | 50 | – | pending |
| 2026-11-09 | [[CPS]] | [[Banas Jonathan P]] | $17K | 28 | – | pending |
| 2026-11-09 | [[NSLR]] | [[Potter Leonard]] | $115K | 35 | – | pending |
| 2026-11-09 | [[TTMI]] | [[FRANKLIN PHILIP G]] | $310K | 52 | – | pending |
| 2026-11-06 | [[FICO]] | [[Rey David A]] | $20K | 7 | +1.3% | open |
| 2026-11-06 | [[ROAD]] | [[Skelly Noreen E]] | $8K | 17 | +4.2% | open |
| 2026-11-06 | [[TBBK]] | [[Mudick Stephanie B]] | $47K | 35 | -0.4% | open |
| 2026-11-06 | [[PMN]] | [[Williams Eugene]] | $91K | 54 | -5.9% | open |
| 2026-11-06 | [[AGMB]] | [[Epstein David R]] | $104K | 42 | -3.6% | open |
| 2026-11-05 | [[COUR]] | [[Pale Fire Capital SE]] | $31.5M | 53 | -6.3% | open |
| 2026-11-05 | [[LBRT]] | [[Gosney Ryan T]] | $45K | 48 | +5.6% | open |
| 2026-11-05 | [[LBRT]] | [[Gusek Ron]] | $377K | 65 | +5.6% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "contrarian")
SORT filed DESC
```

Back to [[What Works]].
