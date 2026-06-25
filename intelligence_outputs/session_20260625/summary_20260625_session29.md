# ACER Intelligence Session 29 Summary
**Date: 2026-06-25 | Session #29**
**Source data: D365 (49,944 records) + Infomerics (8,438 records)**

---

## Session 29 Completed Tasks

### 1. October 2026 Clean Callable Calendar (P1 — COMPLETE)
- **D-grade filter applied** to October 2026 calling calendar (7,837 rows)
- 1,876 records (1,007 unique companies) removed as actual defaults
- **Clean callable list: 5,961 records, 3,179 unique companies**
- Escalations: 2,428 ULTRA HOT | 2,486 HOT | 1,047 MEDIUM
- CRISIL leads clean pool (2,255), followed by CARE (997), BW (822)
- Files: `csv/october2026_clean_callable_20260625.csv` + `october2026_removed_defaults_20260625.csv`

### 2. Brickwork October 2026 Escalation Deep-Dive (P1 — COMPLETE)
- BW full October calendar: 639 unique companies, 1,106 records
- **D-grade removed: 168 companies (26.3%)** — above system average
- **Clean BW callable: 471 unique companies, 822 records**
- 366 ULTRA HOT + 379 HOT escalations = 90.6% in highest urgency buckets
- Top instrument: Term Loans (32%), BG (27%), LC (19%) — all bank instruments (no SEBI license needed)
- Top identified target: Akbar Travels India ₹812.5 Cr (Hotels/Tourism)
- Files: `csv/brickwork_october2026_targets_20260625.csv` + `brickwork_oct2026_sector_summary_20260625.csv`

### 3. ACUITE NCD INC Standalone Profile (P1 — COMPLETE)
- **FINDING: ACUITE has ZERO NCD INC companies** (0.0% INC rate on NCD)
- ACUITE's entire NCD book = 61 records, 19 companies — none are INC
- ACUITE is a bank-instrument agency (TL/BG/LC dominant) — not a capital markets player
- **NCD displacement priority (updated):** IND-RA 663 → CARE 454 → ICRA 282 → BW 82 → ACUITE: N/A
- Cross-agency NCD INC comparison saved for reference
- Files: `csv/acuite_ncd_inc_profile_20260625.csv` (0 rows) + `csv/ncd_inc_all_agencies_comparison_20260625.csv`

---

## Key Findings

1. **October 2026 clean callable universe = 3,179 unique companies (down from 4,151 raw).** The 24.3% D-grade removal is significant — nearly 1 in 4 October escalations is an actual default not worth calling. Use the clean file only.

2. **Brickwork's October pool has the highest D-grade contamination (26.3%).** This reinforces that BW's INC backlog contains a genuine default component — the "permanent INC backlog" (Session 27) includes both non-cooperating and truly distressed companies. BW sales calls should be screened carefully.

3. **ACUITE is absent from the NCD market (confirmed data).** Zero NCD INC companies. All prior ACUITE analysis (Session 22/23) for bank instruments remains fully valid. ACER should not spend resources targeting ACUITE clients for NCD mandates — they don't have NCD ratings.

4. **NCD displacement ranking is definitive: IND-RA > CARE > ICRA > BW, with ACUITE and CRISIL essentially absent.** Total NCD INC callable pipeline: IND-RA 109 + CARE 166 + ICRA 42 + BW 19 = **336 companies callable now** for NCD mandates (SEBI CRA license required).

5. **BW's October top target: Akbar Travels India (₹812.5 Cr)** — Hotels/Tourism company with Fund-Based + BG INC at BW since Oct 2025. Will hit ULTRA HOT exactly at October 7 window. Senior RM should be assigned by September 15.

---

## Hypotheses for Session 30

- H1: IND-RA NCD deep-dive — 663 INC companies, 109 callable now (Session 21 covered IND-RA × CRISIL dual-INC for NCD but not IND-RA standalone NCD profile). Build standalone IND-RA NCD INC profile comparable to CARE NCD (Session 27).
- H2: CRISIL October escalation deep-dive — CRISIL has 2,255 clean October records (largest pool). Map to CRISIL's known sector concentrations.
- H3: October 2026 sector-wise breakdown — which sectors have the most escalations in Oct? Useful for sector-specific outreach campaigns.
- H4: Clean callable October list — build HOT+ULTRA HOT only subset (remove MEDIUM for immediate action list)

---

## Data Quality Notes

- D-grade filter confirmed working: Rating == 'D' (exact), starts with 'IVR D', or contains 'IVR D ' covers all observed patterns.
- ACUITE NCD finding is robust — 61 total NCD records with 0 INC confirms this structurally, not as a data gap.
- BW October D-grade rate (26.3%) vs system average (24.3%) — small but consistent with BW's known distress profile.
- Infomerics NCD: confirmed zero in D365 (Infomerics uses "Long Term Bank Facility" category, not NCD instrument naming).

---

## Open Questions

- Q1: ACER SEBI CRA license — confirmed for NCD instruments? Blocks 336 NCD callable companies.
- Q2: Bank Guarantee capability — 3,593 BG INC companies awaiting ACER product confirmation.
- Q3: MCA CIN upload — geo classification still ~97% unknown.
- Q4: BSE SME fetch — still blocked (403). Manual download needed.

