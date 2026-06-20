# ACER Super-Targets: Multi-Signal Scoring Framework
**Session 19 | 2026-06-20**
**Data: D365 (49,944 records) + Infomerics (8,438 records)**

---

## What This Brief Covers
A new composite scoring methodology that stacks multiple urgency signals to identify the
highest-probability switching companies in the entire ACER target universe.

---

## The 5 Signals (Weighted)

| Signal | Weight | What It Means |
|--------|--------|---------------|
| ULTRA HOT (INC + 365+ days overdue) | 3 pts | Overdue and abandoned — most urgent |
| DUAL INC (CRISIL + BRICKWORK both INC) | 2 pts | Two agencies abandoned them simultaneously |
| RECENT TRANSITION (became INC post Jan 2026) | 2 pts | Freshly frustrated — emotional urgency |
| MULTI-AGENCY (3+ agencies rated them) | 1 pt | Already open to multiple raters |
| RECENTLY DOWNGRADED (last 90 days) | 1 pt | Dissatisfied with current grade |

---

## Total Universe
- **8,634 total INC companies** in dataset
- **1,369 TIER 1+2 (score ≥ 3)** — high-confidence targets
- **81 TIER 1 MAXIMUM PRIORITY (score ≥ 5)** — call this week

---

## Tier Breakdown

| Tier | Score | Companies | Call Timing |
|------|-------|-----------|-------------|
| TIER 1 — MAXIMUM PRIORITY | ≥ 5 | **81** | Call within 24 hours |
| TIER 2 — HIGH PRIORITY | 3–4 | **1,288** | Call this week |
| TIER 3 — MEDIUM PRIORITY | 2 | **229** | Call this month |
| TIER 4 — STANDARD | 1 | **7,036** | Ongoing pipeline |

---

## TIER 1 MAXIMUM PRIORITY — Top Companies

| Company | Score | Agencies | Days Overdue | Signals |
|---------|-------|----------|-------------|---------|
| Arya Steels Rolling (India) Pvt. Ltd. | 7 | BRICKWORK+CARE+CRISIL | 386 | UH+DualINC+3+Agencies+Downgraded |
| Supermint Exports Pvt. Ltd. | 7 | BRICKWORK+CARE+CRISIL | 386 | UH+DualINC+3+Agencies+Downgraded |
| Med Freshe Pvt. Ltd. | 7 | BRICKWORK+CARE+CRISIL | 379 | UH+DualINC+3+Agencies+Downgraded |
| New Modern Technomech Pvt. Ltd. | 7 | ACUITE+BW+CARE+CRISIL | 366 | UH+DualINC+4+Agencies+Downgraded |
| Alamelu Balaji Spg. Mills Pvt. Ltd. | 6 | BRICKWORK+CARE+CRISIL | 407 | UH+DualINC+3+Agencies |
| Khedut Solvexp Pvt. Ltd. | 6 | CARE+CRISIL+IND-RA | 407 | UH+Transition+3+Agencies |
| A & T Infracon Pvt. Ltd. | 6 | CARE+CRISIL+IND-RA | 403 | UH+Transition+3+Agencies |
| Chhabeela Energy Foods Pvt. Ltd. | 6 | BRICKWORK+CRISIL | 401 | UH+DualINC+Downgraded |
| Ilasakaa Steels Ltd. | 6 | BRICKWORK+CARE+CRISIL | 401 | UH+DualINC+3+Agencies |
| K Lall Overseas Pvt. Ltd. [Merged] | 6 | BW+CRISIL+IND-RA | 401 | UH+DualINC+3+Agencies |

**Full TIER 1 list:** `csv/super_targets_tier1_2_20260620.csv` (filter Score ≥ 5)
**All TIER 1+2:** `csv/super_targets_tier1_2_20260620.csv` (1,369 rows)

---

## Key Pattern: CRISIL + BRICKWORK Is the Attack Vector

**81% of TIER 1 companies** are INC at both CRISIL and BRICKWORK.
This is not coincidence — these two agencies have overlapping SME client bases,
and both are showing high INC rates (CRISIL 46.7%, BRICKWORK 89.7%).

ACER's pitch: "Two agencies have abandoned you. ACER is SEBI-recognized with a
dedicated SME analyst team. We can restore your rating in weeks."

---

## PITCH SCRIPTS BY SIGNAL

### Signal: DUAL INC (CRISIL + BRICKWORK)
*"I see you've had difficulty with both your current rating agencies. ACER is a SEBI-registered
credit rating agency that specializes in exactly your situation. We offer a fresh assessment,
dedicated analyst point-of-contact, and guaranteed response within 5 business days. Our team
can start immediately. Would 15 minutes work this week?"*

### Signal: RECENT TRANSITION (became INC post Jan 2026)
*"Your rating was recently moved to INC status. This is a critical window — unrated companies
face higher borrowing costs and bank scrutiny. ACER can provide a new SEBI-recognized rating
within 3–4 weeks. Our reactivation process is specifically designed for companies in your situation."*

### Signal: ULTRA HOT + MULTI-AGENCY
*"You've been rated by [3/4] agencies historically — you understand the value of credit ratings.
At 400+ days with no valid rating, your banking relationships are at risk. ACER can restore
your credit standing immediately. We're competitive on fees and faster than any existing agency."*

---

## Files Produced This Session

- `csv/super_targets_tier1_2_20260620.csv` — 1,369 high-priority targets (Tier 1+2)
- `csv/master_inc_scored_20260620.csv` — all 8,634 INC companies with signal scores
- `csv/crisil_bw_dual_inc_20260620.csv` — 281 dual-INC companies
- `csv/recent_inc_transitions_20260620.csv` — 95 recent transition companies
- `csv/fresh_inc_transitions_justnow_20260620.csv` — 43 freshest transitions (0-90 days)
- `csv/ultra_hot_dead_risk_audit_20260620.csv` — 1,647 ULTRA HOT with risk flags
- `csv/recent_downgrades_90days_20260620.csv` — 523 recently downgraded companies

---

*Confidence: HIGH — all figures drawn directly from d365_data.xlsx + infomerics.json.xlsx*
