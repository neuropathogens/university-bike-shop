# WBI7 — In-House ARGUS
### Documentation & Reference

Wang Brothers Investments' in-house institutional underwriting tool: a single self-contained
HTML file that runs a full monthly, lease-level DCF for commercial real estate — acquisition,
financing, operations, exit, and partnership waterfall — plus a deep analysis layer
(sensitivity, risk-weighting, pre-mortem, optimization, Monte Carlo, version control,
actuals tracking, climate stress) and one-click presentation output. No server, no install,
no per-seat license. Open the file in a browser and underwrite.

---

## 1. Getting started

**Open it.** Double-click `index.html` (or host it anywhere static). Everything runs in the
browser; nothing is uploaded.

**Access gate.** The app opens behind a passphrase. Two keys are accepted: `wbi7` and `test`.
The key is checked against a stored hash; there is no plaintext password in the file.

**Pick a starting point.** Use the preset selector to load any of the 25 built-in California
deals (multifamily, office, retail, industrial, self-storage, etc.) or choose **Custom
scenario** to start from a blank deal pre-filled with reasonable current-market defaults.
Then edit the inputs; outputs recompute live.

**The 60-second workflow.**
1. Load a preset or a blank Custom scenario.
2. In the input sections, set the property, rents, expenses, debt, and exit assumptions.
   For many identical units (e.g. a dorm or a garden apartment complex), use **quick-add
   units** in the Rent Roll section to generate N matching suites and leases at once.
3. Read the KPI strip and cash-flow output.
4. Run the analysis cards (tornado, two-way table, pre-mortem, optimizer, Monte Carlo).
5. Export an **IC summary** or build a **slideshow** for the committee.
6. **Export the deal** to a `.json` file to share it with a colleague or archive it, and
   save a **snapshot** to compare against later versions.

---

## 2. Concepts and unit conventions

This matters if you ever edit the file or read the saved model JSON.

**Monthly, lease-level engine.** Cash flows are modeled month by month for each lease, then
rolled up to annual rows. A consequence worth knowing: expenses escalate *intra-year*
(monthly), so a fixed $X/yr expense reduces year-1 NOI by slightly more than X at any positive
growth rate (≈ X × 1.014 at 3%), not exactly X. This is correct behavior, not a rounding bug.

**Rates are decimals in the model.** In the saved model object, rates are stored as decimals:
`rentGrowth: 0.03`, `exitCap: 0.0625`, `debt.rate: 0.0675`, `ltv: 0.60`, `closingPct: 0.02`,
`sellCostPct: 0.02`. The on-screen inputs are *percent numbers* (you type `3`, not `0.03`);
the collect step divides by 100 and the load step multiplies by 100. A few fields are stored
as percent-numbers instead (recovery `recParam`, percentage-rent `overagePct`, retail
`salesGrowth`, the rent-roll/MLA escalation `esc` value), and a few are raw dollars
(`salesPSF`, breakpoint `bpAmount`). When in doubt, load a preset and inspect the model via the
browser console: `window.__wbi7.collectModel()`.

**Everything is one model object.** The full deal is a single JSON object with sections:
`analysis`, `acquisition`, `property.suites`, `rentRoll`, `mlas`, `absorption`, `expenses`,
`recoverySettings`, `otherIncome`, `debt` (with floating, prepayment, refinance, mezzanine
sub-objects), `exit`, `equity`, `mc`, `tax`, `development`, `fund`. It is saved to
`localStorage` and can be exported.

---

## 3. Inputs

Input sections are collapsible (`<details>`). Each drives the model live.

- **Analysis / global.** Hold period (months), discount rate, general credit/vacancy loss,
  inflation, and the property's map coordinates (used only for the flood/climate and live
  market-context lookups).
- **Acquisition.** Purchase price and closing costs (% of price).
- **Rent Roll.** The in-place leases: tenant, suite, SF, start month, term, base rent ($/SF),
  escalations, free rent, recovery method, and what happens at expiry (renew at market, etc.).
  **Quick-add units** generates many identical leases in one click.
- **Market Leasing Assumptions (MLAs).** The re-leasing rules applied when a lease rolls:
  market rent, rent growth, renewal probability, downtime, TIs, LCs, and free rent for new vs
  renewing tenants. This is what makes the rollover modeling institutional-grade.
- **Absorption.** Lease-up of currently vacant space.
- **Recoveries.** How operating expenses are recovered from tenants: gross-up occupancy, CAM
  admin fee, and an optional annual recovery cap.
- **Other income & reserves.** Non-rent income (parking, signage, fees) with its own growth,
  and a recurring capital reserve.
- **Expenses.** Operating expense line items, each with a basis ($/SF or fixed), growth,
  whether it is recoverable, and whether it varies with occupancy.
- **Debt.** Senior loan sizing (LTV / fixed amount / DSCR target), rate, interest-only period,
  and amortization — plus optional **floating-rate** terms (reset frequency, change per reset,
  cap/floor), **step-down prepayment** penalty, **refinance** (timing, new sizing, rate, cost),
  and **mezzanine** (a subordinate tranche between senior debt and equity).
- **Exit.** Exit cap rate (applied to forward-12-month NOI at sale) and selling costs.
- **Equity / waterfall.** LP/GP split, preferred return, and GP promote/carry — supports a
  tiered waterfall.
- **Monte Carlo.** Trial count (default 100,000), random seed, and the uncertainty (σ) on each
  key driver plus a correlation strength.
- **After-tax.** Land allocation, depreciation life, and ordinary/capital-gains/recapture rates
  for an after-tax return view.
- **Development.** A ground-up pro forma: land, hard cost, soft costs, contingency, construction
  period and loan, lease-up, and stabilized exit.
- **Portfolio / fund.** Roll multiple deals into a fund-level return with its own LP/GP terms.

---

## 4. Outputs and analysis

### KPI strip
Five headline metrics, each with a hover tooltip: **Levered IRR**, **Equity Multiple**,
**Total PV**, **Exit Value**, and **Year-1 DSCR**.

### Model health check
A live pre-flight panel directly under the KPIs that scans the inputs (and a few derived
values) for the things that quietly produce a wrong or meaningless answer, and updates as you
type. It flags three levels: **Issue** (will break or invalidate the numbers — a missing exit
cap, zero hold period, or a loan that exceeds cost), **Check** (plausible but worth a second
look — sub-1.0× year-1 DSCR, leverage above 80% of cost, a likely fat-fingered rate or cost
ratio, aggressive cap compression or rent growth, an unusually high pref/promote, mezzanine
priced below senior, or a refinance scheduled after the sale), and **Note** (informational).
A clean deal shows a single "no issues found" line. It is read-only — it never changes your
model — and it is the cheapest insurance against the embarrassing failure mode of a beautiful,
completely wrong IRR built on a typo.

### Cash flow
The full annual cash-flow table (rent, recoveries, percentage rent, other income, EGI,
expenses, NOI, capital, reserves, debt service, cash flow) with interactive charts (fit-Y,
manual axis, year window, hover tooltips). **Click any year to expand its month-by-month
ledger** — the per-month income → NOI → operating cash-flow waterfall that rolls up into the
annual figures, so any annual number can be traced to the month it came from (the test suite
reconciles every monthly ledger to the annual table across all 25 presets). Expand-all and
collapse-all controls sit above the table; operating cash flow shown per month excludes the
one-time sale and any refinance event, which are reported separately.

### Value-creation bridge
A live panel that decomposes the deal's levered profit into the five economic sources that
produced it — **operating income** collected over the hold, value from **NOI growth** (revalued
at the going-in cap), value from **cap-rate movement** (the exit cap versus the going-in yield,
i.e. the yield bet), **selling costs**, and **financing** (interest and loan costs). It answers
the question every committee asks — *is this an income deal or a cap-rate bet?* — and reports
the income-driven share versus the cap-rate-bet share directly. Two honest design points: the
five sources **reconcile exactly** to the profit shown in the KPIs (cap-rate movement is defined
so that NOI-growth plus cap-shift equals the exit-value gain over basis, and financing is the
measured difference from the all-cash case), and **financing appears as a cost** in total
dollars — because leverage works by lifting the *return* on a smaller equity check, not by
adding dollars, so its benefit lives in the IRR and equity multiple rather than the dollar
total. Read-only; it never changes the model.

### Sensitivity & risk
- **9 · Tornado.** One-way levered-IRR sensitivity: each driver shocked up/down independently,
  sorted by total swing. Shows what the deal is most sensitive to.
- **9b · Assumption Confidence & Risk-Weighted Sensitivity.** Mark how sure you are of each
  driver; the table weights each driver's IRR impact by your uncertainty and ranks a diligence
  list — the things that are both high-impact *and* not yet confident. ARGUS treats every input
  as equally certain; this doesn't.
- **9c · Two-Way Sensitivity Table.** Moves *two* drivers at once across a grid and re-runs the
  full engine at every pair — a heat-mapped data table (levered IRR, equity multiple, unlevered
  IRR, total profit, or year-1 DSCR). The centre cell is your live base case. Surfaces
  interactions the one-way tornado hides (e.g. how much rent growth offsets a softer exit cap).
  This is the classic data table ARGUS makes you export to Excel to build.
- **9d · Break-Even & Margin of Safety.** The downside complement to goal-seek: instead of
  solving for a target return, it solves for the *failure thresholds* and the cushion between
  the base case and each. For every key driver it finds the break-even — the rent decline or
  vacancy rise that takes year-1 DSCR to 1.0× (covenant), and the rent decline, exit-cap rise,
  or maximum purchase price that takes equity profit to zero (or the return to your hurdle) —
  and reports how much room you have. Each break-even is solved by bisection on a full
  re-underwrite, so the value is exact (plugging it back in reproduces the threshold). Coverage
  break-evens are shown only when the deal carries debt. It answers the question a tornado
  doesn't: "how far can this fall before it breaks?"

### Solving & structuring
- **10 · Goal Seek.** Bisection solver: finds the price, exit cap, or uniform rent factor that
  hits a target IRR or equity multiple.
- **10b · Capital-Structure Optimizer.** Grid-searches senior + mezzanine leverage to maximize
  the levered return subject to your LTV / DSCR / debt-yield constraints, against your current
  structure and an all-equity baseline, and names the binding constraint.
- **10c · Pre-Mortem / Kill-Zone.** The opposite of the tornado: finds each driver's **kill
  point** (how far it must move adversely, alone, to drop the return to your failure bar) and
  the **combinations** of two drivers that fail even when neither move alone would.

### Tracking & control
- **10d · Version Diff.** "Git for deals" — snapshot a model, then structurally diff two
  versions and attribute the IRR change to each input (with an honest interaction residual).
- **10e · Actuals vs Underwriting.** Enter realized NOI/EGI/CF by year and track variance
  against the underwriting.
- **10f · Climate / Insurance Stress.** A pure overlay that raises insurance cost (multiplier +
  additive $/SF + an uninsured reserve) and can pull a FEMA flood-zone risk read from the
  property coordinates.

### Roll-ups & specialized models
- **11 · Portfolio / Fund roll-up.** Combine deals into a fund-level return.
- **12 · Development pro forma.** Ground-up construction returns.
- **13 · Hold-period analysis.** Returns across a range of hold periods to find the optimal exit.
- **14 · Scenario compare.** Base/upside/downside side by side.
- **Live Market Context.** Optional pulls of FCC/Census/FRED context for the property location.

> **A note on every overlay.** The risk and structuring cards (two-way table, confidence,
> kill-zone, optimizer, climate, diff) all work by deep-cloning the model and re-running the
> engine — they mutate nothing. That is why running them never changes your base case and never
> affects the preset library.

---

## 5. Export, sharing, and presentation

### Deal files (portability)
**Export deal** downloads the current deal as a `.json` file you can email to a colleague,
archive after closing, back up, or reopen on another machine — no server or cloud account
required. **Import deal** loads one back in. This is the recommended way to move deals between
people and machines; the cloud-save backend is optional and the browser's `localStorage` only
holds the deal on the one machine.

The file is a small *versioned wrapper* around the model, which lets imports validate the
contents and lets the format evolve safely:
```json
{
  "format": "wbi7-deal",
  "appVersion": "wbi7-1",
  "exported": "2026-06-23T18:30:00.000Z",
  "name": "Grocery-Anchored Retail — Sacramento",
  "model": { "analysis": { ... }, "acquisition": { ... }, ... }
}
```
Files are named `WBI7_<deal name>_<YYYY-MM-DD>.json`, with the name sanitized of any
characters illegal in a filename. Import is deliberately strict and friendly: malformed JSON,
a file that isn't a deal, or a deal missing its core sections are each rejected with a plain
message in the status line rather than corrupting your workspace. **Backward compatible:** a
bare model exported by an older build (a raw object with `version: "wbi7-1"`) still imports.
The round-trip is exact — exporting and re-importing reproduces the model byte-for-byte, a
property the test suite enforces across every preset.

### Other output
- **IC Summary.** One click renders a clean, printable investment-committee memo (sources &
  uses, returns, cash flow, key assumptions) as a self-contained HTML page — print to PDF.
- **Slideshow.** Builds a self-contained presentation deck of the deal: title with headline
  stat chips, an agenda, headline returns, capital stack, cash flow, the sensitivity and
  pre-mortem findings, a **Key slide that defines every term** for non-specialist audiences,
  and a methodology/disclaimer close. Navigate with arrow keys, number keys (jump to slide), or
  **G** (jump to the Key); a progress bar tracks position; print → PDF is one slide per page.
- **Snapshots.** Save the current model under a label to `localStorage`; reload or diff later.
  (Snapshots stay in the browser; use a deal file to move a version to another machine.)
- **Excel.** Tabular data exports via the bundled SheetJS library.

---

## 6. Customization

- **Themes.** Eight built-in themes plus a custom accent color and font; persisted across
  sessions.
- **Show / hide sections.** The *Sections* button opens a panel with a checkbox per analysis
  card. Hide the ones your audience doesn't need — hidden cards disappear from view but their
  inputs still feed the model, so nothing breaks.
- **Info tooltips.** Every KPI and every key assumption input has a hover "i" that explains the
  term in plain English (77 in all).
- **Favicon & branding.** The page carries a "WB" icon and the Wang Brothers In-House ARGUS
  title.

---

## 7. Engine API (for developers)

The engine is exposed for scripting and testing on `window.__wbi7`.

**`computeDeal(model)`** — the core monthly DCF. Returns an object including:

| Field | Meaning |
|---|---|
| `irrL`, `irrU` | Levered / unlevered IRR |
| `emL`, `emU` | Levered / unlevered equity multiple |
| `mirr`, `lpIrr`, `gpIrr` | Modified IRR; LP and GP IRRs from the waterfall |
| `profit` | Total profit to equity over the hold |
| `value`, `proceeds` | Exit value and net sale proceeds |
| `price`, `allIn`, `loan`, `equity0` | Purchase price, all-in basis, loan, initial equity |
| `goin`, `exitCap`, `dcr1`, `walt`, `occ0` | Going-in yield, exit cap, year-1 DSCR, WALT, initial occupancy |
| `pvTot`, `dr` | Total PV at the discount rate; the discount rate used |
| `annual[]` | Per-year rows: `{y, rent, cl, rec, pct, oth, egi, exp, noi, cap, reserve, ds, cf}` |
| `eq[]`, `u[]` | Monthly levered / unlevered equity cash-flow vectors |
| `flags[]` | Warnings (e.g. covenant breaches) |

**Other exported functions** (selected): `computeMC` / `computeMCChunked` (Monte Carlo),
`E_tornado`, `E_confidence`, `E_sensTable` (two-way table), `E_goalSeek`, `E_optimize`,
`E_killzone`, `E_diff` / `E_diffBridge`, `E_actuals`, `E_climate`, `E_healthCheck` (the
model health scan), `E_valueBridge` (the value-creation bridge), `E_breakeven` (break-even / margin of safety), `E_monthlyRows` (monthly ledger rows for a hold year),
`computePortfolio`,
`computeDevelopment`, `E_holdAnalysis`, `E_compare`, `E_mezz`, `buildICSummary`,
`buildSlideshow`, plus `collectModel`, `loadModel`, and the `PRESETS` library. Deal-file
portability is exposed as `serializeDeal(model)` → JSON string, `parseDealFile(text)` →
`{ok, model, meta}` or `{ok:false, error}`, and `dealFilename(model)` → a safe download name.

**`E_sensTable(model, opts)`** example:
```js
const R = window.__wbi7.E_sensTable(model, {
  rowKey: "exitCap",      // any driver key (see below)
  colKey: "rentGrowth",
  metric: "irrL",         // irrL | emL | irrU | profit | dcr1
  steps: 2                // half-size; grid is (2*steps+1) square, clamped 1..4
});
// R.grid[r][c] = metric value; R.grid[R.baseRow][R.baseCol] === live base case
```
Driver keys: `exitCap`, `rentGrowth`, `rentLevel`, `price`, `debtRate`, `renewalProb`,
`opexGrowth`, `creditLoss`.

---

## 8. Architecture

- **One file.** `index.html` is fully self-contained (~3,300 lines): styles, an access gate,
  the engine, the UI layer, the preset library, and boot wiring. The only external dependencies
  are a CDN spreadsheet library, the Inter font, and an optional cloud-save backend.
- **Engine block.** All financial logic lives between the markers
  `/* ===================== WBI7 ENGINE START` and `WBI7 ENGINE END ===================== */`.
  Pure-node tests extract exactly this slice and run it in isolation, so the engine is verified
  independently of the DOM.
- **UI layer.** Below the engine: formatters, dynamic table rows, `collectModel` /
  `loadModel` / `renderAll`, the preset library, and `boot()` (which wires every button and
  only runs once the gate is passed).
- **Persistence.** State, theme, fund, compare set, snapshots, and hidden-section choices are
  each kept in their own `localStorage` key.

---

## 9. Testing

WBI7 is built test-first. Run the whole suite:
```bash
./run-tests.sh
```
It runs 30 files and **886 assertions**, all green. Pure-node suites (engine, after-tax,
features, portfolio, development, hold-period, compare, mezzanine, floating, prepayment,
confidence, optimizer, kill-zone, two-way sensitivity table, model health check,
value-creation bridge, **break-even / margin of safety**, version-diff, actuals, climate) extract the engine slice and assert against locally-defined
deal fixtures. jsdom suites (DOM golden, UI features, market data, deal file I/O) load the
whole page and exercise `window.__wbi7` — including an exact export/import round-trip across
every preset.

Two disciplines are enforced on every change:
1. **Presets stay byte-identical.** A jsdom "golden" harness locks 85 exact output values
   across five presets. Every new feature defaults to off/neutral so these never move.
2. **Every feature ships with its own suite.** Overlays additionally assert base-model
   immutability — running them must not mutate the model.

---

## 10. Deliberate limitations

WBI7 is honest about what it is. It matches or exceeds ARGUS on *analysis* (the formulas are
all here, plus tools ARGUS lacks), but it is not a substitute for the ARGUS *ecosystem*:
there is no licensed market data (CoStar/Green Street), no ARGUS-binary interoperability for
sharing files with lenders and JV partners, and no SOC-2 / enterprise trust layer. Several
features (live market context, FEMA flood lookup, cloud save) depend on external services that
must be reachable and are best-effort. Stress sizes in the risk tools are fixed moderate
defaults, not calibrated to a specific market. It is a free, in-house tool — extremely capable
for underwriting and committee work, deliberately not a licensed data-and-interop platform.

**California Prop 13 reassessment.** A purchase is a change of ownership, so the property is
reassessed to the purchase price and property tax is computed as an effective rate × price
(the 1% base plus local assessments, typically ~1.1–1.25%), rising at most 2%/yr until the
next sale. Reassessment is **on by default** in the Acquisition section: the property-tax
expense line (identified by an `isTax` flag or a Prop 13 / property-tax name) is sourced from
the purchase price — so it scales correctly under any price change in a sensitivity, goal-seek,
or optimizer run — and its growth is capped at 2%. Turn it off to carry a manual tax amount;
the health check flags that choice, since carrying the seller's basis overstates going-in NOI.
Simplification: like every other expense in the engine, the reassessed tax escalates smoothly
(month by month) rather than stepping once per assessment year, and supplemental-roll timing
on the first bill is not modeled.

**Loan maturity / balloon.** A loan's term (the months until the balloon is due) is now modeled
separately from its amortization. Set a **loan term** in the debt section: if it is shorter than
the hold, the balloon comes due before sale, and rather than silently carrying the original loan
to sale at the original rate, the engine forces a refinance at maturity using the refinance-section
terms — re-sizing the loan to the property's then-current value at the new rate, with a financing
cost, and a cash-in if proceeds fall short (or a cash-out if value rose). A term of 0 (or one at or
beyond the hold) keeps the original behavior, so the shipped presets — which carry no term — are
unchanged. If you schedule your own refinance at or before maturity, that takes precedence; a refi
scheduled after maturity is overridden by the forced take-out. The health check flags the maturity
and any required cash-in. The model still supports a single refinance event over the hold (one
take-out, not a chain of rolling maturities).

**GP catch-up and clawback.** The promote waterfall now supports a GP catch-up. Without it, the
promote applied only to profit above the preferred return, so the GP was under-promoted relative to
what most institutional LP agreements specify. Turn on **GP catch-up** in the equity section and,
after the LP receives return of capital and its pref, the GP takes the catch-up share (default
100%) of distributions until the GP's profit equals the promote times the *whole* profit above
capital — so a 20% promote yields the GP 20% of all profit, not just the band above the pref. A
partial catch-up (e.g. 50%) reaches the same final split when it completes, differing only in
timing; it must exceed the promote to ever complete. A separate **clawback** toggle adds a final
true-up that returns GP profit to the LP — capped at the GP's profit — if the LP's lifetime cash
flows fail to clear the pref (for example after an early refinance promote and a later capital
call). The catch-up and clawback apply to the single pref/promote waterfall; the multi-tier
IRR-hurdle waterfall is a separate structure and takes precedence when enabled. Both are opt-in,
so the default waterfall and the shipped presets are unchanged.

**Sponsor (GP) fees.** The model now charges the standard sponsor fees: an **acquisition fee**
(% of price, at close), a **financing fee** (% of each loan, at close and at any refinance), an
ongoing **asset-management fee** (on EGI, NOI, invested equity, or a flat dollar amount), a
**disposition fee** (% of gross sale), and a **construction-management fee** (% of capex). Fees are
transfers from the equity pool to the GP, so they leave deal-level returns — project IRR, equity
multiple, and value — unchanged, and instead shift the LP/GP split: the pool the promote waterfall
divides is reduced by the fees and the GP receives them on top, so the LP bears the fees on its
capital. The LP IRR is therefore shown after fees and promote, while the project return is the
fee-free asset performance. These are the *sponsor's* fees, kept separate from lender points (which
sit in closing and refinance costs). All fees default to 0, so deal-level metrics and the presets
are byte-identical. The fee total and its impact are surfaced in the health check.

**Stepped rent schedules.** A lease can carry an explicit rent schedule that overrides its
single escalation rate. In the rent roll, the **Rent steps** field takes `month:rent` pairs measured
from lease commencement — e.g. `0:3, 36:3.6, 60:4.2` means $3.00/SF/mo for the first three years,
$3.60 for years four and five, and $4.20 thereafter. The rent is the last step at or before the
current lease month and is flat between steps; before the first step it is the base rent. Because
the schedule is keyed to commencement, an in-place lease that began before acquisition correctly
lands on whichever step is current at the analysis start. This represents the negotiated bumps that
are routine in ARGUS office and retail leases and that a single growth rate cannot express; the
natural percentage-rent breakpoint follows the stepped rent as well. Leases without a schedule use
the escalation path unchanged, so the presets stay byte-identical.
