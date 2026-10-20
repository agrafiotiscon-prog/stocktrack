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
