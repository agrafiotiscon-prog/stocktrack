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
| 5 sessions | 8 | -2.8% | -1.0% | 38% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-04 | [[JBSS]] | [[Finn Michael J]] | $16K | 22 | – | pending |
| 2026-11-04 | [[JBLU]] | [[Mittal Nik]] | $324K | 59 | – | pending |
| 2026-11-04 | [[TBBK]] | [[Cohn Matthew]] | $46K | 22 | – | pending |
| 2026-11-04 | [[INTC]] | [[TAN LIP BU]] | $9.7M | 64 | – | pending |
| 2026-11-03 | [[NPKI]] | [[MINGE JOHN C]] | $139K | 30 | -4.3% | open |
| 2026-11-03 | [[MGM]] | [[Meister Keith A]] | $51.7M | 58 | +1.3% | open |
| 2026-11-03 | [[PMN]] | [[Williams Eugene]] | $5K | 33 | +2.7% | open |
| 2026-11-03 | [[PMN]] | [[Cashman Neil]] | $39K | 44 | +2.7% | open |
| 2026-11-02 | [[RSI]] | [[Winter Thomas]] | $118K | 42 | +1.8% | open |
| 2026-11-02 | [[JBLU]] | [[BONEPARTH PETER]] | $300K | 47 | +6.7% | open |
| 2026-11-02 | [[ENPH]] | [[Kothandaraman Badrinarayanan]] | $268K | 41 | +9.7% | open |
| 2026-11-02 | [[HDSN]] | [[Hartree Partners, LP]] | $1.3M | 36 | +0.2% | open |
| 2026-11-02 | [[PUMP]] | [[Weatherl Caleb Lyle]] | $16K | 32 | -11.3% | open |
| 2026-10-30 | [[RAPP]] | [[HEALY JAMES]] | $20.4M | 87 | +2.1% | open |
| 2026-10-27 | [[STC]] | [[Matz Deborah Jane]] | $44K | 63 | +7.8% | open |
| 2026-10-27 | [[STC]] | [[EPPINGER FREDERICK H]] | $133K | 65 | +7.8% | open |
| 2026-10-26 | [[GPI]] | [[Conifer Management, L.L.C]] | $24.2M | 44 | +10.2% | open |
| 2026-10-26 | [[STC]] | [[Apel Thomas G]] | $95K | 48 | +7.4% | open |
| 2026-10-26 | [[STC]] | [[Corey William S. Jr]] | $94K | 54 | +7.4% | open |
| 2026-10-26 | [[STC]] | [[BRADLEY C ALLEN JR]] | $95K | 50 | +7.4% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "contrarian")
SORT filed DESC
```

Back to [[What Works]].
