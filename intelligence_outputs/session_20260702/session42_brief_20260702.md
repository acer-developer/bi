# Session 42 Brief — Aug RM Plan Rebuild, Tier 2 Gap Check, Sector-Tagging Root Cause
**Date:** 2026-07-02 | **Session:** 42

**Data files confirmed:** `d365_data.xlsx` (49,945 rows) + `infomerics.json.xlsx` (8,438 rows) —
unchanged since Session 39's fresh pull. All three tasks below build on
`csv/acer_revenue_model_20260630.csv` (10,093 rows, 4,588 unique companies — itself built from
both source files in Session 38), cross-referenced against
`csv/august2026_rm_deployment_plan_20260630.csv` (1,608 rows / 1,565 unique companies).

---

## 1. Aug RM Deployment Plan — REBUILT from full 4,588-company master pipeline (H8)

**Decision:** Rebuild wholesale (per Session 41's Q7), not patch incrementally — the gap was
too large (77%) to close with targeted additions.

**Method:** Applied the plan's own documented Tier logic to every company in the master
pipeline, not just the 4 source groups (Multi-Window / Dual-Quarter / Q1-Construction /
Ghost-HOT, 1,608 companies) the original plan was built from.
- Per company: `Amt_Cr` = **max** single-instrument `Amount Cr` across all its rows (see Data
  Quality Note below on why max, not sum), `NCD` = 1 if any instrument is NCD, `Windows` /
  `Window_Count` = distinct Pipeline_Windows the company appears in.
- **TIER 1 — Senior RM:** Amt_Cr ≥ ₹500 Cr OR NCD-linked
- **TIER 2 — Mid-RM:** Amt_Cr ₹100–499 Cr OR 2+ windows (and not already Tier 1)
- **TIER 3 — Junior/Tele-sales:** everything else
- Aug week: Tier 1 → Wk1, Tier 2 → Wk2, Tier 3 (multi-window or HOT/MEDIUM urgency) → Wk3,
  remaining Tier 3 → Wk4

**Result:**

| Metric | Original Plan | Rebuilt Plan |
|---|---|---|
| Unique companies | 1,565 | **4,588** |
| Tier 1 — Senior RM | 273 | **738** |
| Tier 2 — Mid-RM | 813 | **940** |
| Tier 3 — Junior/Tele | 522 | **2,910** |
| Total Amt_Cr | ₹1,26,959 Cr | **₹2,33,842 Cr** |

- **3,023 companies (66%)** existed in the master pipeline but were completely absent from the
  original plan — confirms and quantifies Session 41's 77% Tier-1-specific gap at full-pipeline
  scale.
- Of 1,565 companies common to both plans: 1,526 kept the same tier; **39 changed tier** — 17
  were downgraded from the original's Tier 1 to Tier 2 under the rebuild's per-instrument-max
  rule (see Data Quality Note), 21 were downgraded Tier 2→Tier 3, 1 upgraded Tier 2→Tier 1.
- **0 companies** in the original plan are absent from the master pipeline — the master pipeline
  is a strict superset (no name-matching orphans).

**Output:**
- `csv/august2026_rm_deployment_plan_REBUILT_20260702.csv` (4,588 rows — **new master RM plan**)
- `csv/august2026_rm_tier_summary_REBUILT_20260702.csv` (3 rows)
- `csv/rm_plan_rebuild_newly_added_20260702.csv` (3,023 rows — companies the original plan missed entirely)
- `csv/rm_plan_rebuild_tier_changes_20260702.csv` (39 rows)
- `csv/rm_plan_rebuild_removed_20260702.csv` (0 rows — confirmed empty, no orphans)
- `csv/rm_plan_rebuild_reconciliation_20260702.csv` (15-row summary)

---

## 2. Tier 2 capture-gap check (H10) — is the defect uniform across tiers?

**Answer: NOT uniform, and not really a "tier" defect at all — it's a "was this company in one
of the 4 original source groups" defect**, which happens to hit Tier 1 much harder than Tier 2.

Mirrored Session 41's row-level methodology on the Tier 2 band (₹100–499 Cr, non-NCD):

| Segment | Unique Companies | Not Captured | Gap % |
|---|---|---|---|
| Amount-band trigger only (₹100–499 Cr, non-NCD) | 297 | 186 | **62.6%** |
| Multi-window trigger (2+ windows, <₹500 Cr, non-NCD) | 740 | 0 | **0.0%** |
| **All Tier 2 triggers combined** | 982 | 186 | **18.9%** |
| *Reference — Tier 1 (≥₹500 Cr), Session 41* | 61 | 47 | **77.0%** |

The multi-window population has a **perfect 0% gap** because "Multi-Window" was literally one
of the 4 groups (869 companies) the original plan was built from. The amount-band-only
population — single-window companies whose only qualifying signal is ticket size — has a
**62.6% gap**, nearly as severe as Tier 1's 77%. Tier 2's blended 18.9% gap looks much better
than Tier 1's only because more Tier 2 companies happen to also carry the multi-window signal.

**Conclusion:** the real fault line isn't Tier 1 vs Tier 2 — it's "flagged by one of the 4 ad hoc
source groups" vs "not." This is fully resolved by the Section 1 rebuild, which ignores source
groups and re-applies the tier rule to every company directly.

**Output:**
- `csv/tier2_capture_gap_100_499cr_all_20260702.csv` (1,139 rows)
- `csv/tier2_capture_gap_100_499cr_summary_20260702.csv` (3 rows)

---

## 3. Root cause of Oct-2026 vs Q1/Q2-2027 sector-tagging divergence (H9)

Investigated the 59 companies (from Session 41) that get a genuinely different **specific**
sector depending on which pipeline window (October 2026 / Q1 2027 / Q2 2027) their row came
from — e.g. "Diamond Beverages Pvt. Ltd." tagged `Jewellery/Gems` in October 2026 rows but
`Agro & Food` in Q2 2027 rows.

**Finding — confirmed root cause: no single, shared, version-controlled sector-classification
function exists in this repo.** Each pipeline window was built in a different session via an
inline, ad hoc re-implementation of keyword-based `classify_sector()`. Evidence:

1. **All 59 companies are internally consistent within each window** (100%, 0 exceptions) — the
   sector never fluctuates row-to-row inside one window, only *across* windows. This rules out
   random noise and points squarely at "different classifier version per window-build session."
2. Two of the surviving analysis scripts in the repo (`session27_analysis.py`,
   `session28_analysis.py`) contain **byte-identical** `SECTOR_PATTERNS` dictionaries — proving
   at least some sessions did try to reuse logic. But neither script's labels match what's
   actually in the live master pipeline: the scripts use slash-separated names
   (`Agro/Food`, `Chemicals/Pharma`, `Steel & Metals`) while `acer_revenue_model_20260630.csv`
   contains a **mix of both slash and ampersand variants for the same concept**
   (`Energy` / `Energy/Power`, `BFSI` / `BFSI/NBFC`, `Jewellery` / `Jewellery/Gems`,
   `Mining` / `Mining & Minerals`) — proof that whatever built the final master pipeline
   (Sessions 33–37) used a **third, unsaved** classifier variant, not the ones on disk.
3. Company names driving the 59 conflicts are inherently ambiguous by keyword alone — e.g.
   "Gowthami **Solvent** **Oils**" matches both a chemicals keyword (solvent) and an agro
   keyword (oils); "Safal **Seeds** & **Biotech**" matches both agro (seeds) and
   chemicals/pharma (biotech); "**Diamond** **Beverages**" matches both jewellery (diamond) and
   (loosely) food/beverage. Which keyword "wins" is purely a function of the keyword-priority
   order coded into whichever classifier version ran for that window — there is no ground-truth
   sector in either source file to arbitrate.

**This is the same underlying defect already flagged in Session 39** ("fixed duplicate sector
labels before scoring" — but only in that session's own output, not at the source), and explains
the other 198 Other↔specific mismatches from Session 41 as well, not just the 59 specific↔specific
ones.

**Permanent fix (not attempted this session — flagged for P1):** either (a) write ONE
`classify_sector()` module, commit it to the repo, and require every future session to import it
rather than redefine it inline, or (b) the already-planned MCA CIN NIC code enrichment (P1 #1 on
the backlog) to get a real, external ground-truth industry code instead of inferring sector from
company name text.

**Output:** `csv/sector_tagging_root_cause_20260702.csv` (59 rows — per-company window-by-window
sector and instrument-type breakdown showing the internal-consistency proof)

---

## Data Quality Notes

- **Amount aggregation choice (max vs sum):** the original Aug RM plan appears to have **summed**
  `Amount Cr` across all of a company's rows when a company had the *same instrument* repeated
  across multiple pipeline windows (e.g. Pushpit Steels' ₹464.13 Cr ACUITE Term Loan appears
  identically in both the October 2026 AND Q2 2027 window builds) — inflating its ticket size to
  ₹1,538 Cr and pushing it into Tier 1. The same instrument recurring across windows reflects the
  window-build scripts' independent forward-looking escalation logic, not two separate loans.
  The rebuild uses **max** per company to avoid this double-count; this is why 17 companies that
  were Tier 1 in the original plan are Tier 2 in the rebuild. Recommend ACER ops confirm which
  convention (max vs sum) should be the standard going forward — this session used max as the
  more conservative, defensible default, but no formal specification exists in `INSTRUCTIONS.md`.
- Instrument Type labels also drift between windows for what appears to be the same instrument
  (`Term Loan` vs `Term loans`, `NCD/Bond` vs `Non-government debt`) — same "separate build per
  window, no shared normalization" root cause as the sector-tagging finding above.
- No new nulls found. Source files unchanged since Session 39.

## Open Questions (Carry Forward)
- Q1–Q7 unchanged from Sessions 40–41 (SEBI license date, BG product capability, BSE/NSE manual
  upload, Infomerics Q2 2027 coverage gap, MCA CIN/NIC enrichment, RM-plan Tier-1 ownership,
  rebuild-vs-patch decision — now resolved by this session in favor of rebuild)
- **Q8 (new):** Should ACER ops adopt max-per-company (this session's convention) or
  sum-per-company (the original plan's convention) as the standard ticket-size aggregation rule?
- **Q9 (new):** Should a canonical `classify_sector()` module be committed to the repo this week,
  ahead of the MCA CIN NIC enrichment (which would take longer to complete)? Quick win vs
  long-term fix.

## Files
- `csv/august2026_rm_deployment_plan_REBUILT_20260702.csv` (4,588 rows)
- `csv/august2026_rm_tier_summary_REBUILT_20260702.csv` (3 rows)
- `csv/rm_plan_rebuild_newly_added_20260702.csv` (3,023 rows)
- `csv/rm_plan_rebuild_tier_changes_20260702.csv` (39 rows)
- `csv/rm_plan_rebuild_removed_20260702.csv` (0 rows)
- `csv/rm_plan_rebuild_reconciliation_20260702.csv` (15 rows)
- `csv/tier2_capture_gap_100_499cr_all_20260702.csv` (1,139 rows)
- `csv/tier2_capture_gap_100_499cr_summary_20260702.csv` (3 rows)
- `csv/sector_tagging_root_cause_20260702.csv` (59 rows)
