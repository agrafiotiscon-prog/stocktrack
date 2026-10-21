# Backtest changes after the pre-registration

The design in `preregistration.json` was committed before any results existed. Changes made after
seeing results are listed here so they can be judged. All of them are bug fixes found by an
independent adversarial review. None changes a slice, bucket edge, horizon, benchmark or verdict
threshold. Every test from every run stays in `tests_log.csv`, tagged by config hash.

## Run 1 (2026-10-19, config `47cec3e7a6c3b407`)

First full run on the pre-registered design.

## Run 2 (2026-10-20): data and look-ahead fixes

Data parsing (these changed which events exist and their features):
- Owner relationships like `TenPercentOwnerOther` / `DirectorOther` (2006-2022 datasets) were
  read as "Other". About 1,300 owners per quarter got the wrong role, and so a wrong score.
- Transactions within a filing weren't in filing order, so holdings before and after a buy (stake
  increase) were wrong for about two thirds of multi-purchase filings.
- Purchases of preferred stock, notes, warrants and rights were treated as buys of the common.
- Two filings were merged as "the same purchase" whenever share counts matched. Now they also need
  a shared owner, the same post-trade balance, or a fund/entity filer. Different insiders who bought
  the same round lot now count separately in clusters.
- Filings that share a reporting owner (a fund family) count as one insider in clusters.
- Yahoo sometimes lists a split twice, which threw off raw prices for that stock's earlier history.
  An unfinished intraday bar is no longer stored as a close.
- A company that now trades only preferred/warrant lines is no longer priced through those lines. A
  reused ticker is priced only when the filing's price matches the market (holdco reorganisations).

Look-ahead (none affected the SPY-based headline materially):
- The survivor index counted stocks before their first insider buy. That selects on a future buy,
  which tends to follow declines, so the index was too low and "beats survivors" too easy.
- The placebo looked at the year *before* each buy, which also selects on the future buy. It now
  uses the year after.
- A trade dated after its own filing (a typo) could be price-checked against a later close.
- Track records were released per filing day rather than per event (latent; no effect on run 1).
- "First buy in 12 months" was meaningless in 2006 because 2005 wasn't loaded. Now it's unknown.
- Winsorizing bounds used the holdout period too. They now come from discovery only.

Statistics:
- Event-level confidence intervals now resample blocks of consecutive months, because 3-month
  windows overlap. The old intervals were too narrow.
- Holdout-only "promising" findings are now Holm-corrected. A significant sign flip between periods
  is labelled "reversed", not "promising".
- "Works" now needs a positive edge against the survivor index in *both* periods, not pooled.
- The walk-forward kept one signal per company-day *before* applying the score filter, dropping
  qualifying filings.
- Insider track records grouped all insiders' buys by company-day before grouping by insider.
- Simulation beta and alpha now come from monthly excess returns (daily small-cap returns lag).

Added analysis (exploratory, not part of the pre-registered tests):
- Each simulated portfolio is also reported hedged: short the Russell 2000 ETF (IWM) against the
  invested fraction each day, to separate the insider edge from the small-cap market's return.

## Run 3 (2026-10-20): second review round

A second independent review (return math, plus a check of the run-2 fixes) confirmed 10 more issues:
- The survivor index included each stock's own post-buy windows, so "vs survivors" compared buys
  partly against themselves and understated the edge by about half. A stock is now left out of the
  index for 63 sessions after its own public signals.
- The survivor index averaged daily returns (daily rebalancing, inflated by bid-ask bounce) but was
  compared with buy-and-hold returns. It is now buy-and-hold, rebalanced monthly.
- The survivor index measured from the prior close; stocks are entered at the open. Entry days now
  use the index's open-to-close return.
- The placebo still dropped windows that contained a *later* buy (selecting on the future). It now
  drops only windows overlapping an *earlier* signal.
- Yahoo sometimes misses a split, leaving a fake 3x+ step (e.g. +225% "returns"). Steps that aren't
  traded like news (dollar volume under 3x normal) are now data breaks that censor returns spanning
  them. Bad ticks lasting up to 3 bars are removed. Sub-penny days are kept, so near-total losses
  aren't dropped.
- Track records in the backtest now skip plan purchases and repeat same-day reports, matching the
  records used live.
- A reused ticker is trusted for an old company only if most of that company's filings match its
  price history (80%+ pass, median ratio 0.9-1.1), not one lucky match.
- Forward test: a date-only log stamp now counts as the end of that day. One failed price download no
  longer aborts the daily run, and new ledger rows are saved before outcomes update. The 16 rows
  logged on 2026-10-20 were re-stamped to their commit time (01:56 UTC, before that day's open).

## Forward test counting (2026-10-21)

Set before any 63-session forward outcome existed. The forward test now counts one signal per company per entry day,
as the backtest does: several insiders of one company buying on the same day share one return, so they are one
observation (the 2026-10-13 HEI filings by eight directors had counted eight times). The "100 matured 63-session
outcomes" in `hypotheses.json` are counted the same way.
