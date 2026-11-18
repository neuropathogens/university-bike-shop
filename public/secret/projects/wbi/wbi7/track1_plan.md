# WBI7 → beating ARGUS: Track 1 build order (the software)

This is the **buildable** track — the engine, features, and workflow that can make
WBI7 the best *technical* underwriting experience. It is sequenced so each item is
additive, fully testable, and keeps the 25 presets byte-identical (the discipline
that has held for every feature so far: 460+ assertions, all green).

It deliberately does **not** include the moat (ARGUS-file interop, licensed data
feeds, SOC 2, distribution). Those are not code — they need a funded company,
contracts, and years. See the conversation summary; they're tracked separately as
"Track 2" and gated on real-world adoption, not engineering.

Legend — effort: S (≈1 session) · M (2–3) · L (4+).  Risk: ★ low (additive) ·
★★ moderate (touches shared paths) · ★★★ high (golden-path surgery / external deps).

---

## Done (this session and before)
The acquisition engine is already at rough parity for the core four asset classes:
monthly lease-level DCF, blended rollover (renewal prob, downtime, TI/LC, free
rent), recoveries (net / base-year / fixed, gross-up, admin fee, caps), percentage
rent, reserves, forward-NOI exit, a full debt stack (fixed, **floating-with-caps**,
IO/amortizing, refinance, **mezzanine**, **step-down prepayment**), LP/GP waterfalls
with tiered hurdles, inflation/CPI, after-tax. Plus analytics ARGUS doesn't bundle:
Monte Carlo, tornado, goal-seek, hold-period optimization, scenario compare, fund
roll-up, development pro forma, and an IC-summary export.

- **[DONE this session] Live market context (data integration, first step).** Free
  public data keyed to property location — US Census ACS demographics + Treasury
  benchmarks via an optional proxy — shown as honest *context* (not licensed comps).
  Parsers fixture-tested; live fetch degrades gracefully. *(S, ★)*

---

## Phase 1 — AI-native workflow (the real wedge; hardest for ARGUS to answer)
This is where WBI7 can be *categorically* better, not just cheaper. ARGUS is a
30-year desktop architecture; the win is making the workflow an order of magnitude
faster, not matching its forms.

1. **Rent-roll & T-12 ingestion.** Drop a messy broker PDF/Excel rent roll or
   trailing-12 operating statement → structured leases + expenses auto-populated.
   Parse + map + a review/confirm step (never silently trust extraction). *(L, ★★)*
2. **Natural-language deal entry & edits.** "Add a 10k SF tenant at $32 NNN, 7-yr
   term, 3% bumps, starting month 6." → rows created. *(M, ★★)*
3. **Assumption anomaly detection.** Flag inputs that are off-market vs the loaded
   context (rent far above area median, exit cap below going-in, etc.). *(S, ★)*
4. **IC-memo narrative generation.** Turn the model into a written investment memo
   (thesis, risks, sensitivities) on top of the existing one-page export. *(M, ★)*

## Phase 2 — Engine depth to full parity
Close the places ARGUS is genuinely deeper.

5. **Audit drill-down.** Click any output → trace to the lease-by-lease,
   month-by-month math. The big differentiator (transparent glass box vs black
   box). *(L, ★★)*
6. **Recovery/reimbursement depth.** Expense pools, recovery ratios, stops + caps
   interacting, base-year details across the full matrix. *(M, ★★)*
7. **Lease-option modeling.** Expansion/contraction options, blend-and-extend,
   multiple abatements, more percentage-rent variants, market-leasing profiles by
   space type. *(M, ★★)*
8. **Reporting library + Excel round-trip.** Read standard rent-roll/T-12 templates;
   export the standardized reports the industry recognizes. The pragmatic on-ramp
   to interop. *(M, ★)*

## Phase 3 — Asset-type engines (where ARGUS is property-type-aware)
9.  **Multifamily unit-mix** (unit types, in-place vs market, loss-to-lease,
    renewal vs new-lease trade-out, concessions). *(M, ★★)*
10. **Hospitality** (RevPAR / ADR / occupancy-driven NOI, departmental expenses,
    management fees, FF&E reserve). *(M, ★★)*
11. **Self-storage & other operationally-intensive types** (unit-mix, churn,
    ECRI). *(M, ★★)*

## Phase 4 — Structure & scale
12. **Partial-interest / JV & co-invest** beyond the current single waterfall
    (multiple partners, side pockets, GP catch-up nuances). *(M, ★★)*
13. **Ground leases** (subordinated/unsubordinated, look-back, resets). *(S, ★★)*
14. **Portfolio at scale** (consolidate many assets, cross-collateralized debt,
    fund-level fees and subscription lines — extends today's fund roll-up). *(M, ★★)*

---

## Sequencing rationale
Do **Phase 1 first.** Adoption is the wedge that earns the right to attack the moat;
AI-native ingestion and NL entry are what make a small shop or analyst pick WBI7
over ARGUS for speed, and they're the features ARGUS structurally can't ship.
Phase 2's audit drill-down is the credibility anchor (transparency beats a black
box). Phases 3–4 broaden coverage once the workflow advantage is real.

**Recommended next item:** #1 (rent-roll / T-12 ingestion) — most differentiated,
directly extends this session's data work, and turns the painful first hour of any
underwrite into a drop-and-confirm. It's an `L` with extraction review built in so
we never trust a parse blindly.
