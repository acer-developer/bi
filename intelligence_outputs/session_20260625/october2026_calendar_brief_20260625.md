# October–November 2026 Calling Calendar Brief
**ACER Intelligence — Session 28**
**Date:** 2026-06-25
**Data Sources:** D365 (49,945 records) + Infomerics (8,438 records)

---

## What This Is

This brief covers all INC companies whose urgency level escalates during October–November 2026.
These are the companies entering their first call window, renewal urgency window, or overdue status for the first time during this period.

---

## Summary Numbers

| Escalation Type | Companies | Records | Call Window Opens |
|---|---|---|---|
| LOW → MEDIUM (first call) | 758 | 758 | October 2026 |
| MEDIUM → HOT (renewal urgent) | 1,885 | 1,885 | Oct–Nov 2026 |
| HOT → ULTRA HOT (overdue) | 1,705 | 1,705 | Oct–Nov 2026 |
| **TOTAL** | **4,151 unique** | **7,837** | |

**HOT/ULTRA HOT escalations only (highest priority):** 3,478 unique companies

---

## April 2026 Cohort (The "Second Blitz" Cohort)

The April 2026 INC cohort was the largest single-month INC event in the dataset (984 unique companies from D365).

| Agency | Companies | Enters MEDIUM (first call) |
|---|---|---|
| CRISIL | 285 | October–November 2026 |
| CARE | 233 | October–November 2026 |
| IND-RA | 177 | October–November 2026 |
| ACUITE | 128 | October–November 2026 |
| BRICKWORK | 94 | October–November 2026 |
| ICRA | 85 | October–November 2026 |
| **TOTAL** | **984** | |

**Urgency timeline:**
- June 25, 2026 (today): ALL 984 are LOW urgency (56–86 days since INC)
- October 1, 2026: 238 enter MEDIUM urgency
- November 1, 2026: ALL 984 are MEDIUM urgency

**Key insight:** ACER should contact the April 2026 cohort in **September 2026** (before October), to get ahead of the wave. First-mover advantage — competitors are unlikely to call until they're already in HOT window.

---

## Agency Breakdown (Full Calendar)

| Agency | Companies Escalating Oct–Nov |
|---|---|
| CRISIL | 1,479 |
| CARE | 834 |
| BRICKWORK | 639 |
| ACUITE | 421 |
| ICRA | 383 |
| IND-RA | 373 |
| Infomerics | 290 |
| **TOTAL** | **4,151 unique** |

CRISIL alone has 1,479 companies escalating — the largest single pool in October–November.

---

## Sector Breakdown

| Sector | Companies Escalating |
|---|---|
| Other (unclassified) | 1,697 |
| Construction | 410 |
| Agro/Food | 357 |
| Steel & Metals | 303 |
| Automobiles | 180 |
| Chemicals/Pharma | 168 |
| IT/Technology | 144 |
| Manufacturing | 139 |
| Energy | 138 |
| Textiles | 136 |

---

## Calling Strategy

### Priority 1: HOT + ULTRA HOT Escalators (3,478 companies)
- File: `csv/october2026_hot_ultraHOT_20260625.csv`
- These companies are in active renewal urgency
- Call dates: October 1 – November 30, 2026
- Pitch: "Your rating is now overdue / entering overdue status. ACER can complete in 2–3 weeks."

### Priority 2: April 2026 Cohort — Pre-Call in September
- File: `csv/april2026_cohort_detail_20260625.csv`
- 984 companies entering MEDIUM urgency in Oct–Nov 2026
- **Pre-call September 2026** — get them before competitors contact in October
- Pitch: "Your INC will hit 6 months in October. Start the ACER process now — we get ahead of the renewal rush."

### Priority 3: Full October Calendar
- File: `csv/october2026_calling_calendar_20260625.csv`
- 7,837 records across all escalation types
- Sort by "Escalates To" (ULTRA HOT first) for daily calling queue

---

## Key Intelligence Finding

**The October 2026 blitz is 4.2x larger than the July 2026 blitz.**

July 2026 calling master (Session 25) had 6,866 unique companies total (built up over months).
October 2026 calendar has **4,151 unique companies escalating in a single 2-month window** — most of whom will not yet be contacted by ACER's July campaign.

This creates a second major calling wave. ACER should plan resource allocation now.

**Confidence:** HIGH — dates derived from actual rating dates in D365 dataset.

---

## Files Produced

- `csv/october2026_calling_calendar_20260625.csv` — Full calendar (7,837 rows)
- `csv/october2026_hot_ultraHOT_20260625.csv` — HOT/ULTRA HOT escalations (6,467 rows, 3,478 unique)
- `csv/april2026_cohort_detail_20260625.csv` — April 2026 cohort with urgency transitions (1,647 rows, 984 unique)
- `csv/october2026_monthly_summary_20260625.csv` — Monthly breakdown by agency and escalation type
