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

## Run 4 (2026-10-21): third review round

Run 3 raised the edge against the survivor index from +2.7% to +6.4% a year. A third independent review, with
skeptics re-checking each finding against the data, traced that jump: buy-and-hold weights (+1.2 points) and leaving
out each stock's own post-signal windows (+2.3 points) are legitimate, but part of the rest came from defects:
- The index dropped a stock at the close *before* its own filing was public, so the overnight jump on an after-hours
  filing (+0.9% on average) was in neither the event nor the index. Membership is now point in time: the index holds
  the stock to the open of its entry session and sells it there (worth about -0.5 points a year on the edge).
- In January-April 2006 the index held only 3-70 stocks, an odd set (stocks whose first filing failed the price
  check), because every stock bought in those months sat out its own window. Sessions with fewer than 100 stocks are
  no longer a benchmark: those months and events have no survivor comparison (about -0.25 points; the 2006 figure
  of +9.1% vs survivors is withdrawn).
- A reused ticker joined the index at the *former* company's rejected filings, years before the current company's
  first filing, selecting on its later buy. The start now comes only from the company priced on that ticker.

Data breaks (run 3): the rule that a 3x step on under 3x normal dollar volume is a missed split mostly caught real
crashes, because dollar volume is measured at the crashed price (OVV 2020-03-09, Fannie Mae 2008-09-08, IMNN 2013).
Those losses were censored and portfolios sold the close before the crash. A fall now counts as a break only if it
looks like a split (a whole-number ratio, all in the opening gap, flat after, ordinary dollar volume). Rises keep the
old rule (a missed reverse split). Bad-tick removal now skips heavily traded spikes, and the placebo is censored at
breaks like the events.

Placebo: dropping placebo windows that overlap an earlier signal also dropped the events *followed* by a re-buy
190-251 sessions later, which tend to be losers, so the paired event mean was too high (+1.26% vs +0.90% for all
events). The event side is now every event with a placebo window; the difference with no exclusions is reported as
a conservative bound.

Smaller fixes: the forward-test ledger gives a row stopped by a data break a final "break" status instead of leaving
it open forever; the daily run stamps new rows when it writes them and falls back to cached SPY prices if the refresh
fails; a failing reused-ticker issuer no longer relabels never-checked filings as price mismatches. Regression tests
cover each change, and each was checked to fail when its fix is reverted.

Not changed: the review found no defect in the track-record, reused-ticker or forward-timing fixes from run 3, and
none of these changes touches a slice, bucket, horizon, benchmark choice or verdict rule.

## Forward test counting (2026-10-21)

Set before any 63-session forward outcome existed. The forward test now counts one signal per company per entry day,
as the backtest does: several insiders of one company buying on the same day share one return, so they are one
observation (the 2026-10-13 HEI filings by eight directors had counted eight times). The "100 matured 63-session
outcomes" in `hypotheses.json` are counted the same way.

## Signal desk (2026-10-21): exploratory, not pre-registered

The dashboard's report cards (`stocktrack/advisor.py`, `data/backtest/advisor.json`) are an added analysis, built
after seeing the results, so the forward test is their real check. What was tried and what was kept:

- A ridge regression of each buy's 3-month return over comparable stocks on all its features, fit on 2006-2015 with
  the shrinkage chosen inside that period, predicted nothing on 2016+ (rank correlation -0.01; the chosen shrinkage
  was the largest tried, i.e. "ignore the features"). It was dropped: individual buys are mostly noise.
- Kept instead: "tilts", the features that beat or lagged the typical buy (calendar-time portfolios, liquid buys at
  $2+ and $1M+/day) by at least 1% a year in the same direction in two periods. Each tilt is the smaller of its two
  edges. A buy's tilts are summed; +2% a year or more is "above typical", -2% or worse "below typical".
- Out-of-sample check of that procedure: tilts chosen from 2006-2010 vs 2011-2015 only, applied unchanged to 2016+.
  Above-typical buys beat comparable stocks by +8.0% a year (t 3.0), typical +2.9%, below-typical -0.8%; above minus
  below +8.9% a year (p 0.02). (Averaging the two periods' edges instead of taking the smaller gave +5.2%, p 0.05;
  the smaller was adopted because one feature otherwise dominated the live tiers.) In a 20-position simulated
  account since 2016 the tiers made 11.8%, 11.4% and 3.2% a year against 15.1% for SPY: avoiding below-typical
  buys helped, above-typical buys barely beat typical ones, and nothing beat the S&P 500.
- The live tilts use 2006-2015 vs 2016+. Position sizes come from risk (a loss budget over the 1-in-10 bad 3-month
  return of stocks at a similar price and liquidity), capped at 5% of the account and 2% of daily dollar volume.
  (Changed to 1-in-20 on 2026-10-23; see the review below.)

## Signal desk review (2026-10-23)

Three independent reviews (model validity, card accuracy and UX, wording) checked the desk. The validation
reproduces exactly and its date splits are clean: no 2016+ data enters the validation tilts. But it is weaker than
the section above made it sound.

**All of the separation is from 2016-2020.** Above minus below was +18.7% a year in 2016-2020 (t 4.1) and +1.0% a year
since 2021 (t 0.2). By year: 2016 +18%, 2017 +11%, 2018 +12%, 2019 +12%, 2020 +32%, 2021 0%, 2022 -4%, 2023 +7%,
2024 -10%, 2025 +2%, 2026 so far +11%. Several live tilts reversed in 2021-2026: price $1-5 (+3.0% live, -8.4% a year
in 2021-26), 10% owner (+2.2% live, -9.3%) and 3+ insiders (+1.2% live, -1.8%). `advisor.json` now stores the
validation by period and by year, and the desk shows the split.

**2016+ was looked at several times before the settings were fixed, and the p-value isn't adjusted for that.** In
order: every level's 2016+ edge for these eight features was printed; averaged tilts were run on 2016+ at a 2%
threshold (+5.2%, p 0.047) and at 3% (not reported before); the ridge model had been scored on 2016+; the
smaller-of-two-edges rule was chosen after seeing both results; and the early/late split moved from 2011-12-31 (the
ridge model's) to 2010-12-31 without a stated reason. With the 2011 split the same procedure gives +5.6% a year,
t 1.13, p 0.26. Treat p 0.02 as exploratory.

Robustness, above minus below in % a year (t), as computed by the model reviewer. Its sub-periods were cut a little
differently from `advisor.json`, so the first row differs slightly from the +18.7% and +1.0% above.

| Variant | 2016+ | 2016-20 | 2021-26 |
|---|---|---|---|
| Published (min tilt 1%, tier edge 2%, split 2010) | +8.9 (2.36) | +17.5 (3.77) | +0.1 (0.02) |
| Min tilt 0.5% | +6.9 (2.21) | +13.6 (3.29) | +1.3 (0.33) |
| Min tilt 1.5% | +8.8 (2.19) | +17.8 (3.56) | -0.4 (-0.07) |
| Tier edge 1% | +4.3 (2.06) | +3.5 (1.12) | +5.2 (1.86) |
| Tier edge 3% | +12.8 (2.28) | +25.8 (3.54) | +2.1 (0.28) |
| Min tilt 0.5%, tier edge 3% | +7.0 (1.47) | +19.7 (3.13) | -3.6 (-0.60) |
| Without the $1-5 price tilt | +9.3 (2.68) | +18.3 (3.98) | +0.1 (0.04) |
| Averaged edges, tier edge 2% / 3% | +5.2 (1.99) / +8.8 (2.92) | +5.9 / +12.2 | +3.6 (0.99) / +6.3 (1.53) |
| Split 2009-12-31 | +8.6 (3.00) | +12.6 | +6.0 (1.37) |
| Split 2011-12-31 | +5.6 (1.13) | +13.9 | -1.0 (-0.15) |
| Split 2012-12-31 | +11.1 (1.75) | +22.8 | +0.8 (0.12) |
| Min sample 200 | +9.7 (2.73) | +15.6 | +3.7 (0.80) |

The 2016+ sign is positive in every variant; its size (+4% to +13%) and significance depend on the settings, and
2021-26 is about zero in nearly all of them. Leaving out any one tilt keeps 2016+ at +8.5% to +10.0%.

**Survivorship.** Tilts and outcome ranges come only from companies still listed today, and the share of buys that can
be priced rises from 25% (2006) to 85% (2025). The levels that swing most between periods (low prices, big prior
falls, unknown prior returns) are the ones survivorship would distort.

**What changed.**

- Sizing uses the 1-in-20 bad 3 months (`p05`) of similar past buys instead of 1-in-10, so sizes are smaller.
- One card per company: its latest filing day in the window, with everything on the card from that day's largest
  buy. Before, a card could name one insider and show another's price, link and features, and one company could have
  up to eight cards. The validation counted each company-day's first filing; the cards and the forward test use its
  largest, a choice that wasn't validated separately (a reviewer's check of a similar rule moved the 2016+ gap from
  +8.9% to +8.8%).
- Entered cards show the latest close from the ledger, not the close before entry.
- The desk says plainly that the profiles were fitted after seeing the data, that the edges are before costs and
  from survivors, that no profile beat the S&P 500 since 2016, and what all the example sizes add up to.
- From 2026-10-23 the daily run records each new buy's profile (`tier`, `tilt`) in `data/picks.csv` when it is
  logged, and `hypotheses.json` registers "tier: above vs below": judged at 100 matured outcomes per group, counting
  each company-day once with its largest buy. A later refit can't change what gets judged.
- The settings (`MIN_EFFECT` 1%, `TIER_EDGE` 2%, `SPLIT_EARLY` 2010-12-31, `MIN_N` 150) are frozen as of this date.
