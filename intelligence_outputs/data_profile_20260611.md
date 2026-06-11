# ACER Intelligence — Data Profile Report
**Date:** 2026-06-11 | **Session:** 1 (First Run)

---

## CRITICAL DATA GAPS FOUND

Both data files are **missing State/Region columns** — the INSTRUCTIONS.md task 'Map all states to regions' **cannot be completed from current data**.

**Action Required:** Enrich data files with State field before regional analysis is possible.

---

## FILE 1: infomerics.json.xlsx

- **Rows:** 8,438
- **Unique Companies:** 4,175
- **Date Range:** 2016-12-06 to 2026-02-10
- **Columns Found:** Company Name, Date, Instruments, Size, Current Ratings, Outlook, Rating Rationale PDF, Source URL
- **Expected but Missing:** Sector, State

### Null Counts
- Company Name: 0 nulls
- Date: 4 nulls
- Current Ratings: 14 nulls
- Instruments: 0 nulls
- Size: 21 nulls

### Urgency Distribution (Recency Score)
| Urgency | Count | Meaning |
|---------|-------|--------|
| HIGH | 4,308 | Rating >12 months old — call now |
| MEDIUM | 2,687 | 6–11 months — approaching renewal |
| LOW | 1,439 | <6 months — recently rated |
| UNKNOWN | 4 | No date |

### Rating Action Distribution
| Action | Count |
|--------|-------|
| Reaffirmed | 2,350 |
| INC | 1,993 |
| Assigned | 1,827 |
| Upgraded | 1,064 |
| Other | 904 |
| Downgraded | 206 |
| Withdrawn | 94 |

### Instrument Family Groups
| Family | Count |
|--------|-------|
| Long Term | 4,967 |
| Short Term | 3,096 |
| NCD/Debenture | 185 |
| Other | 89 |
| Term Loan | 41 |
| Commercial Paper | 37 |
| Fund Based | 18 |
| Non-Fund Based | 5 |

### Outlook Distribution
| Outlook | Count |
|---------|-------|
| Nil | 3,597 |
| Stable | 3,258 |
| Negative | 1,047 |
| Stable/- | 229 |
| Negative/- | 117 |
| Positive | 117 |
| Rating Watch with Developing Implications | 45 |
| Positive/- | 13 |
| Rating Watch with Negative Implications | 12 |
| Credit Watch with Negative Implications | 2 |
| Credit Watch with Developing Implications | 1 |

---

## FILE 2: d365_data.xlsx

- **Rows:** 49,945
- **Unique Companies:** 17,622
- **Date Range:** 2025-05-06 to 2026-05-04
- **Columns Found:** Company Name, Date, Agency, Instrument, Grade, Rating, Status, Ammount, Company/Issuer not cooperating
- **Expected but Missing:** State/Region

### Null Counts
- Company Name: 1 nulls
- Date: 1 nulls
- Agency: 1 nulls
- Instrument: 1 nulls
- Rating: 1 nulls

### Agency Distribution
| Agency | Records | Market Share |
|--------|---------|-------------|
| CRISIL | 18,549 | 37.1% |
| CARE | 11,020 | 22.1% |
| ICRA | 6,360 | 12.7% |
| IND-RA | 5,162 | 10.3% |
| ACUITE | 4,635 | 9.3% |
| BRICKWORK | 4,217 | 8.4% |

### Urgency Distribution (Recency Score)
| Urgency | Count | Meaning |
|---------|-------|--------|
| HIGH | 8,926 | Rating >12 months old — call now |
| MEDIUM | 21,576 | 6–11 months — approaching renewal |
| LOW | 19,441 | <6 months — recently rated |
| UNKNOWN | 2 | No date |

### Status Distribution
| Status | Count |
|--------|-------|
| Reaffirmed | 31,391 |
| Downgraded | 5,608 |
| Initial Rating | 4,154 |
| Withdrawn | 4,102 |
| Upgraded | 3,329 |
| Rating Watch | 1,359 |

### Competitor Concentration
| Type | Companies | Opportunity |
|------|-----------|-------------|
| Multi-Agency (2+ raters) | 3,623 | HIGH — already open to competition |
| Single-Agency (1 rater) | 13,999 | MEDIUM — captive but reachable |

---

## OVERLAP ANALYSIS

- Infomerics unique companies: 4,175
- D365 unique companies: 17,622
- Exact name match overlap: 4 companies

**Note:** Low overlap due to name formatting differences (capitalization, abbreviations, Pvt vs Private). Fuzzy matching needed for true deduplication — flagged as P2 task.

Exact matches found: bank of india, bank of maharashtra, cimechel electric private limited, uco bank

---

## DATA ENRICHMENT REQUIREMENTS (Flagged for leadership)

1. **State/Region field** — required for regional territory maps (WHO task)
2. **Sector/Industry field** — infomerics has no sector; required for Sector Attractiveness Matrix
3. **Fuzzy company matching** — for cross-file deduplication
4. **ACER own pipeline data** — to flag which companies ACER is already pursuing

