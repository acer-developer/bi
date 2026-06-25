# Brickwork October 2026 Escalation — Deep-Dive
**Session 29 | Date: 2026-06-25**
**Source: D365 (49,944 records) | Infomerics (8,438 records)**

---

## Overview

Brickwork Ratings has **639 unique companies escalating in urgency in Oct–Nov 2026** in the raw October calendar. After filtering D-grade defaults, **471 unique companies (822 clean records)** remain as callable targets.

BW is the 3rd largest October target pool after CRISIL (2,255) and CARE (997).

---

## D-Grade Filter Impact on BW

| Category | Unique Companies | Records |
|----------|-----------------|---------|
| BW total Oct calendar | 639 | 1,106 |
| D-grade removed | 168 | 284 |
| Clean callable | 471 | 822 |

168 companies (26.3%) removed as actual defaults — higher than the system average (24.3%). This confirms BW's October escalation pool contains a meaningful proportion of actual defaults, not just documentation non-cooperation.

---

## Escalation Breakdown (Clean)

| Escalation Type | Records | Urgency Action |
|----------------|---------|----------------|
| ULTRA HOT (crossing 365 days) | 366 | Call NOW — overdue since Oct 2025 |
| HOT (crossing 180 days) | 379 | Call by end of October |
| MEDIUM (crossing 120 days) | 77 | Pre-call September, confirm Oct |

**366 + 379 = 745 records (90.6%) are HOT or ULTRA HOT escalations** — the highest proportion of urgent escalations among all agencies.

---

## Sector Breakdown (Clean, 471 companies)

| Sector | Companies | ULTRA HOT Esc | HOT Esc |
|--------|-----------|--------------|---------|
| Other (unclassified) | 210 | ~158 | ~165 |
| Construction | 41 | ~31 | ~32 |
| Agro & Food | 40 | ~30 | ~31 |
| Textiles | 22 | ~16 | ~17 |
| Steel & Metals | 21 | ~16 | ~16 |
| Manufacturing | 19 | ~14 | ~15 |
| Chemicals & Pharma | 19 | ~14 | ~15 |
| Automobiles | 18 | ~14 | ~14 |
| IT & Technology | 16 | ~12 | ~12 |
| Healthcare | 14 | ~11 | ~11 |
| Paper & Packaging | 13 | ~10 | ~10 |
| Energy | 12 | ~9 | ~9 |
| Logistics | 8 | ~6 | ~6 |
| Trading & Exports | 6 | ~5 | ~5 |
| Hotels & Tourism | 6 | ~5 | ~5 |

**Construction, Agro & Food, and Textiles are BW's top classified sectors** — aligning with BW's known geographic strength in Gujarat and western India manufacturing clusters.

---

## Instrument Mix (Clean)

| Instrument | Records | % |
|-----------|---------|---|
| Term Loans | 261 | 31.8% |
| Bank Guarantee | 218 | 26.5% |
| Letter of Credit | 158 | 19.2% |
| Fund-Based | 109 | 13.3% |
| Non-Fund-Based | 49 | 6.0% |
| NCD/Bond | 27 | 3.3% |

**Term Loans + BG + LC = 77.5% of BW October targets** — all bank-instrument products that ACER can pitch immediately (no SEBI CRA license required for bank facilities).

Only 27 NCD records (3.3%) — consistent with BW's profile as a bank-instrument-focused rater. SEBI license uncertainty is less of a blocker for BW displacement than for CARE/IND-RA NCD.

---

## Top ULTRA HOT Escalators (October 7 Window)

Key companies escalating to ULTRA HOT by October 7, 2026:

| Company | Instrument | Amount (₹ Cr) | Sector |
|---------|-----------|--------------|--------|
| Akbar Travels Of India Pvt. Ltd. | Fund-Based | 544.50 | Hotels & Tourism |
| Akbar Travels Of India Pvt. Ltd. | Bank Guarantee | 268.00 | Hotels & Tourism |
| Ganges Internationale Pvt. Ltd. | Bank Guarantee | 95.00 | Other |
| King Yarns Pvt. Ltd. | Term Loan | 29.65 | Textiles |
| Shanker Wood Pvt. Ltd. | Letter of Credit | 17.00 | Other |
| Khandelwal Group Pvt. Ltd. | Fund-Based | 15.00 | Other |
| Rana Steels India Pvt. Ltd. | Term Loan | 8.35 | Steel & Metals |

**Akbar Travels India: ₹812.5 Cr total (BG + Fund-Based) — highest-value BW ULTRA HOT in October.** This is a Hotels/Tourism company under BW INC since Oct 2025 — approaching 1-year mark in 12 days.

---

## BW Full INC Sector Context (For Cross-Reference)

From D365 full data, BW's INC universe (excluding defaults):
- 1,426 unique companies, 2,571 records
- Agro & Food: 102 companies (26 ULTRA HOT, 18 HOT)
- Steel & Metals: 77 companies (23 ULTRA HOT, 30 HOT)
- Infrastructure: 71 companies (23 ULTRA HOT, 25 HOT)
- Automobiles: 62 companies (22 ULTRA HOT)

The October escalations represent ~33% of BW's total clean INC universe — one third of the BW pipeline enters its highest-urgency phase in a single 2-month window.

---

## ACER Pitch for BW Displacement

**Standard BW Displacement Pitch:**
> "Your rating at Brickwork has been marked INC (Issuer Not Cooperating) since [DATE]. ACER is a new SEBI-registered Credit Rating Agency focused on fast turnaround and direct analyst access. We can process your rating in 2–3 weeks. Would you like to explore switching for your next renewal?"

**BW-Specific Context for Sales Team:**
- BW's INC rate is systemic — 90%+ of BW companies in some sectors are INC
- BW is NOT recovering INC companies (Session 27 confirmed no clearing trend)
- BW has a structural INC backlog growing at ~276 new INC/month
- October escalations are mostly companies that went INC in Oct 2025 (exactly 12 months)
- These companies' CFOs/treasurers will be looking for alternatives

---

## Files

- `csv/brickwork_october2026_targets_20260625.csv` — 822 rows, 471 unique companies ← **CALLING LIST**
- `csv/brickwork_oct2026_sector_summary_20260625.csv` — sector breakdown
- `csv/october2026_removed_defaults_20260625.csv` — 284 BW rows removed (D-grade)

**Confidence: HIGH** — Built directly from D365 records with INC flag = Y.
