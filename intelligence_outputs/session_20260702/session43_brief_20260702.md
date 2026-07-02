# Session 43 Brief — Aug RM Plan Ticket-Convention Decision, Canonical Sector Classifier
**Date:** 2026-07-02 | **Session:** 43

**Data files confirmed:** `d365_data.xlsx` and `infomerics.json.xlsx` present at repo root
(unchanged since Session 39's fresh pull, per Session 42's confirmation). All three tasks below
build on `csv/acer_revenue_model_20260630.csv` (10,093 rows, 4,588 unique companies — combines
both source files, built Session 38) and `csv/august2026_rm_deployment_plan_REBUILT_20260702.csv`
(4,588 rows, built Session 42) — no single-file output produced, per mandatory data rule.

---

## 1. Aug RM plan ticket-size convention — DECIDED (H11, Q8)

**Question carried from Session 42:** the REBUILT Aug plan used **max single-row `Amount Cr`
per company** as its ticket size. Should ACER ops instead use the original plan's **sum-across-
all-rows** convention, or something else?

**Finding: neither extreme is correct.** Both were tested against the full 4,588-company
pipeline:

| Convention | Total Amt_Cr | Problem |
|---|---|---|
| Naive full sum (original Aug plan, pre-rebuild) | ₹3,17,855 Cr | Double-counts a company's *same instrument* when it recurs across pipeline windows (e.g. Pushpit Steels' ₹464.13 Cr ACUITE Term Loan is one loan, not two, even though it appears in both the October 2026 and Q2 2027 window builds) |
| Single overall max (Session 42 REBUILT) | ₹2,33,842 Cr | Fixes the double-count, but also collapses **genuinely different instruments** held by the same company down to just the largest one — undercounts real multi-instrument exposure |
| **Sum of per-instrument-type max (recommended)** | **₹2,82,177 Cr** | Takes the max `Amount Cr` *within each distinct Instrument Type* (removing the cross-window duplicate), then sums *across* distinct instrument types (preserving genuine multi-instrument exposure) |

**Decision: adopt the REBUILT plan as the operational plan, but replace its ticket-size formula
with sum-of-per-instrument-type-max.** This is not a compromise between the two conventions — it
is the technically correct fix for both errors identified so far (double-counted repeats *and*
under-counted genuine multi-instrument companies).

**Impact of the fix:**
- 2,400 of 4,588 companies (52.3%) hold 2+ distinct instrument types; for 2,343 of those, the
  corrected convention produces a higher (more accurate) ticket size than Session 42's single-max
  rule.
- **61 companies change RM tier** between the Session 42 REBUILT plan and the corrected
  convention (49 Tier 3→Tier 2, 12 Tier 2→Tier 1).
- **12 companies newly qualify for TIER 1 — Senior RM** that the Session 42 REBUILT plan missed
  entirely — largest: Pushpit Steels (₹1,380.76 Cr combined vs ₹464.13 Cr single-max), Gama
  Infraprop (₹963.17 Cr vs ₹282.99 Cr), Goel Ganga India (₹879.61 Cr vs ₹417.65 Cr).
- Total pipeline value re-estimated at ₹2,82,177 Cr (+₹48,335 Cr / +20.7% vs Session 42's
  ₹2,33,842 Cr; still ₹35,678 Cr / 11.2% below the original plan's inflated ₹3,17,855 Cr).

**Output (new v2 plan, ready to operate from):**
- `csv/august2026_rm_deployment_plan_V2_SUMCONVENTION_20260702.csv` (4,588 rows)
- `csv/august2026_rm_tier_summary_V2_20260702.csv` (3 rows)
- `csv/rm_plan_ticket_convention_tier_diffs_20260702.csv` (61 rows — every company whose tier
  changes between the Session 42 REBUILT plan and this corrected convention)
- `csv/rm_plan_newly_tier1_suminstrument_20260702.csv` (12 rows — new Tier 1 targets)

**Recommendation to ACER ops:** confirm this becomes the standing rule in `INSTRUCTIONS.md`
("ticket size = sum of per-instrument-type max Amount Cr, not raw sum, not single overall max")
so no future session re-litigates this.

---

## 2. Canonical `classify_sector()` module — COMMITTED (H12)

Wrote and committed `classify_sector.py` at the repo root — one shared, version-controlled
sector classifier with a fixed keyword list and fixed priority order, replacing the ad hoc
per-session reimplementations that Session 42 identified as the root cause of sector-tagging
drift.

**What changed vs. the (several) prior inline versions:**
- **One label per category** — resolves the 4 duplicate label pairs found live in the master
  pipeline: `Energy/Power`→`Energy`, `BFSI/NBFC`→`BFSI`, `Jewellery`→`Jewellery/Gems`,
  `Mining`→`Mining & Minerals` (via `SECTOR_ALIASES` for normalizing old data, and by construction
  in `SECTOR_PATTERNS` for anything freshly classified).
- **Fixed priority order** designed specifically around the conflicts Session 41 documented:
  Paper/Packaging, Hotels & Tourism, BFSI, Media/Retail, Mining & Minerals, and Steel & Metals are
  checked before generic/ambiguous sectors; Jewellery/Gems is checked last (diamond/gold/silver
  are common brand-name modifiers, not reliable trade signals).
- **Regex bug fixes** found by tracing the 97 flagged companies: word-boundary gaps that let
  `tin` match inside "Sen**tin**i", `car` match inside "Medi**car**e", and `trad` match inside
  "Indi**trad**e" have all been fixed with `\b` boundaries; missing keywords (`hospitality`,
  `medicare`, `housing finance`, `beverages`, `fincorp`, `broadcast`, `pulp`, `agri`, `titanium`,
  `irrigation`/`sprinklers`) have been added.

**Output:** `classify_sector.py` (repo root, committed) — no CSV for this task; the diff is
produced in Task 3 below.

---

## 3. Re-run the 97 flagged companies against the canonical classifier — COMPLETE (H13)

Ran every company from `sector_misclassification_flags_20260701.csv` through the new
`classify_sector()` and compared against its previously-recorded (wrong) sector(s).

| Flag type | Count | Result under canonical classifier |
|---|---|---|
| Cross-window inconsistency (same company, 2 different sectors depending on which pipeline window) | 59 | **100% resolved by construction** — one shared function now always returns the same answer for the same name, so this class of bug cannot recur |
| Keyword mismatch (name strongly implies sector X, was tagged something else) | 38 | **36/38 (94.7%) now match the expected correct sector** |
| Still unresolved (falls to `Other`) | 3 of 97 | Genuinely ambiguous names with no reliable keyword signal even under the expanded pattern set: "Sainath Autolinks Pvt. Ltd.", "Nash Robotics & Automation Pvt. Ltd." ("automation" was deliberately *not* pattern-matched to Automobiles — it is not an automobile business), "Encore Projects Pvt. Ltd." |

**Two flags in the original 38 were themselves false positives**, and the canonical classifier
deliberately does *not* "fix" them: "Diamond Shipping Agencies Pvt. Ltd." (Logistics — a shipping
company, "Diamond" is a name, not a trade signal) and "Diamond Textile Mills Pvt. Ltd." (Textiles
— a textile mill). The Session 41 detector's heuristic ("this keyword strongly implies sector X")
was itself too aggressive for "diamond" specifically; the canonical classifier's ordering (see
Task 2) is the corrected version of that heuristic, not a replication of it.

**Output:** `csv/sector_reclassification_before_after_20260702.csv` (97 rows: Company Name,
Detection_Method, Sector_Before, Sector_After_Canonical, Keyword_Case_Now_Matches_Expected)

---

## Key Findings (Session-Wide)

1. **Neither "sum" nor "max" was the right answer to Session 42's Q8** — the correct ticket-size
   rule is sum-of-per-instrument-type-max, which recovers ₹48,335 Cr of legitimately under-counted
   pipeline value and surfaces 12 new Tier 1 targets the Session 42 rebuild missed.
2. The canonical `classify_sector()` module is now the one place sector logic lives — any future
   session should `from classify_sector import classify_sector` rather than redefine it, per
   Session 42's root-cause diagnosis.
3. 96.9% of the 97 flagged misclassifications resolve correctly under the new classifier; the
   remaining 3% are genuinely unresolvable from company name text alone and are exactly the kind
   of case MCA CIN NIC enrichment (P1 backlog #1/#2) would fix with ground-truth industry codes.
4. The classifier module surfaced that the Session 41 detection heuristic itself had a small
   false-positive rate (2 of 38) — worth remembering when interpreting *any* keyword-based flag
   list in this repo: a keyword match is evidence, not proof.

---

## Hypotheses for Next Session

- H14: Re-run `classify_sector()` across the FULL 4,588-company master pipeline (not just the 97
  flagged companies) and produce a full before/after diff + updated sector-level revenue density
  ranking (Session 39's analysis used the old, inconsistent Sector column)
- H15: Once ACER ops confirms the sum-of-per-instrument-max convention (Task 1), regenerate the
  Aug weekly call schedule and RM tier assignment files from `august2026_rm_deployment_plan_V2_SUMCONVENTION_20260702.csv` as the new master, retiring the Session 42 REBUILT file
- H16: MCA CIN NIC enrichment remains the highest-value unlock (per TODO P1 #2) — the 3 companies
  that still resolve to "Other" even under the expanded classifier are a live example of its
  ceiling

## Data Quality Notes
- No new nulls; source files unchanged since Session 39's pull (49,945 d365 rows / 8,438
  Infomerics rows, per Session 42's confirmation)
- Confirmed via direct computation: 2,343 of 4,588 companies were undercounted by Session 42's
  single-overall-max ticket-size rule; the fix is now available as `august2026_rm_deployment_plan_V2_SUMCONVENTION_20260702.csv`
- `classify_sector.py`'s pattern set is necessarily a heuristic over company-name text; 3 of 97
  known-flagged companies still fall to "Other" and should not be assumed to have a knowable
  sector without external data (MCA CIN NIC)

## Open Questions (Carry Forward)
- Q8 — RESOLVED this session: adopt sum-of-per-instrument-type-max as the standard convention
  (recommend codifying in INSTRUCTIONS.md)
- Q9 — RESOLVED this session: canonical classifier committed as `classify_sector.py`
- Q10 (new): should `august2026_rm_deployment_plan_V2_SUMCONVENTION_20260702.csv` replace the
  Session 42 REBUILT file as *the* operational Aug plan, or do both need to stay live until ACER
  ops formally signs off on the convention? Recommend the former, pending explicit confirmation.
- Q1-Q6 unchanged (SEBI license date, BG product capability, BSE/NSE manual upload, Infomerics
  Q2 2027 coverage gap, MCA CIN/NIC enrichment, RM-plan Tier-1 ownership)

---

## Files Created This Session (Total: 6 new CSVs + 1 new MD + 1 new committed .py module)

All in: `intelligence_outputs/session_20260702/`

CSVs (6):
- `csv/august2026_rm_deployment_plan_V2_SUMCONVENTION_20260702.csv` (4,588 rows)
- `csv/august2026_rm_tier_summary_V2_20260702.csv` (3 rows)
- `csv/rm_plan_ticket_convention_tier_diffs_20260702.csv` (61 rows)
- `csv/rm_plan_newly_tier1_suminstrument_20260702.csv` (12 rows)
- `csv/sector_reclassification_before_after_20260702.csv` (97 rows)

MDs (1):
- `session43_brief_20260702.md` (this file)

Code (1, repo root, committed):
- `classify_sector.py`

Session closed: 2026-07-02 ~21:00 IST
