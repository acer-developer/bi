# Sector Revenue Density Brief
Date: 2026-06-30 | Session 39

Source: csv/acer_revenue_model_20260630.csv (10,093 records, 4,588 unique companies — full 9-month pipeline: Oct 2026 + Q1 2027 + Q2 2027)

## What "Revenue Density Score" Measures
Weighted composite (0-100 scale) of three components per sector:
- **Revenue per company** (50% weight) — average fee yield per unique company
- **Deal volume** (30% weight) — number of unique companies (scale matters for RM staffing)
- **NCD rate** (20% weight) — % of records that are NCD/Bond (highest-fee instrument, ₹20L/deal)

## Data Quality Fix Applied
Raw data had duplicate sector labels: "Energy" (Oct/Q1 windows) vs "Energy/Power" (Q2 window), and "Jewellery" vs "Jewellery/Gems". Both pairs were merged before scoring — this corrects a gap noted in Session 38 where Q2 Energy appeared to have 0 records.

## Top Findings

1. **"Other" unclassified bucket ranks #2 by density (61.4) and is the largest single revenue pool** — 1,806 companies, ₹220.3 Cr revenue, ₹103,562 Cr identified amount. This is the single biggest argument for promoting MCA CIN/NIC enrichment to unblock sector classification (already flagged P1 in TODO).

2. **Energy (merged) is the highest-reliability, highest-density real sector** — 170 companies, ₹209.9 Cr amount/company (3rd highest), 10.2% NCD rate, density score 39.1. This confirms Session 38's H1 hypothesis: Energy yields far more per company than high-volume sectors like Construction (₹174.5 Cr/company) or Agro & Food (₹39.8 Cr/company).

3. **Construction has 2.9x Energy's company count (489 vs 170) but lower density (35.5 vs 39.1)** — Construction is the volume play, Energy is the yield play. Both deserve dedicated Senior RM tracks but for different reasons.

4. **Education, Mining & Minerals, BFSI/NBFC, Infrastructure, Media/Retail, and Mining all carry LOW or MEDIUM reliability flags (n<15 or n<50 companies)** — their density scores are statistically noisy and should not drive resourcing decisions alone. Education's #1 rank (68.0) is driven by just 5 companies — do not over-index on this.

5. **Jewellery (merged) jumped to a real 53-company sector at 22.0% NCD rate** — second-highest NCD rate of any sector after Education — worth a dedicated mini-brief if capacity allows (P2 candidate).

## Recommendation
Resource allocation priority by density (excluding LOW-reliability sectors): **Other (pending MCA unlock) > Energy > Chemicals & Pharma > Construction > IT/Technology > Textiles/Manufacturing**, with Construction and Agro & Food kept as high-volume telesales tracks regardless of density rank.

Output file: `csv/sector_revenue_density_20260630.csv` (23 sectors, ranked)
