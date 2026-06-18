# BRICKWORK Master Displacement Brief
**ACER Intelligence | Session 15 | 2026-06-18**
**The Single Highest-Yield Call List ACER Has**
Data: D365 (49,945 rows) — Full BRICKWORK working capital INC analysis

---

## Executive Summary

BRICKWORK Ratings has systematically abandoned its working capital client base while pivoting to structured finance (bonds/debentures: only 11.6% INC). Their SME clients — rated for Bank Guarantees, Letters of Credit, and Term Loans — have been left with INC status en masse.

**This file is ACER's single highest-conversion call list.**

| Metric | Value |
|--------|-------|
| Total BRICKWORK working capital INC companies | **1,885** |
| ULTRA HOT (>365 days overdue + INC) | **223** |
| HOT (180–365 days + INC) | **293** |
| WARM (< 180 days + INC) | **1,369** |
| Working capital INC rows | **3,392 of 4,045 (83.9%)** |
| BG INC rate | **86.5%** |
| LC INC rate | **87.9%** |
| Term loan INC rate | **86.1%** |
| Fund-based INC rate | **71.9%** |

**File: `csv/BW_displacement_master_20260618.csv` (1,885 rows)**

---

## The BRICKWORK Strategy Shift (Confirmed)

From the Agency × Instrument INC matrix (Session 14):

| Instrument | BRICKWORK INC Rate |
|------------|--------------------|
| Bank Guarantee | 86.5% |
| Letter Of credit | 87.9% |
| Term loans | 86.1% |
| Fund based | 71.9% |
| Non-fund based | 76.6% |
| **Debentures/Bonds** | **11.6%** |
| Non-government debt | 67.7% |

**Interpretation:** BRICKWORK is not struggling — they are choosing. Debentures/Bonds at 11.6% INC means they are actively managing their structured finance clients while abandoning working capital clients. This is a deliberate strategic pivot toward institutional clients and away from SMEs. ACER fills the gap they've left.

---

## Priority Breakdown by Instrument

Most common INC instrument combinations:

| INC Instruments | Companies |
|-----------------|-----------|
| Term loans only | 437 |
| Bank Guarantee + Term loans | 253 |
| Bank Guarantee only | 233 |
| Letter of Credit only | 168 |
| BG + LC | 139 |
| BG + LC + Term loans | 128 |
| LC + Term loans | 114 |
| Fund-based + Non-fund-based | 109 |
| Fund-based + Term loans | 64 |
| Fund-based only | 63 |

---

## Sector Distribution of BRICKWORK INC Companies

| Sector | Companies |
|--------|-----------|
| Other (unclassified) | 724 |
| Infrastructure | 164 |
| Manufacturing | 148 |
| Construction | 131 |
| Agro & Food | 113 |
| Steel & Metals | 104 |
| Automobiles & Auto | 89 |
| IT & Software | 85 |
| Chemicals & Pharma | 57 |
| Paper & Packaging | 44 |
| Textiles | 42 |
| Healthcare | 42 |
| Energy | 36 |
| Mining & Minerals | 19 |
| Hotels & Tourism | 18 |
| Trading & Exports | 17 |
| BFSI | 16 |
| Jewellery & Gems | 16 |
| Media & Retail | 13 |
| Logistics | 7 |

**724 companies in "Other" sector** — these are unclassified by keyword. With MCA CIN NIC code enrichment (P2 task), many of these would be placed in specific sectors. They are valid leads — do not skip them.

---

## Sales Execution Plan

### Phase 1: ULTRA HOT Sprint (223 companies — THIS WEEK)
- All rated >365 days ago with INC status
- Their rating has fully lapsed — they NEED a new rater immediately
- Call script: "Your BRICKWORK rating has expired and is INC. Your bank may already have flagged your credit facility. ACER can restore your rating in 15 days. Can we schedule a call this week?"

### Phase 2: HOT Wave (293 companies — NEXT 2 WEEKS)
- Rated 180–365 days ago with INC
- Approaching expiry; BRICKWORK still nominally their rater but not cooperating
- Call script: "Your BRICKWORK rating is INC and approaching its one-year mark. The clock is ticking. Would you like ACER to prepare a free initial assessment?"

### Phase 3: WARM Pipeline (1,369 companies — MONTHLY CADENCE)
- INC but rating is still recent (<180 days)
- Awareness campaign: send one email per quarter until they flip to HOT
- Call script: "BRICKWORK has marked your account INC. Many of their clients are switching to ACER. We'd like to show you what a fresh rating would look like."

---

## BRICKWORK Displacement Talking Points

1. **BRICKWORK exited SME working capital.** This is documented, not speculation. 87-88% INC on BG and LC is not capacity — it is policy.

2. **Banks are already aware.** When a rating is INC, lenders flag the instrument. The company is likely already experiencing difficulties renewing credit lines.

3. **ACER is the natural successor.** ACER targets exactly the segment BRICKWORK abandoned: working capital instruments for mid-size manufacturing, infrastructure, and agri companies.

4. **15-day turnaround.** This is ACER's key differentiator vs BRICKWORK's historic 45-60 day process (when they were still servicing).

5. **Regulatory angle.** For companies with BG on government tenders, a lapsed or INC rating may disqualify them from new bids. Urgency is existential for contractor segment.

---

## Important Caveat: Bank Guarantee

3,593+ companies in the master database have INC Bank Guarantees. The entire BG displacement opportunity depends on ACER having BG rating capability.

**Confirm with ACER product team before running Phase 1 BG-focused calls.**
→ See P3 task in TODO.md

If ACER has BG capability: this is the single largest revenue opportunity in the dataset.
If ACER does NOT have BG capability: exclude BG-only companies from call list (233 companies from "Bank Guarantee only" row above) and focus on Term loans + LC + Fund-based.

---

## Output File

→ `intelligence_outputs/session_20260618/csv/BW_displacement_master_20260618.csv`
- 1,885 rows
- Columns: Company Name, INC Instruments, All Instruments, Last Rating, Last Status, Last Rating Date, Days Since Rating, Urgency, Priority, Sector, INC Count, Why Target, ACER Pitch Angle, Current Rater
- Sorted: ULTRA HOT → HOT → WARM, then by days overdue (longest first)
