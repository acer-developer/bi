# Instrument Family Reconciliation — 4-Family (Script Matrix) vs 9-Family (Revenue Model)
Date: 2026-07-01 | Session 40
Data Source: `csv/acer_revenue_model_20260630.csv` (10,093-row forward pipeline)
Confidence: HIGH — mapping verified against full record counts (exact match, see below)

---

## Why this exists

Session 39 built two instrument-grouping schemes for two different purposes and used
different granularity for each, without documenting how they relate:
1. `august2026_pitch_script_matrix_20260630.md` — 4-family grouping, built fresh from
   raw d365_data.xlsx, used for agency × instrument competitor-weakness call scripts.
2. `csv/acer_revenue_model_20260630.csv` — 9-family `Instrument_Family` column, used for
   per-instrument fee tiering and revenue estimation across the full 9-month pipeline.

Session 40 was tasked with reconciling the two so future sessions don't conflate a
pitch-tier label with an actual fee tier.

---

## The Mapping (verified exact)

| 4-Family (script matrix) | 9-Family (`Instrument_Family`) | Records | Fee_Avg_Lakhs |
|---|---|---|---|
| Bank Guarantee | Bank Guarantee | 1,894 | 4.00 |
| **Term Loan** | Term Loan | 3,977 | 4.97 |
| **Term Loan** | LT Bank Facilities | 454 | 4.96 |
| **Term Loan** | ST Bank Facilities | 228 | **2.50** |
| **Fund-Based/Other** | Fund-Based Facilities | 803 | **5.00** |
| **Fund-Based/Other** | Letter of Credit | 1,217 | 3.00 |
| **Fund-Based/Other** | Non-Fund-Based | 429 | 3.00 |
| **Fund-Based/Other** | Other/Unknown | 242 | 3.00 |
| NCD/Bond | NCD / Bond | 849 | 20.00 |

**4,659 + 2,691 + 1,894 + 849 = 10,093 — exact match to the full revenue model row count.**
The 4-family scheme is a strict superset grouping of the 9-family scheme; no records are
lost or double-counted in either direction.

---

## Finding: the collapse hides real fee variance in 2 of the 4 buckets

**Bank Guarantee** and **NCD/Bond** collapse cleanly (1:1, no variance lost).

**"Term Loan" (4-family) hides a 2x fee spread:** ST Bank Facilities (228 records, 4.9%
of the bucket) prices at ₹2.5L — half the ₹4.97L rate of Term Loan / LT Bank Facilities
(the other 95.1%). A blended weighted average for this bucket is ₹4.85L — close enough
to Term Loan's own rate that the bucket is **usable for revenue purposes as-is** (5% of
records, error is small in aggregate) but NOT if anyone quotes "Term Loan family = ₹5L/deal"
as a flat per-record rate — that overstates the 228 ST Bank Facilities deals by ~2x.

**"Fund-Based/Other" (4-family) hides a more material fee spread:** Fund-Based Facilities
(803 records, 29.8% of the bucket) prices at ₹5.00L — 67% higher than the ₹3.00L rate for
the other 70.2% (Letter of Credit, Non-Fund-Based, Other/Unknown). A blended average of
₹3.60L understates revenue for those 803 records by ₹1.40L each (₹1,124L / ₹11.24 Cr
aggregate understatement) if a flat "Fund-Based/Other = ₹3L" rate were ever applied instead
of the true per-instrument rate.

---

## Recommendation

**No change needed to existing outputs** — `acer_revenue_model_20260630.csv` and everything
built on top of it (RM deployment plan, revenue density, this session's NCD gap file)
already use the correct 9-family `Instrument_Family` fee tiers, not a blended 4-family rate.
No revenue figures published to date are affected.

**Keep both schemes, but scope them explicitly:**
- **4-family grouping → pitch/call-script use only.** It's the right level of granularity
  for a sales script ("your Fund-Based facility is at risk") — reps don't need to
  distinguish Letter of Credit from Non-Fund-Based on a call.
- **9-family `Instrument_Family` → all revenue/financial modeling.** Never average fees
  across a 4-family bucket for a $ estimate; always use the 9-family tier.

**One follow-up worth doing (not urgent):** if a future session builds an agency ×
instrument INC-rate script matrix again, break out "Fund-Based Facilities" as its own
row rather than folding it into "Fund-Based/Other" — at 803 records (29.8% of that
bucket) with a materially different fee profile, it's large enough to warrant its own
line, unlike ST Bank Facilities (4.9% of its bucket) which is fine to leave folded in.

---

## Files
- This brief: `instrument_family_reconciliation_20260701.md` (no CSV — this is a
  documentation/reconciliation deliverable, not a company lead list; Rule 5 does not apply)
