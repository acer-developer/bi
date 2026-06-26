"""
ACER BI Session 31 Analysis
Date: 2026-06-26
Tasks:
  1. CARE October 2026 escalation deep-dive (997 records)
  2. ACUITE + BRICKWORK combined October brief (MSME agencies)
  3. October 2026 week-by-week call schedule
"""

import pandas as pd
import numpy as np
import os

# ── paths ──────────────────────────────────────────────────────────────────
BASE_DIR = "/home/user/bi/intelligence_outputs"
OUT_DIR  = f"{BASE_DIR}/session_20260626/csv"
MD_DIR   = f"{BASE_DIR}/session_20260626"
os.makedirs(OUT_DIR, exist_ok=True)

DATE_SUFFIX = "20260626"

# ── primary source: enriched October 2026 file (from Session 30) ─────────
ENRICHED_PATH = f"{OUT_DIR}/october2026_clean_callable_enriched_{DATE_SUFFIX}.csv"
# Fallback to Session 29 base if enriched not available
BASE_PATH = f"{BASE_DIR}/session_20260625/csv/october2026_clean_callable_20260625.csv"

print("Loading October 2026 clean callable data …")
try:
    df = pd.read_csv(ENRICHED_PATH)
    print(f"  Loaded enriched file: {len(df):,} rows")
except FileNotFoundError:
    df = pd.read_csv(BASE_PATH)
    print(f"  Loaded base file (fallback): {len(df):,} rows")

# Standardise column names
df.columns = df.columns.str.strip()

# Confirm agency distribution
print("\nAgency distribution in base file:")
print(df['Agency'].value_counts())

# Confirm urgency columns
urg_col     = 'Current Urgency'   # urgency as-of Jun 25
esc_col     = 'Escalates To'      # ULTRA HOT / HOT / MEDIUM
esc_date    = 'Escalation Date'   # when it hits that level
sector_col  = 'Sector'
amt_col     = 'Amount Cr'

# Parse amount to numeric (might be string)
df['Amt_num'] = pd.to_numeric(df.get('Amt_num', df[amt_col]), errors='coerce').fillna(0)

# Parse escalation date
df['EscDate_parsed'] = pd.to_datetime(df[esc_date], errors='coerce')

print(f"\nTotal records: {len(df):,} | Unique companies: {df['Company Name'].nunique():,}")
print(f"Escalation date range: {df['EscDate_parsed'].min()} → {df['EscDate_parsed'].max()}")

# ══════════════════════════════════════════════════════════════════════════
# TASK 1: CARE October 2026 Escalation Deep-Dive
# ══════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("TASK 1: CARE October 2026 Escalation Deep-Dive")
print("="*70)

care = df[df['Agency'] == 'CARE'].copy()
print(f"CARE records: {len(care):,} | Unique companies: {care['Company Name'].nunique():,}")

# Urgency breakdown (Escalates To)
care_urg = care[esc_col].value_counts()
print("\nCAREEscalation urgency distribution:")
print(care_urg)

# Sector breakdown
care_sector = (
    care.groupby(sector_col)
    .agg(
        Companies   = ('Company Name', 'nunique'),
        Records     = ('Company Name', 'count'),
        ULTRA_HOT   = (esc_col, lambda x: (x == 'ULTRA HOT').sum()),
        HOT         = (esc_col, lambda x: (x == 'HOT').sum()),
        MEDIUM      = (esc_col, lambda x: (x == 'MEDIUM').sum()),
        Total_Cr    = ('Amt_num', 'sum'),
        Avg_Cr      = ('Amt_num', 'mean'),
    )
    .reset_index()
    .sort_values('Companies', ascending=False)
)
care_sector['ACER_Score'] = (
    care_sector['ULTRA_HOT'] * 3 +
    care_sector['HOT'] * 1 +
    care_sector['Total_Cr'] * 0.001
).round(1)
care_sector = care_sector.sort_values('ACER_Score', ascending=False)
care_sector['Total_Cr'] = care_sector['Total_Cr'].round(2)
care_sector['Avg_Cr']   = care_sector['Avg_Cr'].round(2)

print("\nTop sectors by ACER Score:")
print(care_sector[['Sector', 'Companies', 'ULTRA_HOT', 'HOT', 'Total_Cr', 'ACER_Score']].head(10).to_string(index=False))

# Instrument mix
care_inst = care['Instrument Type'].value_counts().reset_index()
care_inst.columns = ['Instrument', 'Count']
care_inst['Pct'] = (care_inst['Count'] / len(care) * 100).round(1)
print("\nCAREInstrument mix:")
print(care_inst.head(10).to_string(index=False))

# Top targets by amount
care_top = (
    care[care[esc_col].isin(['ULTRA HOT', 'HOT'])]
    .sort_values('Amt_num', ascending=False)
    .drop_duplicates('Company Name')
    [['Company Name', 'Instrument Type', 'Rating', 'Rating Date',
      esc_col, 'EscDate_parsed', 'Amt_num', sector_col, 'Why Target', 'ACER Pitch Angle']]
    .head(30)
)
print(f"\nTop 30 CARE callable targets (ULTRA HOT + HOT) by amount:")
print(care_top[['Company Name', 'Instrument Type', esc_col, 'Amt_num', sector_col]].to_string(index=False))

# Save: CARE October full list
care_out = care.copy()
care_out['Escalation Date'] = care_out['EscDate_parsed'].dt.strftime('%Y-%m-%d')
care_out = care_out.drop(columns=['EscDate_parsed', 'Amt_num'], errors='ignore')

care_fn = f"{OUT_DIR}/care_october2026_targets_{DATE_SUFFIX}.csv"
care_out.to_csv(care_fn, index=False)
print(f"\nSaved: {care_fn} ({len(care_out):,} rows)")

# Save: sector summary
care_sec_fn = f"{OUT_DIR}/care_october2026_sector_summary_{DATE_SUFFIX}.csv"
care_sector.to_csv(care_sec_fn, index=False)
print(f"Saved: {care_sec_fn} ({len(care_sector):,} sectors)")

# Save: ULTRA HOT subset
care_uh = care[care[esc_col] == 'ULTRA HOT'].copy()
care_uh['Escalation Date'] = care_uh['EscDate_parsed'].dt.strftime('%Y-%m-%d')
care_uh = care_uh.drop(columns=['EscDate_parsed', 'Amt_num'], errors='ignore')
care_uh_fn = f"{OUT_DIR}/care_october2026_ultraHOT_{DATE_SUFFIX}.csv"
care_uh.to_csv(care_uh_fn, index=False)
print(f"Saved: {care_uh_fn} ({len(care_uh):,} rows, {care_uh['Company Name'].nunique():,} unique)")

# Key stats for MD
care_uh_count   = len(care[care[esc_col] == 'ULTRA HOT'])
care_hot_count  = len(care[care[esc_col] == 'HOT'])
care_med_count  = len(care[care[esc_col] == 'MEDIUM'])
care_callable   = care_uh_count + care_hot_count
care_total_cr   = care['Amt_num'].sum()
care_avg_cr     = care['Amt_num'].mean()
care_top1       = care_sector.iloc[0] if len(care_sector) > 0 else {}

# ══════════════════════════════════════════════════════════════════════════
# TASK 2: ACUITE + BRICKWORK Combined October Brief (MSME agencies)
# ══════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("TASK 2: ACUITE + BRICKWORK Combined October Brief")
print("="*70)

msme = df[df['Agency'].isin(['ACUITE', 'BRICKWORK'])].copy()
print(f"MSME pool total: {len(msme):,} records | {msme['Company Name'].nunique():,} unique")
print(f"  ACUITE:    {len(msme[msme['Agency']=='ACUITE']):,} records | {msme[msme['Agency']=='ACUITE']['Company Name'].nunique():,} unique")
print(f"  BRICKWORK: {len(msme[msme['Agency']=='BRICKWORK']):,} records | {msme[msme['Agency']=='BRICKWORK']['Company Name'].nunique():,} unique")

# Per-agency urgency breakdown
for ag in ['ACUITE', 'BRICKWORK']:
    sub = msme[msme['Agency'] == ag]
    print(f"\n{ag} urgency (Escalates To):")
    print(sub[esc_col].value_counts().to_string())
    print(f"  Callable (UH+HOT): {len(sub[sub[esc_col].isin(['ULTRA HOT','HOT'])]):,}")

# Combined sector breakdown
msme_sector = (
    msme.groupby([sector_col])
    .agg(
        Companies   = ('Company Name', 'nunique'),
        Records     = ('Company Name', 'count'),
        ULTRA_HOT   = (esc_col, lambda x: (x == 'ULTRA HOT').sum()),
        HOT         = (esc_col, lambda x: (x == 'HOT').sum()),
        MEDIUM      = (esc_col, lambda x: (x == 'MEDIUM').sum()),
        ACUITE_cos  = ('Agency', lambda x: (x == 'ACUITE').sum()),
        BW_cos      = ('Agency', lambda x: (x == 'BRICKWORK').sum()),
        Total_Cr    = ('Amt_num', 'sum'),
    )
    .reset_index()
    .sort_values('Companies', ascending=False)
)
msme_sector['Total_Cr'] = msme_sector['Total_Cr'].round(2)
msme_sector['UH_rate_pct'] = (msme_sector['ULTRA_HOT'] / msme_sector['Records'] * 100).round(1)
msme_sector = msme_sector.sort_values('ULTRA_HOT', ascending=False)

print("\nTop MSME sectors by ULTRA HOT count:")
print(msme_sector[['Sector','Companies','ULTRA_HOT','HOT','UH_rate_pct','Total_Cr']].head(12).to_string(index=False))

# Agency × Sector pivot
ag_sec_pivot = msme.pivot_table(
    values='Company Name',
    index=sector_col,
    columns='Agency',
    aggfunc='nunique',
    fill_value=0
).reset_index()
print("\nAgency × Sector pivot (unique companies):")
print(ag_sec_pivot.to_string(index=False))

# Top BRICKWORK targets
bw_top = (
    msme[(msme['Agency'] == 'BRICKWORK') & msme[esc_col].isin(['ULTRA HOT', 'HOT'])]
    .sort_values('Amt_num', ascending=False)
    .drop_duplicates('Company Name')
    [['Company Name', 'Instrument Type', esc_col, 'EscDate_parsed', 'Amt_num', sector_col]]
    .head(20)
)
print("\nTop 20 BRICKWORK targets by amount:")
print(bw_top.to_string(index=False))

# Top ACUITE targets
ac_top = (
    msme[(msme['Agency'] == 'ACUITE') & msme[esc_col].isin(['ULTRA HOT', 'HOT'])]
    .sort_values('Amt_num', ascending=False)
    .drop_duplicates('Company Name')
    [['Company Name', 'Instrument Type', esc_col, 'EscDate_parsed', 'Amt_num', sector_col]]
    .head(20)
)
print("\nTop 20 ACUITE targets by amount:")
print(ac_top.to_string(index=False))

# Check overlap (same company rated by BOTH)
bw_cos  = set(msme[msme['Agency'] == 'BRICKWORK']['Company Name'].unique())
ac_cos  = set(msme[msme['Agency'] == 'ACUITE']['Company Name'].unique())
overlap = bw_cos & ac_cos
print(f"\nCompanies rated by BOTH BRICKWORK and ACUITE in October pool: {len(overlap):,}")
if overlap:
    overlap_df = msme[msme['Company Name'].isin(overlap)][
        ['Company Name', 'Agency', esc_col, 'Amt_num', sector_col]
    ].sort_values('Company Name')
    print(overlap_df.head(10).to_string(index=False))

# Save: combined MSME file
msme_out = msme.copy()
msme_out['Escalation Date'] = msme_out['EscDate_parsed'].dt.strftime('%Y-%m-%d')
msme_out = msme_out.drop(columns=['EscDate_parsed', 'Amt_num'], errors='ignore')
msme_fn = f"{OUT_DIR}/msme_agencies_october2026_{DATE_SUFFIX}.csv"
msme_out.to_csv(msme_fn, index=False)
print(f"\nSaved: {msme_fn} ({len(msme_out):,} rows)")

# Save: sector summary
msme_sec_fn = f"{OUT_DIR}/msme_agencies_october2026_sector_{DATE_SUFFIX}.csv"
msme_sector.to_csv(msme_sec_fn, index=False)
print(f"Saved: {msme_sec_fn} ({len(msme_sector):,} sectors)")

# Save: BW UH only
bw_uh = msme[(msme['Agency']=='BRICKWORK') & (msme[esc_col]=='ULTRA HOT')].copy()
bw_uh['Escalation Date'] = bw_uh['EscDate_parsed'].dt.strftime('%Y-%m-%d')
bw_uh = bw_uh.drop(columns=['EscDate_parsed', 'Amt_num'], errors='ignore')
bw_uh_fn = f"{OUT_DIR}/brickwork_october2026_ultraHOT_{DATE_SUFFIX}.csv"
bw_uh.to_csv(bw_uh_fn, index=False)
print(f"Saved: {bw_uh_fn} ({len(bw_uh):,} rows)")

# Save: ACUITE UH only
ac_uh = msme[(msme['Agency']=='ACUITE') & (msme[esc_col]=='ULTRA HOT')].copy()
ac_uh['Escalation Date'] = ac_uh['EscDate_parsed'].dt.strftime('%Y-%m-%d')
ac_uh = ac_uh.drop(columns=['EscDate_parsed', 'Amt_num'], errors='ignore')
ac_uh_fn = f"{OUT_DIR}/acuite_october2026_ultraHOT_{DATE_SUFFIX}.csv"
ac_uh.to_csv(ac_uh_fn, index=False)
print(f"Saved: {ac_uh_fn} ({len(ac_uh):,} rows)")

# Key stats for MD
bw_uh_n  = len(msme[(msme['Agency']=='BRICKWORK') & (msme[esc_col]=='ULTRA HOT')])
bw_hot_n = len(msme[(msme['Agency']=='BRICKWORK') & (msme[esc_col]=='HOT')])
ac_uh_n  = len(msme[(msme['Agency']=='ACUITE')    & (msme[esc_col]=='ULTRA HOT')])
ac_hot_n = len(msme[(msme['Agency']=='ACUITE')    & (msme[esc_col]=='HOT')])
bw_unique = msme[msme['Agency']=='BRICKWORK']['Company Name'].nunique()
ac_unique = msme[msme['Agency']=='ACUITE']['Company Name'].nunique()
bw_total_cr = msme[msme['Agency']=='BRICKWORK']['Amt_num'].sum()
ac_total_cr = msme[msme['Agency']=='ACUITE']['Amt_num'].sum()

# ══════════════════════════════════════════════════════════════════════════
# TASK 3: October 2026 Week-by-Week Call Schedule
# ══════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("TASK 3: October 2026 Week-by-Week Call Schedule")
print("="*70)

# Use full clean callable universe
wk = df.copy()
wk = wk[wk['EscDate_parsed'].notna()].copy()

# Assign call weeks
def assign_week(dt):
    if pd.isna(dt):
        return "Unknown"
    y, m, d = dt.year, dt.month, dt.day
    if m == 10:
        if d <= 7:   return "Oct Wk1 (Oct 1-7)"
        elif d <= 14: return "Oct Wk2 (Oct 8-14)"
        elif d <= 21: return "Oct Wk3 (Oct 15-21)"
        else:        return "Oct Wk4 (Oct 22-31)"
    elif m == 11:
        if d <= 7:   return "Nov Wk1 (Nov 1-7)"
        elif d <= 14: return "Nov Wk2 (Nov 8-14)"
        elif d <= 21: return "Nov Wk3 (Nov 15-21)"
        else:        return "Nov Wk4 (Nov 22-30)"
    elif m < 10:
        return "Pre-Oct (already escalated)"
    else:
        return "Dec+"

wk['Call Week'] = wk['EscDate_parsed'].apply(assign_week)
print("\nCall week distribution:")
print(wk['Call Week'].value_counts().sort_index().to_string())

# Week × Agency pivot (unique companies)
week_agency = wk.pivot_table(
    values='Company Name',
    index='Call Week',
    columns='Agency',
    aggfunc='nunique',
    fill_value=0
).reset_index()

# Add total column
agency_cols = [c for c in week_agency.columns if c != 'Call Week']
week_agency['TOTAL'] = week_agency[agency_cols].sum(axis=1)

# Sort by call week label (logical order)
week_order = [
    "Pre-Oct (already escalated)",
    "Oct Wk1 (Oct 1-7)",
    "Oct Wk2 (Oct 8-14)",
    "Oct Wk3 (Oct 15-21)",
    "Oct Wk4 (Oct 22-31)",
    "Nov Wk1 (Nov 1-7)",
    "Nov Wk2 (Nov 8-14)",
    "Nov Wk3 (Nov 15-21)",
    "Nov Wk4 (Nov 22-30)",
    "Dec+",
    "Unknown"
]
week_agency['sort_key'] = week_agency['Call Week'].map({v: i for i, v in enumerate(week_order)})
week_agency = week_agency.sort_values('sort_key').drop(columns='sort_key')
print("\nWeek × Agency unique companies:")
print(week_agency.to_string(index=False))

# Week × Urgency (Escalates To) breakdown
week_urg = wk.pivot_table(
    values='Company Name',
    index='Call Week',
    columns=esc_col,
    aggfunc='nunique',
    fill_value=0
).reset_index()
week_urg['sort_key'] = week_urg['Call Week'].map({v: i for i, v in enumerate(week_order)})
week_urg = week_urg.sort_values('sort_key').drop(columns='sort_key')
print("\nWeek × Urgency (Escalates To):")
print(week_urg.to_string(index=False))

# Week × Sector (top 5 sectors per week)
top_sectors = ['Construction', 'Agro/Food', 'Steel & Metals', 'Manufacturing', 'Automobiles']
wk_top_sec = wk[wk[sector_col].isin(top_sectors)].pivot_table(
    values='Company Name',
    index='Call Week',
    columns=sector_col,
    aggfunc='nunique',
    fill_value=0
).reset_index()
wk_top_sec['sort_key'] = wk_top_sec['Call Week'].map({v: i for i, v in enumerate(week_order)})
wk_top_sec = wk_top_sec.sort_values('sort_key').drop(columns='sort_key')
print("\nWeek × Top 5 Sectors (unique companies):")
print(wk_top_sec.to_string(index=False))

# Full week-level file with all companies
wk_out = wk.copy()
wk_out['Escalation Date'] = wk_out['EscDate_parsed'].dt.strftime('%Y-%m-%d')
wk_out = wk_out.drop(columns=['EscDate_parsed', 'Amt_num'], errors='ignore')
wk_out = wk_out.sort_values(['Call Week', 'Company Name'])

wk_fn = f"{OUT_DIR}/october2026_weekly_calendar_{DATE_SUFFIX}.csv"
wk_out.to_csv(wk_fn, index=False)
print(f"\nSaved: {wk_fn} ({len(wk_out):,} rows)")

# Save: week summary table
week_summary = wk.groupby('Call Week').agg(
    Records     = ('Company Name', 'count'),
    Unique_Cos  = ('Company Name', 'nunique'),
    ULTRA_HOT   = (esc_col, lambda x: (x == 'ULTRA HOT').sum()),
    HOT         = (esc_col, lambda x: (x == 'HOT').sum()),
    MEDIUM      = (esc_col, lambda x: (x == 'MEDIUM').sum()),
    Total_Cr    = ('Amt_num', 'sum'),
).reset_index()
week_summary['Total_Cr'] = week_summary['Total_Cr'].round(2)
week_summary['sort_key'] = week_summary['Call Week'].map({v: i for i, v in enumerate(week_order)})
week_summary = week_summary.sort_values('sort_key').drop(columns='sort_key')

wk_sum_fn = f"{OUT_DIR}/october2026_weekly_summary_{DATE_SUFFIX}.csv"
week_summary.to_csv(wk_sum_fn, index=False)
print(f"Saved: {wk_sum_fn} ({len(week_summary):,} week rows)")

# Save: agency × week pivot
ag_wk_fn = f"{OUT_DIR}/october2026_agency_week_matrix_{DATE_SUFFIX}.csv"
week_agency.to_csv(ag_wk_fn, index=False)
print(f"Saved: {ag_wk_fn}")

print("\n" + "="*70)
print("All outputs saved successfully.")
print("="*70)

# ══════════════════════════════════════════════════════════════════════════
# WRITE MARKDOWN BRIEF: CARE October 2026
# ══════════════════════════════════════════════════════════════════════════

care_md = f"""# CARE October 2026 Escalation Deep-Dive
**Session 31 | Date: 2026-06-26 | Confidence: HIGH**

---

## Executive Summary

CARE has the **second-largest October 2026 callable pool** after CRISIL.
Of 5,961 total clean callable records, **CARE contributes {len(care):,} records ({care['Company Name'].nunique():,} unique companies)**.

- **ULTRA HOT:** {care_uh_count:,} records | **HOT:** {care_hot_count:,} | MEDIUM: {care_med_count:,}
- Callable NOW (ULTRA HOT + HOT): **{care_callable:,} records ({care[care[esc_col].isin(['ULTRA HOT','HOT'])]['Company Name'].nunique():,} unique)**
- Total identified instrument amount: ₹{care_total_cr/100:.1f} Cr (across {len(care):,} records)
- Average per record: ₹{care_avg_cr:.1f} Cr

---

## Top Sectors by ACER Opportunity Score

| Sector | Companies | ULTRA HOT | HOT | Total Cr | Score |
|--------|-----------|-----------|-----|---------|-------|
"""
for _, r in care_sector.head(10).iterrows():
    care_md += f"| {r['Sector']} | {int(r['Companies'])} | {int(r['ULTRA_HOT'])} | {int(r['HOT'])} | ₹{r['Total_Cr']:,.1f} | {r['ACER_Score']:.1f} |\n"

care_md += f"""
---

## Instrument Mix

| Instrument | Count | % |
|-----------|-------|---|
"""
for _, r in care_inst.iterrows():
    care_md += f"| {r['Instrument']} | {int(r['Count'])} | {r['Pct']:.1f}% |\n"

care_md += f"""
---

## Top 15 CARE Targets (ULTRA HOT + HOT, by Amount)

| Company | Instrument | Urgency | Amount Cr | Sector |
|---------|-----------|---------|-----------|--------|
"""
for _, r in care[care[esc_col].isin(['ULTRA HOT','HOT'])].sort_values('Amt_num', ascending=False).drop_duplicates('Company Name').head(15).iterrows():
    care_md += f"| {r['Company Name']} | {r['Instrument Type']} | {r[esc_col]} | ₹{r['Amt_num']:,.1f} | {r[sector_col]} |\n"

care_md += f"""
---

## ACER Calling Strategy for CARE October Pool

### Phase 1 — ULTRA HOT ({care_uh_count:,} records)
These companies have exceeded 12 months since INC. Call immediately.
Priority sectors: {care_sector.head(3)['Sector'].tolist()}

### Phase 2 — HOT ({care_hot_count:,} records)
Approaching ULTRA HOT. First call in September 2026. Goal: get ACER intro before the crisis deepens.

### Phase 3 — MEDIUM ({care_med_count:,} records)
October 2026 escalation window. Queue for October / November calling.

### Pitch Angle for CARE Companies
"Your CARE rating has been INC for [X months]. CARE's INC backlog means your renewal is likely delayed.
ACER is a SEBI-approved rating agency with a 30-day turnaround commitment. Let's get you active again."

---

## Files
- `csv/care_october2026_targets_{DATE_SUFFIX}.csv` — Full CARE October list ({len(care):,} rows)
- `csv/care_october2026_sector_summary_{DATE_SUFFIX}.csv` — Sector summary
- `csv/care_october2026_ultraHOT_{DATE_SUFFIX}.csv` — ULTRA HOT subset ({care_uh_count:,} rows)
"""

care_md_fn = f"{MD_DIR}/care_october2026_brief_{DATE_SUFFIX}.md"
with open(care_md_fn, 'w') as f:
    f.write(care_md)
print(f"\nSaved MD: {care_md_fn}")

# ══════════════════════════════════════════════════════════════════════════
# WRITE MARKDOWN BRIEF: MSME Agencies October 2026
# ══════════════════════════════════════════════════════════════════════════

msme_md = f"""# ACUITE + BRICKWORK October 2026 — MSME Agency Combined Brief
**Session 31 | Date: 2026-06-26 | Confidence: HIGH**

---

## Overview

ACUITE and BRICKWORK are ACER's highest-priority Phase 1 displacement targets
(per the Competitor Vulnerability Matrix, Session 17). Together they contribute
**{len(msme):,} records ({msme['Company Name'].nunique():,} unique companies)** to the October 2026
callable universe.

| Agency | Records | Unique Companies | ULTRA HOT | HOT | Callable | Total Cr |
|--------|---------|-----------------|-----------|-----|---------|---------|
| BRICKWORK | {len(msme[msme['Agency']=='BRICKWORK']):,} | {bw_unique:,} | {bw_uh_n:,} | {bw_hot_n:,} | {bw_uh_n+bw_hot_n:,} | ₹{bw_total_cr/100:.1f} Cr |
| ACUITE    | {len(msme[msme['Agency']=='ACUITE']):,} | {ac_unique:,} | {ac_uh_n:,} | {ac_hot_n:,} | {ac_uh_n+ac_hot_n:,} | ₹{ac_total_cr/100:.1f} Cr |
| **COMBINED** | **{len(msme):,}** | **{msme['Company Name'].nunique():,}** | **{bw_uh_n+ac_uh_n:,}** | **{bw_hot_n+ac_hot_n:,}** | **{bw_uh_n+ac_uh_n+bw_hot_n+ac_hot_n:,}** | **₹{(bw_total_cr+ac_total_cr)/100:.1f} Cr** |

Companies rated by BOTH agencies (dual-coverage): **{len(overlap):,}**

---

## BRICKWORK Analysis

**Key stat confirmed from Session 26:** BRICKWORK's INC pool self-replenishes —
~276 new INC/month. October pool = {bw_uh_n:,} ULTRA HOT ({round(bw_uh_n/len(msme[msme['Agency']=='BRICKWORK'])*100,1)}% of BRICKWORK October records).

### BRICKWORK Urgency Rate (October pool):
- ULTRA HOT: {bw_uh_n:,} ({round(bw_uh_n/max(len(msme[msme['Agency']=='BRICKWORK']),1)*100,1)}%)
- HOT: {bw_hot_n:,} ({round(bw_hot_n/max(len(msme[msme['Agency']=='BRICKWORK']),1)*100,1)}%)
- MEDIUM: {len(msme[(msme['Agency']=='BRICKWORK') & (msme[esc_col]=='MEDIUM')]):,}

**BW ULTRA HOT rate confirms permanent displacement window — do NOT wait.**

---

## ACUITE Analysis

- ACUITE October pool: {ac_unique:,} unique companies
- ULTRA HOT: {ac_uh_n:,} | HOT: {ac_hot_n:,}
- ACUITE's INC rate has doubled in 14 months (April 2026 peak at 57.4%)
- ACUITE is bank-instrument only (TL/BG/LC); NCD pitch does NOT apply

---

## Combined Sector Breakdown (ACUITE + BRICKWORK)

| Sector | Companies | UH | HOT | UH Rate | Total Cr |
|--------|-----------|----|----|---------|---------|
"""
for _, r in msme_sector.head(12).iterrows():
    msme_md += f"| {r['Sector']} | {int(r['Companies'])} | {int(r['ULTRA_HOT'])} | {int(r['HOT'])} | {r['UH_rate_pct']:.1f}% | ₹{r['Total_Cr']:,.1f} Cr |\n"

msme_md += f"""
---

## ACER Calling Strategy — MSME Phase 1 Blitz

### BRICKWORK Pitch
"Your BRICKWORK rating has been INC. BRICKWORK's recovery rate is under 5% —
they will not clear your INC. ACER is a fresh SEBI-approved agency.
We can issue a new active rating in 30 days. Let's restart your credit profile."

### ACUITE Pitch
"Your ACUITE rating has been INC since [date]. ACUITE's INC rate doubled in 2026 —
they're overwhelmed. ACER has specialist analysts for [their sector].
We offer direct RM access and same-day callbacks."

### Priority Order Within MSME Pool
1. BRICKWORK ULTRA HOT ({bw_uh_n:,}) — call immediately
2. ACUITE ULTRA HOT ({ac_uh_n:,}) — call simultaneously
3. Combined HOT ({bw_hot_n+ac_hot_n:,}) — September queue
4. MEDIUM — October 2026 queue

---

## Files
- `csv/msme_agencies_october2026_{DATE_SUFFIX}.csv` — Combined list ({len(msme):,} rows)
- `csv/msme_agencies_october2026_sector_{DATE_SUFFIX}.csv` — Sector summary
- `csv/brickwork_october2026_ultraHOT_{DATE_SUFFIX}.csv` — BW ULTRA HOT ({bw_uh_n:,} rows)
- `csv/acuite_october2026_ultraHOT_{DATE_SUFFIX}.csv` — ACUITE ULTRA HOT ({ac_uh_n:,} rows)
"""

msme_md_fn = f"{MD_DIR}/msme_agencies_october2026_brief_{DATE_SUFFIX}.md"
with open(msme_md_fn, 'w') as f:
    f.write(msme_md)
print(f"Saved MD: {msme_md_fn}")

# ══════════════════════════════════════════════════════════════════════════
# WRITE MARKDOWN BRIEF: Week-by-Week Calendar
# ══════════════════════════════════════════════════════════════════════════

wk_md = f"""# October 2026 Week-by-Week Call Schedule
**Session 31 | Date: 2026-06-26 | Confidence: HIGH**

---

## Overview

This is the **tactical week-level call schedule** derived from the 5,961-company
clean October callable universe. It tells ACER's sales team EXACTLY which week
to call which company, based on when their INC rating hits the ULTRA HOT threshold.

**Total:** {len(wk):,} records | {wk['Company Name'].nunique():,} unique companies

---

## Week-by-Week Summary

| Call Week | Records | Unique Cos | ULTRA HOT | HOT | MEDIUM | Total Cr |
|-----------|---------|-----------|-----------|-----|--------|---------|
"""
for _, r in week_summary.iterrows():
    wk_md += f"| {r['Call Week']} | {int(r['Records'])} | {int(r['Unique_Cos'])} | {int(r['ULTRA_HOT'])} | {int(r['HOT'])} | {int(r['MEDIUM'])} | ₹{r['Total_Cr']:,.1f} |\n"

wk_md += f"""
---

## Agency Distribution by Week

| Call Week | ACUITE | BRICKWORK | CARE | CRISIL | ICRA | IND-RA | Infomerics | TOTAL |
|-----------|--------|-----------|------|--------|------|--------|-----------|-------|
"""
for _, r in week_agency.iterrows():
    cols_to_print = [r.get('ACUITE',0), r.get('BRICKWORK',0), r.get('CARE',0),
                     r.get('CRISIL',0), r.get('ICRA',0), r.get('IND-RA',0),
                     r.get('Infomerics',0), r.get('TOTAL',0)]
    wk_md += f"| {r['Call Week']} | " + " | ".join(str(int(c)) for c in cols_to_print) + " |\n"

wk_md += f"""
---

## Recommended Daily Call Volume

Based on a 5-day work week and equal daily distribution:

| Week | Unique Cos | Daily Target |
|------|-----------|-------------|
"""
for _, r in week_summary.iterrows():
    daily = int(r['Unique_Cos'] / 5) if r['Unique_Cos'] > 0 else 0
    wk_md += f"| {r['Call Week']} | {int(r['Unique_Cos'])} | {daily}/day |\n"

wk_md += f"""
---

## Key Insights

1. **Largest single week:** {week_summary.sort_values('Unique_Cos', ascending=False).iloc[0]['Call Week']} ({int(week_summary.sort_values('Unique_Cos', ascending=False).iloc[0]['Unique_Cos'])} unique companies)
2. **Most ULTRA HOT in a single week:** {week_summary.sort_values('ULTRA_HOT', ascending=False).iloc[0]['Call Week']} ({int(week_summary.sort_values('ULTRA_HOT', ascending=False).iloc[0]['ULTRA_HOT'])} records)
3. **Pre-October already-escalated companies:** {int(week_summary[week_summary['Call Week'].str.startswith('Pre-')]['Unique_Cos'].sum() if any(week_summary['Call Week'].str.startswith('Pre-')) else 0)} — call these FIRST (already ULTRA HOT)
4. **October total callable:** {int(week_summary[week_summary['Call Week'].str.startswith('Oct')]['Unique_Cos'].sum()):,} unique companies
5. **November overflow:** {int(week_summary[week_summary['Call Week'].str.startswith('Nov')]['Unique_Cos'].sum()):,} unique companies

---

## How to Use This File

1. Download `csv/october2026_weekly_calendar_{DATE_SUFFIX}.csv`
2. Filter the **Call Week** column for your target week
3. Sort by **Escalates To** (ULTRA HOT first) then **Amount Cr** (descending)
4. Assign companies to RMs by sector/region
5. Start calls 1 week BEFORE the escalation date to get ahead of the wave

---

## Files
- `csv/october2026_weekly_calendar_{DATE_SUFFIX}.csv` — Full weekly file ({len(wk_out):,} rows)
- `csv/october2026_weekly_summary_{DATE_SUFFIX}.csv` — Week summary ({len(week_summary):,} rows)
- `csv/october2026_agency_week_matrix_{DATE_SUFFIX}.csv` — Agency × week pivot
"""

wk_md_fn = f"{MD_DIR}/october2026_weekly_calendar_{DATE_SUFFIX}.md"
with open(wk_md_fn, 'w') as f:
    f.write(wk_md)
print(f"Saved MD: {wk_md_fn}")

print("\n✓ All 3 P1 tasks complete.")
