# October 2026 Clean Callable Calendar — D-Grade Filtered
**Session 29 | Date: 2026-06-25**
**Source: D365 (49,944 records) + Infomerics (8,438 records)**

---

## Summary

The October 2026 calling calendar (built in Session 28, 7,837 rows) has been filtered to remove companies with "D" (actual default) ratings — these are likely NCLT/wind-down situations that cannot be called for rating mandates.

---

## What Was Removed

| Category | Records Removed | Unique Companies Removed |
|----------|----------------|--------------------------|
| D-grade (actual default) | 1,876 | 1,007 |
| Remaining (clean callable) | 5,961 | 3,179 |

**D-grade definition used:**
- Rating = 'D' (exact default)
- Rating starts with 'IVR D' (Infomerics default variant)
- Rating contains 'IVR D ' (with space — Infomerics formatting variant)

**D-grade removed by agency:**
| Agency | Removed Records |
|--------|----------------|
| CRISIL | 526 |
| CARE | 462 |
| BRICKWORK | 284 |
| ICRA | 212 |
| ACUITE | 164 |
| IND-RA | 128 |
| Infomerics | 100 |

---

## Clean October 2026 Callable Calendar

| Metric | Value |
|--------|-------|
| Total clean records | 5,961 |
| Unique companies | 3,179 |
| Escalating to ULTRA HOT | 2,428 records |
| Escalating to HOT | 2,486 records |
| Escalating to MEDIUM | 1,047 records |

**By agency (clean):**
| Agency | Records |
|--------|---------|
| CRISIL | 2,255 |
| CARE | 997 |
| BRICKWORK | 822 |
| ACUITE | 688 |
| ICRA | 463 |
| Infomerics | 447 |
| IND-RA | 289 |

---

## Strategic Implication

1,007 unique companies removed as actual defaults — these are non-callable and should not be approached until resolution of NCLT/stress proceedings. The clean callable list of **3,179 unique companies** is the actionable October 2026 target universe.

**CRISIL has the largest D-grade removal (526 records)** — consistent with CRISIL's large portfolio. After cleaning, CRISIL still leads with 2,255 clean records.

**BRICKWORK: 284 D-grade records removed** (25.7% of its October calendar). This reinforces the Session 27 finding that BW's INC backlog contains genuine defaults mixed with INC-due-to-non-cooperation cases.

---

## Files

- `csv/october2026_clean_callable_20260625.csv` — 5,961 rows, 3,179 unique companies ← **USE THIS FOR CALLING**
- `csv/october2026_removed_defaults_20260625.csv` — 1,876 rows, 1,007 companies (DO NOT CALL — defaults)

**Confidence: HIGH** — D-grade is an unambiguous default indicator across all agencies.
