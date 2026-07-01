# ACER Intelligence — Session 41 Brief
Date: 2026-07-01 | Session #41

Source files (read fresh, both combined per mandatory data rule):
- `d365_data.xlsx`: 49,945 raw rows
- `infomerics.json.xlsx`: 8,438 rows
- Both already unified into `csv/acer_revenue_model_20260630.csv` (10,093-row, 4,588-unique-company
  forward pipeline built from both files in Session 38) — reused per standing practice for all
  three tasks below, cross-referenced against `csv/august2026_rm_deployment_plan_20260630.csv`
  (1,608 unique companies) and `csv/ncd_rm_plan_gap_all_agencies_20260701.csv` (695 rows, Session 40).

---

## 1. Aug Wk2/Wk3 NCD Call Schedule — the 454 uncaptured NCD companies (answers H5)

Session 40 flagged 454 of 695 NCD company-agency pairs (65.3%) as absent from the Aug RM
deployment plan. This session builds the actual week-by-week assignment.

**Rule applied:** all 454 are NCD-linked, so per the RM plan's own Tier 1 trigger (≥₹500 Cr
OR NCD-linked → Tier 1 Senior RM), every row is assigned **TIER 1 — Senior RM**. Week split is
by escalation urgency (how soon the Call_Window closes):
- **Aug Wk2 (Aug 10–14):** companies whose Call_Window falls in Sep/Oct 2026 or "Call now" — 157 companies, ₹5,410 Cr
- **Aug Wk3 (Aug 17–21):** companies whose Call_Window falls Nov 2026 – Jan 2027 (more runway) — 297 companies, ₹17,584 Cr

| Agency | Aug Wk2 | Aug Wk3 |
|---|---|---|
| IND-RA | 76 | 150 |
| CARE | 45 | 76 |
| ICRA | 26 | 50 |
| BRICKWORK | 7 | 21 |
| Infomerics | 3 | 0 |

**Capacity note:** the existing RM plan already has 792 companies in Aug Wk2 (vs. only 48 in
Aug Wk3). Adding 157 more to Wk2 pushes it to ~949; Aug Wk3 goes from 48 to 345, which is a much
better fit for available slack. If RM bandwidth is tight, consider shifting the Wk2 additions to
telesales/junior RM lanes rather than senior RM calendars.

Output: `csv/ncd_aug_wk2_wk3_schedule_20260701.csv` (454 rows) + `csv/ncd_aug_wk2_wk3_agency_summary_20260701.csv` (agency × week rollup)

---

## 2. Does the Tier-1-only capture gap extend beyond NCD? (answers H6)

Tested whether non-NCD companies meeting the ≥₹500 Cr Tier 1 trigger have the same capture
problem as NCD companies.

| Segment | Total companies | Not captured in Aug RM plan | Gap % |
|---|---|---|---|
| Non-NCD ≥₹500 Cr | 52 | 40 | **76.9%** |
| NCD ≥₹500 Cr (same threshold, for comparison) | 9 | 7 | 77.8% |
| **All ≥₹500 Cr combined** | **61** | **47** | **77.0%** |

**Finding: the gap is not NCD-specific — it is actually slightly worse for non-NCD high-value
companies (76.9%) than the NCD-specific gap found in Session 40 (65.3% on the full NCD
population).** The RM plan's Tier 1 auto-routing logic is under-capturing high-value companies
broadly, regardless of instrument type. This means the 273-company Tier 1 list in the existing
Aug deployment plan is missing roughly 3 out of 4 companies that meet its own stated ≥₹500 Cr
threshold — a build-time coverage bug in how the Tier 1 list was assembled, not a
threshold-design problem.

Output: `csv/tier1_capture_gap_500cr_all_20260701.csv` (61 rows, full lead-list format) +
`csv/tier1_capture_gap_500cr_summary_20260701.csv` (3-row segment summary)

---

## 3. Sector-classification false positives beyond Jewellery (answers H7)

Session 40 found 2–3 keyword-misclassified companies in the 53-company Jewellery sector
("Diamond Beverages", "Silvertoan Papers", "Goldenglobe Hotels"). This session checked whether
similar misclassification exists elsewhere, using two independent detection methods:

**Method A — cross-window sector inconsistency (new, stronger evidence):** the same company
appears with a *different* Sector label depending on which pipeline window (October 2026 vs.
Q1 2027 vs. Q2 2027 source file) it came from. Example confirmed manually: **"Just Textiles
Ltd."** is tagged `Textiles` in its Q2 2027 rows but `Construction` in its October 2026 rows —
same company, same underlying business, conflicting label. Across the whole file:
- 198 companies show an Other ↔ specific-sector inconsistency (expected — matches the known,
  already-documented "Other bucket reclassification coverage gap" from Session 5/11, not new)
- **59 companies show a specific-sector ↔ specific-sector conflict** (genuinely new finding) —
  the largest clusters: Construction↔Textiles (9), Automobiles↔Manufacturing (7),
  Agro & Food↔Textiles (5), Chemicals & Pharma↔Healthcare (5), Agro & Food↔Energy (4)

**Method B — keyword mismatch (same method as the original Jewellery finding):** company name
contains an unambiguous business-type word for a different sector than the one it's tagged with
(e.g., "K K V Agro Powers Ltd." tagged `Agro & Food` but name signals `Energy`; "Diamond
Beverages Pvt. Ltd." tagged `Jewellery/Gems` but clearly `Agro & Food` — this one is caught by
*both* methods, cross-validating them). 42 companies flagged.

**Combined: 97 unique companies flagged** (4 companies caught by both methods).
Steel & Metals and Energy — the two sectors named in the task — do appear in the list but are
not disproportionately affected; Construction↔Textiles and Automobiles↔Manufacturing are the
biggest clusters, not Steel/Energy specifically.

**This raises the stakes on the MCA CIN/NIC enrichment case further**: the cross-window method
shows the classification problem isn't confined to ambiguous keyword overlaps (like "Diamond" =
gem or beverage) — the *same* company can get two different sector labels purely because of
which quarterly pipeline extract it was pulled from, meaning at least two of the three source
pipelines use inconsistent sector-tagging logic for an overlapping set of ~260 companies.

Output: `csv/sector_misclassification_flags_20260701.csv` (97 rows)

---

## Key Findings (Session-Wide)

1. **The Tier-1 capture gap is a systemic RM-plan build defect, not an NCD- or
   threshold-specific issue** — 77% of all ≥₹500 Cr companies (NCD or not) are missing from the
   Aug plan despite meeting its own auto-routing rule. Recommend the RM plan be rebuilt from the
   full 4,588-company master pipeline with the Tier logic re-applied, rather than patched
   piecemeal per finding.
2. The 454 uncaptured NCD companies now have a concrete Aug Wk2/Wk3 schedule (157 / 297 split by
   urgency) ready for RM assignment.
3. Sector misclassification is broader than the Jewellery-specific finding suggested — 59
   companies show hard evidence (different label in different source window) of a labeling
   defect that predates any keyword ambiguity, on top of 42 keyword-driven false positives.

## Hypotheses for Next Session
- H8: Rebuild the Aug RM deployment plan directly from the full 4,588-company master pipeline
  (`acer_revenue_model_20260630.csv`) with the Tier 1/2/3 rule re-applied end-to-end, rather than
  continuing to patch individual gaps (NCD gap, 500cr gap) on top of the Session-38 plan.
- H9: Investigate root cause of the October-2026-window vs Q1/Q2-2027-window sector-tagging
  divergence for the 59 specific-sector-conflict companies — is Q1/Q2 2027 pulling from a
  different source classification pass than October 2026?
- H10: Apply the same non-NCD ≥₹500 Cr gap check to a lower threshold (₹100–499 Cr, i.e. the
  Tier 2 population) to see if the capture defect is uniform across all tiers or concentrated at
  the top.

## Data Quality Notes
- Confirmed (not just hypothesized) that the Aug RM plan's build process drops companies that
  meet its own Tier 1 trigger — this is a plan-construction bug, independent of any single
  agency or instrument type.
- Cross-window sector inconsistency (59 companies) is a harder-edged, non-keyword-dependent
  signal of the same sector-labeling problem previously only evidenced via keyword ambiguity.

## Open Questions (Carry Forward)
- Same Q1–Q6 as Session 40 (SEBI license date, BG product capability, BSE/NSE manual upload,
  Infomerics Q2 2027 coverage gap, MCA CIN/NIC enrichment, RM-plan Tier-1 ownership) — all still
  open.
- New: should the Aug RM deployment plan be rebuilt wholesale (H8) before further gap-patching
  sessions, or does ACER ops want incremental fixes layered on the existing Session-38 plan?
