# WBI7 ↔ ARGUS Interoperability — Plan

The honest version first: **the data models align well; the file format is the hard part, and the hard part is commercial, not technical.** WBI7 was deliberately built to mirror ARGUS's mechanics (market leasing assumptions, reimbursement methods, capital events, waterfall), so mapping the *meaning* of a deal between the two is mostly one-to-one. What's genuinely difficult is reading and writing ARGUS's native files, and that difficulty is about access and licensing, not about parsing skill.

This plan is tiered so the valuable, dependency-free work ships first and the partnership-gated work is scoped honestly.

---

## 1. The reality of ARGUS files

- **ARGUS Enterprise stores scenarios in a proprietary, database-backed format** (SQL Server for enterprise installs; a local store otherwise). The native files are undocumented and not meant to be read by third parties. Older ARGUS DCF `.sf` scenario files are likewise proprietary.
- **There is no open, public, round-trippable ARGUS cash-flow file format.** Industry XML efforts exist (OSCRE schemas, the old "aXML" idea), but none is a usable, ARGUS-native interchange you can rely on.
- **The supported integration path is the ARGUS Enterprise API / SDK**, available from Altus Group under their developer/partner program. Using it requires (a) an Altus partner agreement and API credentials, and (b) the customer running a licensed ARGUS Enterprise instance the connector can talk to.
- **ARGUS can export to Excel** (cash flows, rent roll, assumptions, reports), and accepts structured data via Excel/import templates for parts of the model. This is the one bridge that needs no partnership and no format license.

The consequence: "import/export ARGUS files" is really three different projects with very different costs. Treat them separately.

---

## 2. Why the semantics are the easy part

WBI7's model maps onto ARGUS almost field-for-field:

| ARGUS concept | WBI7 model | Notes |
|---|---|---|
| Property / areas | `property.suites[]` | direct |
| Tenants (rent roll) | `rentRoll[]` | direct; start month, term, base rent, free rent, TI/LC |
| Market Leasing Assumptions | `mlas[]` | WBI7 mirrors MLAs deliberately (renewal prob, downtime, new/renew TI-LC-free, market rent, escalation) |
| Tenant rent: flat growth **or stepped schedule** | `escalation` **or `rentSteps[]`** | stepped rent schedules now supported (month:rent from commencement) |
| Reimbursement: Net / Base-Year Stop / Fixed / Gross | `recMethod` = net / baseYear / fixed / none | direct; gross-up, admin fee, caps supported |
| Expenses: fixed, $/area | `expenses[]` (fixed / psf) | **gap:** ARGUS "% of EGR" expense basis is not yet in WBI7 |
| Capital expenditures | `capex[]` | direct (month, amount) |
| Debt / financing | `debt{}` | LTV/amount, IO, amort, **loan term/maturity → forced refi**, floating, mezz, prepay |
| Yield / resale (exit cap) | `exit{}` | direct; **gap:** ARGUS gross-price / $-per-area exit not yet supported |
| Inflation / market rates | growth fields | direct |
| Partnership / distribution | `equity{}` | pref, promote, **catch-up, clawback, sponsor fees**, multi-tier IRR hurdles |
| Property tax | `expenses[].isTax` + Prop 13 reassessment | WBI7 adds CA reassessment on top |

Of the WBI7 gaps that mattered for a clean import, **stepped rent schedules are now done** (the most important one — ARGUS office/retail leases routinely carry negotiated steps a single growth rate can't express). Two small, self-contained engine additions remain and should be closed before Phase 2 so imported deals don't silently lose detail: the **% of EGR expense basis** and **gross-price / $-per-area exit**.

---

## 3. The plan

### Phase 0 — Formalize the WBI7 interchange format *(no dependencies; ~1 week)*

WBI7 already exports and imports its own deal file (`serializeDeal` / `parseDealFile`). Turn that into a **stable, versioned, documented interchange schema** — `wbi7-deal-v1` — so any tool (or an ARGUS Excel export, via Phase 1) can target it.

- Freeze the JSON schema, add a `schemaVersion`, and document every field with units and conventions (most rates are decimals; some UI-facing fields are percents — that ambiguity must be written down).
- Publish the ARGUS-concept mapping table above as the canonical crosswalk.
- Add a migration shim so older deal files load forward.

**Unlocks:** a clean target for every later phase, and a format the technical co-founder (or anyone) can write against without reverse-engineering anything.

### Phase 1 — Excel bridge *(no partnership needed; ~3–4 weeks)*

This is where most of the practical value is, and it needs no ARGUS license or Altus relationship.

1. **Importer (ARGUS → WBI7).** Read ARGUS's Excel exports and generic rent-roll spreadsheets into the WBI7 model. Build a column-mapping step (the user points "Tenant", "SF", "Start", "Term", "Base Rent", "Recovery", … at WBI7 fields), persist the mapping as a template, and populate `rentRoll[]`, `expenses[]`, and `mlas[]`. This subsumes the "paste-from-Excel" item on the review list and the rent-roll-import gap — the single biggest workflow blocker for live deals.
2. **Exporter (WBI7 → ARGUS-shaped Excel).** Emit a workbook laid out to match ARGUS Enterprise's import templates (rent-roll tab, MLA tab, expense tab, assumptions tab) so a user can move a WBI7 deal *into* ARGUS with minimal hand-keying.
3. **Reconciliation report.** After an import, run WBI7's engine on the imported inputs and produce a **line-by-line NOI and cash-flow comparison against the ARGUS figures contained in the same export.** This is the trust artifact: it makes the "WBI7 reproduces ARGUS from the same inputs" claim tangible, and it surfaces exactly where a difference comes from (e.g. a % of EGR expense WBI7 approximated, or a stepped rent it flattened).

**Unlocks:** real two-way movement of the data that actually changes between the tools (rent roll + assumptions), plus a credible, auditable reconciliation. Close the remaining engine gaps (% of EGR expenses, gross-price exit) first so the reconciliation comes out clean; stepped rent is already handled.

### Phase 2 — ARGUS Enterprise API/SDK connector *(partnership-gated; months, not weeks)*

The only way to read and write ARGUS's *native* scenarios reliably.

- **Prerequisites (these are the real blockers, not the code):** an Altus Group partner agreement and API credentials; a design-partner customer (Wang Brothers) running a licensed ARGUS Enterprise instance the connector is allowed to reach; and review of the API terms for what may be read/written and stored.
- **Scope once unblocked:** authenticate; pull a property/scenario; map it through the `wbi7-deal-v1` schema (the Phase 0 crosswalk does the heavy lifting); optionally push WBI7 edits back as a new scenario. Start read-only; add write only after reconciliation is trusted.

**Unlocks:** native, no-Excel round-tripping — the genuine "interop" an enterprise buyer means. Entirely dependent on the commercial relationship; the engineering is straightforward once access exists.

### Not pursuing — binary/database reverse-engineering

Directly parsing `.sf` or the ARGUS Enterprise data store is **out of scope and not recommended.** It almost certainly violates the ARGUS license, it breaks every time Altus changes the format, and it becomes a permanent maintenance liability. The Excel bridge captures most of the value legally; the API captures the rest, properly. There is no good reason to reverse-engineer the binaries.

---

## 4. Recommended sequence and effort

1. **Phase 0** (1 wk) — formalize `wbi7-deal-v1` + crosswalk. Do this regardless; everything else leans on it.
2. **Engine gaps** (~1 wk) — % of EGR expenses and gross-price exit. (Stepped rent is done.) Needed for clean imports and worth having anyway.
3. **Phase 1** (3–4 wks) — Excel importer + exporter + reconciliation report. This is the highest value-per-effort and unblocks live deals immediately.
4. **Phase 2** (gated) — begin the Altus partner conversation in parallel; build the connector only once credentials and a licensed instance exist.

The framing to hold onto: **WBI7 already matches ARGUS on the math.** Interop doesn't require closing a modeling gap — it requires a data bridge. Phases 0–1 deliver that bridge with no outside dependencies and make the "reproduces ARGUS" claim demonstrable; Phase 2 is real but is a business-development task with an engineering tail, not the other way around.
