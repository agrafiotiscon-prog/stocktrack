---
type: "strategy"
key: "proven_insider"
signals: 20141
cagr: 0.124546
spy_cagr: 0.111785
sharpe: 0.510198
max_drawdown: 0.614357
holdout_excess: 0.004467
---

# Insiders whose earlier buys beat SPY

Rule key: `proven_insider`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 20,141 |
| 3-month excess vs SPY (mean / median) | +0.7% / -0.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +0.6% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +6.1% (p 0.018) |
| 2016+ excess /yr | +0.4% (p 0.892) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +7.8% | +11.2% | 0.36 | 0.56 | 52% | 1.10 | -2.9% | 33% | 4,541 | 8.6% | -0.3% / -0.12 / 46% |
| 63d | +12.5% | +11.2% | 0.51 | 0.56 | 61% | 1.23 | +0.5% | 52% | 1,613 | 3.2% | +3.9% / 0.24 / 39% |
| 126d | +8.9% | +11.2% | 0.40 | 0.56 | 57% | 1.15 | -2.3% | 38% | 818 | 1.5% | +0.4% / -0.05 / 44% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +15.8%/yr, double costs +9.1%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.9% | +13.9% | +3.0% |
| 2007 | +1.5% | +5.1% | -3.6% |
| 2008 | -22.3% | -36.8% | +14.5% |
| 2009 | +23.9% | +26.4% | -2.5% |
| 2010 | +33.4% | +15.1% | +18.3% |
| 2011 | +11.4% | +1.9% | +9.5% |
| 2012 | +15.6% | +16.0% | -0.4% |
| 2013 | +33.3% | +32.3% | +1.0% |
| 2014 | +17.6% | +13.5% | +4.2% |
| 2015 | -15.7% | +1.2% | -16.9% |
| 2016 | +20.7% | +12.0% | +8.7% |
| 2017 | +8.7% | +21.7% | -13.0% |
| 2018 | -13.9% | -4.6% | -9.3% |
| 2019 | +28.7% | +31.2% | -2.6% |
| 2020 | +33.0% | +18.3% | +14.7% |
| 2021 | +13.7% | +28.7% | -15.1% |
| 2022 | -27.8% | -18.2% | -9.6% |
| 2023 | +37.9% | +26.2% | +11.8% |
| 2024 | +21.8% | +24.9% | -3.1% |
| 2025 | +38.3% | +17.7% | +20.5% |
| 2026 | +14.9% | +11.5% | +3.4% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 31 | +3.1% | +2.8% | 87% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-04 | [[ASPE]] | [[ORBIMED ADVISORS LLC]] | $15.0M | 80 | – | pending |
| 2026-11-04 | [[UPBD]] | [[BROWN JEFFREY J]] | $400K | 65 | – | pending |
| 2026-11-04 | [[UMBF]] | [[Peterman Tamara]] | $27K | 32 | – | pending |
| 2026-11-04 | [[AN]] | [[Szlosek Thomas A]] | $300K | 65 | – | pending |
| 2026-11-04 | [[INTC]] | [[TAN LIP BU]] | $9.7M | 64 | – | pending |
| 2026-11-03 | [[SIRI]] | [[BERKSHIRE HATHAWAY INC]] | $26.9M | 40 | +5.6% | open |
| 2026-11-03 | [[NPKI]] | [[MINGE JOHN C]] | $139K | 30 | -4.3% | open |
| 2026-11-03 | [[SITE]] | [[BLACK DOUG]] | $1.0M | 62 | +0.1% | open |
| 2026-11-03 | [[JOF]] | [[Saba Capital Management, L.P]] | $30K | 14 | -0.5% | open |
| 2026-11-03 | [[RNST]] | [[LEVY JONATHAN A]] | $82K | 41 | -1.2% | open |
| 2026-11-03 | [[MGM]] | [[Meister Keith A]] | $51.7M | 58 | +1.3% | open |
| 2026-11-03 | [[LKQ]] | [[CLARKE ANDREW C]] | $400K | 60 | +3.1% | open |
| 2026-11-03 | [[FISI]] | [[DORN ANDREW W JR]] | $63K | 26 | -0.6% | open |
| 2026-11-03 | [[IBKR]] | [[Conkling Lori A]] | $2K | 0 | -0.3% | open |
| 2026-11-02 | [[NTRS]] | [[Moritz Robert Edward Jr]] | $40K | 23 | +1.9% | open |
| 2026-11-02 | [[JOF]] | [[Saba Capital Management, L.P]] | $702K | 31 | -2.1% | open |
| 2026-11-02 | [[ROL]] | [[LOR INC]] | $50.0M | 41 | +3.3% | open |
| 2026-11-02 | [[JBLU]] | [[BONEPARTH PETER]] | $300K | 47 | +6.7% | open |
| 2026-11-02 | [[ENPH]] | [[Kothandaraman Badrinarayanan]] | $268K | 41 | +9.7% | open |
| 2026-11-02 | [[BANC]] | [[WOLFF JARED M]] | $100K | 39 | -1.7% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "proven_insider")
SORT filed DESC
```

Back to [[What Works]].
