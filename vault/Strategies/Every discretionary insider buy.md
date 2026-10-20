---
type: "strategy"
key: "all_liquid"
signals: 66032
cagr: 0.0540996
spy_cagr: 0.110724
sharpe: 0.267835
max_drawdown: 0.573338
holdout_excess: 0.00327607
---

# Every discretionary insider buy

Rule key: `all_liquid`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 66,032 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.7% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.6% |
| vs surviving stocks | +0.3% |
| 2006-2015 excess /yr | +6.3% (p 0.022) |
| 2016+ excess /yr | +0.3% (p 0.927) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Years beating SPY | Trades | Costs/yr |
|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.9% | +11.1% | 0.32 | 0.56 | 63% | 1.15 | 43% | 4,963 | 9.1% |
| 63d | +5.4% | +11.1% | 0.27 | 0.56 | 57% | 1.10 | 52% | 1,660 | 2.7% |
| 126d | +5.4% | +11.1% | 0.27 | 0.56 | 57% | 1.04 | 38% | 840 | 1.5% |


Cost sensitivity (63-session hold): no costs +8.2%/yr, double costs +2.7%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +21.9% | +13.8% | +8.0% |
| 2007 | -8.4% | +5.1% | -13.5% |
| 2008 | -28.2% | -36.8% | +8.6% |
| 2009 | +54.0% | +26.4% | +27.6% |
| 2010 | +28.3% | +15.1% | +13.3% |
| 2011 | -11.4% | +1.9% | -13.3% |
| 2012 | +19.6% | +16.0% | +3.6% |
| 2013 | +35.5% | +32.3% | +3.2% |
| 2014 | -1.5% | +13.5% | -15.0% |
| 2015 | +4.2% | +1.2% | +3.0% |
| 2016 | +35.0% | +12.0% | +23.0% |
| 2017 | +27.1% | +21.7% | +5.3% |
| 2018 | -14.2% | -4.6% | -9.6% |
| 2019 | +11.1% | +31.2% | -20.1% |
| 2020 | +32.6% | +18.3% | +14.3% |
| 2021 | -1.0% | +28.7% | -29.7% |
| 2022 | -40.0% | -18.2% | -21.8% |
| 2023 | +27.9% | +26.2% | +1.7% |
| 2024 | -13.9% | +24.9% | -38.8% |
| 2025 | -9.2% | +17.7% | -26.9% |
| 2026 | -0.7% | +13.4% | -14.1% |


## Live forward test

13 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-19 | [[FUL]] | [[Malik Muhammad Shahbaz]] | $25K | 35 | – | pending |
| 2026-10-16 | [[SAH]] | [[Rusnak Paul P]] | $752K | 28 | -2.3% | open |
| 2026-10-16 | [[NAD]] | [[TOTH TERENCE J]] | $72K | 33 | -0.6% | open |
| 2026-10-16 | [[CRBG]] | [[NIPPON LIFE INSURANCE CO]] | $20.5M | 25 | +0.1% | open |
| 2026-10-16 | [[FIS]] | [[Goldstein Jeffrey A]] | $58K | 13 | +1.1% | open |
| 2026-10-16 | [[NBIS]] | [[Grimme Arne]] | $50K | 10 | -5.0% | open |
| 2026-10-16 | [[PEP]] | [[POHLAD ROBERT C]] | $23.7M | 62 | +1.7% | open |
| 2026-10-16 | [[BYRN]] | [[Roth Adam L]] | $70K | 40 | +0.7% | open |
| 2026-10-16 | [[PAM]] | [[Mindlin Marcos Marcelo]] | $35.1M | 49 | -2.5% | open |
| 2026-10-16 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | -1.7% | open |
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | $1.5M | 72 | -1.5% | open |
| 2026-10-16 | [[BORR]] | [[Troim Tor Olav]] | $2.3M | 51 | -1.5% | open |
| 2026-10-16 | [[EDRY]] | [[Pittas Aristeidis P]] | $29K | 19 | -0.2% | open |
| 2026-10-16 | [[BZUN]] | [[Qiu Wenbin]] | $20K | 30 | +3.7% | open |
| 2026-10-15 | [[BPRE]] | [[MacDonald Ryan S]] | $2K | 34 | -1.5% | open |
| 2026-10-15 | [[BPRE]] | [[Ruddy Jordan B]] | $44K | 63 | -1.5% | open |
| 2026-10-15 | [[IMSR]] | [[Pardee Charles G]] | $22K | 55 | -10.4% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -0.9% | open |
| 2026-10-15 | [[TRXB]] | [[Alexandria Venture Investments, LLC]] | $2.5M | 55 | +3.1% | open |
| 2026-10-15 | [[CRBG]] | [[NIPPON LIFE INSURANCE CO]] | $8.8M | 24 | +0.6% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "all_liquid")
SORT filed DESC
```

Back to [[What Works]].
