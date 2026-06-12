# ACER Intelligence — Data Profile Report
**Date:** 2026-06-11 | **Session:** 1 | **Analyst Role:** Head of Strategic Development & BI

---

## FILE 1: infomerics.json.xlsx — Infomerics Ratings Data

### Basic Profile
| Metric | Value |
|--------|-------|
| Total Records | 8,438 |
| Unique Companies | 4,175 |
| Date Range | Dec 2016 → Feb 2026 |
| Columns | 8 |

### Columns Found
| Column | Notes |
|--------|-------|
| Company Name | Primary identifier |
| Date | String format: "July 18, 2025" — parsed successfully |
| Instruments | Instrument type (raw, needs normalization) |
| Size | Facility size in Cr. (21 nulls) |
| Current Ratings | IVR-prefixed, includes action in parentheses |
| Outlook | Stable / Negative / Positive / Nil / Watch |
| Rating Rationale PDF | PDF URL (always present) |
| Source URL | Infomerics website URL |

### Data Quality
| Column | Nulls | Action Required |
|--------|-------|-----------------|
| Company Name | 0 | Clean |
| Date | 4 | Exclude these 4 rows |
| Instruments | 0 | Clean |
| Size | 21 | Non-critical, skip |
| Current Ratings | 14 | Exclude for rating analysis |
| Outlook | 0 | Clean |

### Gap vs. Expected Schema
> **IMPORTANT:** infomerics.json.xlsx does NOT have a State or Sector column.
> Expected columns were: Company Name, Instrument Type, Rating, Rating Date, Outlook, Sector, State
> State and Sector are MISSING from this file. These will need to be derived from company names,
> external lookup, or sourced separately.

### Instrument Family Distribution
| Family | Count | % |
|--------|-------|---|
| Long Term | 4,878 | 57.8% |
| Short Term | 2,695 | 31.9% |
| Long/Short Term | 345 | 4.1% |
| Other | 292 | 3.5% |
| NCD | 189 | 2.2% |
| Commercial Paper | 39 | 0.5% |

### Rating Action Distribution
| Action | Count |
|--------|-------|
| Reaffirmed | 2,566 |
| Assigned | 1,832 |
| Withdrawn | 1,531 |
| Downgraded | 1,380 |
| Upgraded | 893 |
| Other | 236 |

### Outlook Distribution
| Outlook | Count |
|---------|-------|
| Nil | 3,597 |
| Stable | 3,258 |
| Negative | 1,047 |
| Stable/- | 229 |
| Negative/- | 117 |
| Positive | 117 |
| Rating Watch (Developing) | 45 |
| Rating Watch (Negative) | 12 |

### Recency Score Distribution
| Urgency | Count | % |
|---------|-------|---|
| HIGH (>12 months) | 3,752 | 44.5% |
| MEDIUM (6–11 months) | 3,222 | 38.2% |
| LOW (<6 months) | 1,460 | 17.3% |
| UNKNOWN | 4 | ~0% |

**Key insight:** 82.7% of Infomerics-rated instruments are approaching or past renewal — massive opportunity for ACER to re-rate.

---

## FILE 2: d365_data.xlsx — 365-Day Multi-Agency Data

### Basic Profile
| Metric | Value |
|--------|-------|
| Total Records | 49,945 |
| Unique Companies | 17,622 |
| Date Range | May 2025 → May 2026 |
| Columns | 9 |

### Columns Found
| Column | Notes |
|--------|-------|
| Output source file name: W11 | Company/Issuer name (rename to "Company Name") |
| Date | String format: "09-01-2026" (DD-MM-YYYY) — parsed successfully |
| Agency | Rating agency name |
| Instrument | Instrument type |
| Grade | Safety category (High Risk / Adequate Safety / etc.) |
| Rating | Alphanumeric rating (A+, BBB, D, etc.) |
| Status | Reaffirmed / Downgraded / Upgraded / Withdrawn / etc. |
| Ammount | Facility size (1,785 nulls — ~3.6%) |
| Company/Issuer not cooperating | Y/N flag |

### Gap vs. Expected Schema
> **IMPORTANT:** d365_data.xlsx does NOT have a State or Region column.
> Expected columns were: Company Name, Agency Name, Instrument, Rating, Date, Region/State
> State/Region is MISSING. Cannot build regional maps without external enrichment.

### Agency Distribution
| Agency | Records | Market Share |
|--------|---------|--------------|
| CRISIL | 18,549 | 37.1% |
| CARE | 11,020 | 22.1% |
| ICRA | 6,360 | 12.7% |
| IND-RA (India Ratings) | 5,162 | 10.3% |
| ACUITÉ | 4,635 | 9.3% |
| BRICKWORK | 4,217 | 8.4% |
| **Total** | **49,944** | |

### Status Distribution
| Status | Count |
|--------|-------|
| Reaffirmed | 31,391 |
| Downgraded | 5,608 |
| Initial Rating | 4,154 |
| Withdrawn | 4,102 |
| Upgraded | 3,329 |
| Rating Watch | 1,359 |

### Grade Distribution
| Grade | Count |
|-------|-------|
| High Risk | 12,970 |
| Moderate Safety | 9,182 |
| High Safety | 6,764 |
| Adequate Safety | 6,103 |
| Highest Safety | 5,362 |
| Default | 4,688 |
| Inadequate Safety | 3,872 |
| Substantial Risk | 1,002 |

### Recency Score Distribution
| Urgency | Count | % |
|---------|-------|---|
| MEDIUM (6–11 months) | 25,695 | 51.5% |
| LOW (<6 months) | 19,661 | 39.4% |
| HIGH (>12 months) | 4,587 | 9.2% |
| UNKNOWN | 2 | ~0% |

**Note:** d365 covers only the last 12 months, so the HIGH bucket is smaller. MEDIUM = renewal approaching.

---

## CROSS-FILE ANALYSIS

### Company Overlap
| Metric | Value |
|--------|-------|
| Exact name matches (case-insensitive) | 4 |
| Infomerics unique companies | 4,175 |
| d365 unique companies | 17,622 |

**Overlapping companies (exact match):** Bank of Maharashtra, Bank of India, UCO Bank, Cimechel Electric Pvt. Ltd.

> Low overlap is expected: name formatting differs across agencies. True overlap will be higher
> after fuzzy matching (future session task). Infomerics is a separate universe of SME borrowers.

### Competitor Concentration (d365)
| # Agencies | Companies | Opportunity Level |
|------------|-----------|-------------------|
| 1 (single rater) | 13,998 | Medium — captive but approachable |
| 2 agencies | 3,102 | High — already shopping multiple raters |
| 3 agencies | 453 | Very High — experienced multi-rater |
| 4 agencies | 61 | Very High — sophisticated borrower |
| 5 agencies | 6 | Very High — top-tier target |
| 6 agencies | 1 | Very High |

**3,623 companies are rated by 2+ agencies** — these are ACER's prime acquisition targets.

---

## SESSION 1 KEY FINDINGS

1. **State/Sector data is missing** from both files — regional maps cannot be built without enrichment
2. **82.7% of Infomerics instruments are MEDIUM/HIGH urgency** — renewal season is NOW
3. **3,623 companies use multiple raters** — these companies are predisposed to add ACER
4. **CRISIL dominates with 37%** of d365 — incumbent to displace or complement
5. **Infomerics has 1,380 downgrades** — dissatisfied borrowers are hottest leads
6. **5,608 d365 downgrades** — companies that were downgraded by competitor agencies want alternatives

---

*Generated: 2026-06-11 | Next: Build lead list from HIGH-urgency Infomerics + downgraded d365 companies*
