# WBI7 — Wang Brothers Investments · Lease-Level DCF

A single-file, institutional-grade real-estate DCF underwriting tool. Monthly
lease-level engine with blended rollover, expense recoveries (including annual
caps), **percentage rent** (retail overage), **recurring capital reserves**,
valuation sensitivity matrices, a **tornado IRR-sensitivity** chart, a
**goal-seek solver**, a **portfolio / fund roll-up** (pool several deals on a
common timeline with a fund-level promote), a **ground-up development pro forma**
(phased construction draws, capitalized interest, lease-up, yield-on-cost and
development spread), correlated Monte Carlo, refinance, a **mezzanine / second tranche** (subordinate
debt layered on the senior loan, with blended cost and all-in coverage),
multi-tier IRR-hurdle
promote waterfalls, an inflation factor (real returns + CPI escalation), an
after-tax module (depreciation, recapture, capital gains), and a one-click
**IC summary** export (a print-ready one-page deal sheet). Ships with 25
California scenario presets across five asset classes and an optional cloud
backend.

---

## 1. Run it (standalone — no setup)

Open **`index.html`** in any modern browser (Chrome, Safari, Edge, Firefox).
Double-click it, or drag it into a browser tab. That's the whole install.

- **Access key:** `wbi7` (type it at the gate, press Enter).
- Opens to a blank **Custom scenario** by default — start entering your property,
  or pick one of the 25 sample scenarios from the top-bar dropdown (grouped by
  asset class) as a starting point.
- Results update live on the right: KPI strip, sources & uses, annual cash flow
  (now with **% Rent** and **Reserves** columns), NOI and lease-expiration charts,
  returns & valuation, the LP/GP waterfall, heat-mapped sensitivity matrices, a
  **tornado** IRR-sensitivity chart, a **goal-seek** panel, and Monte Carlo.
- **Export / Import a deal** as a portable, versioned `.json` file (share it,
  archive it, or reopen it on another machine; the round-trip is exact and
  validated), **Export XLSX**, download a one-page
  **IC summary** (a self-contained, print-ready HTML deal sheet), switch
  **light/dark**, pick an accent color and font. Everything persists in your
  browser automatically.

Optional features inside the app:
- **Percentage rent** (Rent Roll card): per-lease retail overage — natural or fixed
  breakpoint, with monthly accrual and an annual true-up. Off when overage % is 0.
- **Recovery caps** (Recoveries card): an annual ceiling on each tenant's billable
  pool, cumulative (from the base year) or year-over-year. Off when the cap is 0.
- **Capital reserves** (Other Income card): a recurring below-NOI replacement
  reserve ($/SF/yr or fixed $/yr, with growth). Off when the amount is 0.
- **Tornado** (output card 9): one-driver-at-a-time levered-IRR swings, sorted by
  sensitivity, around the base case.
- **Goal seek** (output card 10): solve price, exit cap, or a uniform rent factor
  to hit a target levered IRR or equity multiple, by bisection.
- **Portfolio / fund roll-up** (output card 11): snapshot deals into a fund, each
  at its own start-month offset; the pooled levered/unlevered equity cash flows
  give a fund-level IRR, equity multiple, profit, and a fund promote waterfall.
  The fund is saved in your browser.
- **Development / construction** (input card XIV → output card 12): a self-contained
  ground-up pro forma — land + hard/soft/contingency drawn over the build on an
  S-curve or straight line, a construction loan funding its LTC share plus
  capitalized interest, NOI ramping over lease-up, then a stabilized sale. Reports
  total cost, equity/loan, yield-on-cost, development spread, profit/margin on
  cost, and a levered IRR/EM. Off unless you toggle it on.
- **Hold-period analysis** (output card 13): levered IRR and equity multiple for
  every exit year, by re-running the full model at each horizon, with the
  IRR-maximizing hold highlighted — the "when should we sell?" view.
- **Scenario compare** (output card 14): snapshot the current deal as a column
  (base / upside / downside, or distinct deals) and compare a full metric stack
  side by side, with green/red deltas against the base. Saved in your browser.
- **Refinance** (Debt card): a mid-hold refi with LTV / DSCR / fixed sizing.
- **Mezzanine / second tranche** (Debt card → output card 6d): subordinate debt
  layered on the senior loan — shrinks the equity check, is serviced after senior
  and repaid from sale proceeds after the senior balance. Shows blended cost,
  loan-to-cost, all-in DSCR and debt yield, and the equity IRR/EM with vs. without
  it (positive leverage when the deal yield beats the blended debt cost). Off at 0.
- **Climate & insurance stress** (card 10f): look up the property's **FEMA flood
  zone** (free public data), then stress the deal with a higher insurance premium and
  an uninsured-loss reserve and see NOI, year-1 DSCR, IRR, value and profit before vs
  after. High-hazard zones (A…, V…) suggest a larger stress. The math is a pure
  overlay; the FEMA lookup is best-effort (CORS may block it — enter the zone manually).
- **Actuals vs underwriting** (card 10e): once the deal is operating, enter actual
  results year by year and compare them to the model's projection. Reports per-year
  NOI variance ($ and %), a cumulative **NOI index** (actual ÷ underwritten), and an
  ahead / on-track / behind flag against your threshold. Pairs with snapshots — the
  original underwriting is just a saved version. A tracking tool, not a re-underwrite.
- **Version diff — "git for deals"** (card 10d): snapshot the deal to local storage,
  then compare any two versions. It lists exactly which assumptions changed (old →
  new) and shows an **IRR attribution bridge** — how much each group of changes moved
  the levered IRR, measured by replacing one group at a time and re-running the full
  model. Contributions are standalone effects, so the interaction residual is reported
  explicitly. Read-only: comparing never alters the live inputs.
- **Onboarding & navigation**: a first-run **welcome guide** (re-openable from the top
  bar) explains the workflow and indexes every capability in the tool, and a
  **Jump to** menu navigates the 22 section cards. Pure UI — no engine change.
- **Analysis slideshow** (top bar → *Slideshow*): one click builds a self-contained,
  presentable deck of the deal — title (with headline stat chips), an agenda, headline
  returns, capital stack, annual cash flow, the sensitivity (tornado) and pre-mortem
  (kill-zone) findings, a **Key slide defining every term** for non-specialist
  audiences, and a methodology/disclaimer close. Navigate with arrow keys, number keys
  (jump to slide), or **G** (jump to the Key); a progress bar tracks position. **Print →
  Save as PDF** lays it out one slide per page. No dependencies; user inputs are HTML-escaped.
- **Interactive charts**: every bar chart (cash flow, NOI, lease expirations, fund
  cash flow, development draws, hold-period IRR) has a control row to **fit the Y
  axis to the data** (drop the zero baseline to magnify differences), set a manual
  **Y min/max**, window the **X axis** to a range of years, or reset — plus hover
  **tooltips**. Axis choices persist as you edit the deal.
- **Pre-mortem / kill-zone** (card 10c): the inverse of the tornado — instead of the
  spread of outcomes, it finds what makes the deal *lose money*. For each driver it
  bisects the adverse move needed, on its own, to drop the levered IRR to your failure
  bar (its "kill point", or "robust" if it can't sink the deal alone), and it
  stress-tests driver *pairs* to surface the combinations that fail even when neither
  move alone would ("flat rents AND a wider exit cap"). Pure overlay; the notch sizes
  are fixed moderate stresses, not market-calibrated.
- **Capital-structure optimizer** (card 10b): given your debt terms and lender
  constraints (max senior LTV, max total LTV, min DSCR, min debt yield, mezz rate),
  grid-searches senior + mezzanine leverage for the mix that maximizes the levered
  equity return, then shows it against your current structure and an all-equity
  baseline and names the binding constraint. Positive leverage lifts the return
  until a constraint binds; dilutive debt pushes the optimum toward no leverage.
  Pure overlay (clone + re-run) — the base model is never mutated. Directional (a
  discrete grid; debt isn't re-priced by leverage tier).
- **Assumption confidence & risk-weighted sensitivity** (card 9b): tag how sure you
  are of each key driver (exit cap, rents, rent growth, price, loan rate, renewal,
  downtime, opex growth, credit loss). The tool then weights each driver's levered-IRR
  impact by your uncertainty — High = a tighter plausible band, Low = wider — and ranks
  a **diligence list**: the drivers that are both high-impact *and* not yet
  high-confidence, i.e. what to verify first. A pure overlay (clone + re-run), so it
  changes nothing in the base model; something ARGUS doesn't do (it treats every input
  as equally certain).
- **Floating-rate / ARM** (Debt card): the senior rate starts at the fixed rate and
  steps by a bps amount at each reset interval (positive = rising-rate stress,
  negative = falling), bounded by a cap and floor; the payment recasts at each
  reset. Flows through DSCR, cash flow and IRR. Off unless toggled — the fixed
  path is byte-identical to before.
- **Prepayment penalty** (Debt card): a step-down penalty (e.g. 5-4-3-2-1) charged
  on the loan balance at any early payoff — at sale and at a refinance. It reduces
  net proceeds and the levered return only (not the unlevered), and eases the
  longer you hold, which the hold-period card reflects automatically. Off unless
  toggled — byte-identical to before.
- **Multi-tier waterfall** (Equity card): IRR-hurdle promote tiers.
- **Inflation** (Analysis card) + a **CPI** toggle per lease/profile.
- **After-tax returns** (Taxes card): depreciation shield, recapture, cap gains.

It works fully offline. The only external references (the spreadsheet-export
library and, if you enable cloud, the Supabase SDK) degrade gracefully when
unavailable.

---

## 2. Optional: cloud sync, sharing, live rates

Want sign-in, deals saved to the cloud and reachable from any device, sharing
with real permissions, and live benchmark rates? See **`SETUP.md`** for
step-by-step instructions (Supabase + a Netlify function). In short:

1. Create a free Supabase project; run `backend/supabase/schema.sql` in its SQL editor.
2. Paste your Supabase URL + anon key into the `WBI7_CLOUD` line near the top of
   `index.html`'s script.
3. (For live rates) deploy on Netlify with `backend/netlify.toml` +
   `backend/netlify/functions/market-data.mjs` and a free `FRED_API_KEY`.

Left blank, the cloud layer stays completely inert and the file behaves exactly
as the standalone app.

---

## 3. Run the tests

All logic is covered by a test suite — engine math (analytic + hand-computed),
after-tax, the five newer modules (percentage rent, recovery caps, capital
reserves, tornado, goal seek), plus two browser-free DOM harnesses (run in
[jsdom](https://github.com/jsdom/jsdom)) that drive the **real UI render path**:
one locks representative outputs to golden values, the other checks the new
feature surfaces round-trip and render.

```bash
# one-time: the DOM harnesses need jsdom
npm i jsdom

# everything (auto-skips the optional Chrome harness if no CHROME_PATH):
./run-tests.sh

# or pieces individually:
node wbi7_test.js        # core engine analytic tests (Part A)
node aftertax_tests.js   # after-tax (depreciation, recapture, cap gains)
node feature_tests.js    # percentage rent, recovery caps, reserves, tornado, goal seek
node portfolio_tests.js  # portfolio / fund roll-up (additivity, blending, waterfall)
node development_tests.js # development / construction pro forma (cost, yield, leverage)
node holdperiod_tests.js # hold-period analysis (IRR by exit year, optimal hold)
node compare_tests.js    # scenario compare (reconciliation, deltas, immutability)
node mezz_tests.js       # mezzanine overlay (identity, leverage, coverage, amort)
node floating_tests.js   # floating-rate ARM (off==fixed, steps, cap/floor, direction)
node prepay_tests.js     # step-down prepayment penalty (off==none, exact, decline, refi)
node confidence_tests.js # assumption confidence + risk-weighted sensitivity (overlay)
node optimize_tests.js   # capital-structure optimizer (feasibility, leverage, DSCR-bind)
node killzone_tests.js   # pre-mortem / kill-zone (kill points, combinations, overlay)
node versiondiff_tests.js # version diff + IRR attribution bridge (pure)
node actuals_tests.js    # actuals vs underwriting variance (pure)
node climate_tests.js    # climate / insurance stress + FEMA parsing (pure)
node marketdata_tests.js # live market-data parsers (fixture-tested; needs jsdom)
node dom_golden.js       # locked display goldens for 5 presets, via jsdom
node ui_features.js      # new-feature UI wiring/round-trip, via jsdom
```

`wbi7_test.js` Part A extracts the pure engine and checks it against
hand-computed values; Part B (an optional puppeteer golden-master harness) runs
only when `CHROME_PATH` is set (`npm i puppeteer-core`) and otherwise skips. The
two jsdom harnesses reproduce the important parts of that browser coverage
without needing a Chrome binary.

---

## 4. Files

```
index.html                  -- the app (single self-contained file)
wbi7_test.js               -- engine analytic (Part A) + optional puppeteer harness (Part B)
aftertax_tests.js          -- after-tax tests
feature_tests.js           -- percentage rent, recovery caps, reserves, tornado, goal seek
portfolio_tests.js         -- portfolio / fund roll-up tests
development_tests.js       -- development / construction pro forma tests
holdperiod_tests.js        -- hold-period analysis (IRR by exit year) tests
compare_tests.js           -- scenario compare tests
mezz_tests.js              -- mezzanine / stacked-debt overlay tests
floating_tests.js          -- floating-rate (ARM) senior-debt tests
prepay_tests.js            -- step-down prepayment-penalty tests
confidence_tests.js        -- assumption confidence + risk-weighted sensitivity tests
optimize_tests.js          -- capital-structure optimizer tests
killzone_tests.js          -- pre-mortem / kill-zone tests
versiondiff_tests.js       -- version diff + IRR attribution tests
actuals_tests.js           -- actuals vs underwriting tests
climate_tests.js           -- climate / insurance stress tests
marketdata_tests.js        -- live market-data parser tests (fixtures)
dom_golden.js              -- jsdom golden-master (locked display values for 5 presets)
ui_features.js             -- jsdom UI smoke test for the new feature surfaces
run-tests.sh               -- one-command runner for all suites
SETUP.md                   -- optional cloud backend (Supabase) setup guide
backend/supabase/schema.sql -- Supabase tables + RLS for cloud save & sharing
backend/proxy/market-data.mjs -- optional serverless rates proxy (FRED, key server-side)
TRACK1_PLAN.md             -- sequenced build order toward technical parity with ARGUS
```

---

## Notes & honest limitations
- Numbers use monthly cash timing and a forward-12-month-NOI exit; they will
  differ from annual-period models by construction.
- After-tax: building depreciation only (capital improvements / leasing costs are
  not separately depreciated); passive-loss limitations are not modeled.
- Recoveries: net / base-year stop / fixed CAM with gross-up, an admin fee, and an
  annual cap (cumulative or year-over-year).
- Percentage rent is modeled per in-place lease (natural or fixed breakpoint, with
  an annual true-up); it is not currently applied to rollover/market leasing
  assumptions. Capital reserves are a recurring below-NOI cost and deliberately do
  not affect NOI, the cap-rate exit value, or debt-coverage metrics.
- Tornado and goal-seek shock one input at a time and assume the metric is
  monotone in that input over the search range (true for the drivers offered).
- Portfolio roll-up pools deal-level equity cash flows on a common timeline with a
  single fund-level promote; it does not yet model fund-level subscription lines,
  management fees, or capital-call mechanics. Pooling can net one deal's capital
  call against another's distribution (so total equity invested reflects the
  cross-collateralized pool, not the naive sum of day-one checks).
- The **Market Context** panel pulls free public data (US Census ACS demographics
  by county; Treasury/mortgage benchmarks via the optional FRED proxy) as market
  *context* keyed to the property's coordinates. It is deliberately **not** a comps
  feed: no submarket cap rates, no comparable asking rents, no transaction comps —
  that data is licensed (CoStar, Green Street, RCA, Trepp) and can't be sourced for
  free or scraped. Live calls depend on the data APIs and the browser (CORS); the
  parsers are unit-tested with fixtures, but the live fetch is exercised on your
  first run and degrades gracefully if a source is unreachable.
- The prepayment penalty is a step-down schedule (a year-1 % declining by a fixed
  step each loan year) applied to the balance at any early payoff — at sale and at
  a refinance. It is not yield maintenance or defeasance (those would need a
  separate loan-maturity and reinvestment-rate input), and it does not apply to
  the mezzanine tranche.
- Floating-rate (ARM) debt applies to the original senior loan only: the rate
  starts at the fixed rate and steps by a fixed bps amount each reset, bounded by
  a cap/floor, with the payment recast at each reset. It is a deterministic
  rate-path stress, not a stochastic rate model, and a refinance (if any) still
  originates at its own fixed rate.
- The mezzanine tranche is overlaid on the senior-levered cash flow (it does not
  re-run the engine): it shrinks the equity check, is serviced monthly after the
  senior loan (same rate convention), and is repaid from sale proceeds after the
  senior balance. It assumes the mezz rides to sale — it is not paid off at a
  refinance, and the senior loan is sized independently of the mezz piece.
  it draws hard/soft/contingency on an S-curve or straight line, capitalizes the
  construction-loan interest, ramps NOI over lease-up, and sells at the exit cap.
  Stabilized NOI is an input (read it from the operating model, or click "Use
  current deal's Yr-1 NOI"); it does not yet model phased delivery, a separate
  perm-loan takeout, or unit-by-unit absorption within lease-up.
- The financial engine and UI are tested; the live Supabase/Netlify cloud
  path is exercised by you at setup (its data transforms and the standalone
  fallback are unit-tested).
- This tool is for analysis and education; it is not investment, legal, or tax
  advice.
