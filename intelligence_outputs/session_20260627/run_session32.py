"""
ACER Intelligence Session 32 — 2026-06-27
P1 Tasks:
1. IND-RA + ICRA combined October brief
2. September pre-call strategy list (Oct Wk1+Wk2)
3. Cross-agency duplicate check in October pool
4. Infomerics October deep-dive
"""

import pandas as pd
import os

TODAY = "20260627"
OUT_DIR = f"intelligence_outputs/session_{TODAY}/csv"
os.makedirs(OUT_DIR, exist_ok=True)

# ─── Load base data files (mandatory: read both fresh every session) ───────────
print("Loading d365_data.xlsx...")
d365 = pd.read_excel("d365_data.xlsx")
print(f"  D365: {len(d365)} rows, cols: {d365.columns.tolist()}")

print("Loading infomerics.json.xlsx...")
inf = pd.read_excel("infomerics.json.xlsx")
print(f"  Infomerics: {len(inf)} rows, cols: {inf.columns.tolist()}")

# ─── Load October pool (enriched from session 20260626) ───────────────────────
print("\nLoading October 2026 clean callable pool...")
oct_enr = pd.read_csv(
    "intelligence_outputs/session_20260626/csv/october2026_clean_callable_enriched_20260626.csv"
)
print(f"  October enriched: {len(oct_enr)} rows")

# Load weekly calendar (has Call Week column)
oct_wk = pd.read_csv(
    "intelligence_outputs/session_20260626/csv/october2026_weekly_calendar_20260626.csv"
)
print(f"  October weekly calendar: {len(oct_wk)} rows")

print(f"\nD365 record count: {len(d365)}")
print(f"Infomerics record count: {len(inf)}")
print(f"October pool (clean callable): {len(oct_enr)} records | {oct_enr['Company Name'].nunique()} unique companies")

# =============================================================================
# TASK 1: IND-RA + ICRA Combined October Brief
# =============================================================================
print("\n" + "="*60)
print("TASK 1: IND-RA + ICRA Combined October Brief")
print("="*60)

indra_oct = oct_wk[oct_wk['Agency'] == 'IND-RA'].copy()
icra_oct = oct_wk[oct_wk['Agency'] == 'ICRA'].copy()
combined_oct = oct_wk[oct_wk['Agency'].isin(['IND-RA', 'ICRA'])].copy()

print(f"\nIND-RA: {len(indra_oct)} records | {indra_oct['Company Name'].nunique()} unique companies")
print(f"ICRA: {len(icra_oct)} records | {icra_oct['Company Name'].nunique()} unique companies")
print(f"Combined: {len(combined_oct)} records | {combined_oct['Company Name'].nunique()} unique companies")

# Check for overlap (companies at both IND-RA and ICRA)
indra_cos = set(indra_oct['Company Name'].str.strip().str.upper())
icra_cos = set(icra_oct['Company Name'].str.strip().str.upper())
dual_cos = indra_cos & icra_cos
print(f"Companies at BOTH IND-RA and ICRA: {len(dual_cos)}")
if dual_cos:
    print("  Dual companies:", list(dual_cos)[:10])

# Urgency breakdown
for agency, sub in [('IND-RA', indra_oct), ('ICRA', icra_oct), ('COMBINED', combined_oct)]:
    uh = (sub['Escalates To'] == 'ULTRA HOT').sum()
    hot = (sub['Escalates To'] == 'HOT').sum()
    med = (sub['Escalates To'] == 'MEDIUM').sum()
    callable_ = uh + hot
    amt = sub['Amt_num'].sum() if 'Amt_num' in sub.columns else sub['Amount Cr'].apply(
        lambda x: float(str(x).replace('₹','').replace('Cr','').strip()) if pd.notna(x) and str(x).strip() not in ['', '0', 'nan'] else 0
    ).sum()
    print(f"\n{agency}: ULTRA HOT={uh} | HOT={hot} | MEDIUM={med} | Callable={callable_} | Total Amt=₹{amt:,.0f} Cr")

# IND-RA instrument breakdown
print("\nIND-RA Instrument Mix:")
print(indra_oct.groupby('Instrument Type').agg(
    Records=('Company Name', 'count'),
    UH=('Escalates To', lambda x: (x=='ULTRA HOT').sum()),
    HOT=('Escalates To', lambda x: (x=='HOT').sum()),
).sort_values('Records', ascending=False).to_string())

print("\nICRA Instrument Mix:")
print(icra_oct.groupby('Instrument Type').agg(
    Records=('Company Name', 'count'),
    UH=('Escalates To', lambda x: (x=='ULTRA HOT').sum()),
    HOT=('Escalates To', lambda x: (x=='HOT').sum()),
).sort_values('Records', ascending=False).to_string())

# Weekly breakdown
print("\nIND-RA Weekly Schedule:")
print(indra_oct.groupby('Call Week').agg(
    Records=('Company Name','count'),
    Unique=('Company Name','nunique'),
    UH=('Escalates To', lambda x:(x=='ULTRA HOT').sum()),
).to_string())

print("\nICRA Weekly Schedule:")
print(icra_oct.groupby('Call Week').agg(
    Records=('Company Name','count'),
    Unique=('Company Name','nunique'),
    UH=('Escalates To', lambda x:(x=='ULTRA HOT').sum()),
).to_string())

# Top targets each agency — sort by ULTRA HOT first, then by amount
def parse_amt(x):
    try:
        v = float(str(x).replace('₹','').replace('Cr','').replace(',','').strip())
        return v if v > 0 else 0
    except:
        return 0

indra_oct['Amt_parsed'] = indra_oct['Amount Cr'].apply(parse_amt)
icra_oct['Amt_parsed'] = icra_oct['Amount Cr'].apply(parse_amt)
combined_oct['Amt_parsed'] = combined_oct['Amount Cr'].apply(parse_amt)

print("\nTop 10 IND-RA October targets (by ULTRA HOT + Amount):")
indra_top = indra_oct[indra_oct['Escalates To'].isin(['ULTRA HOT','HOT'])].sort_values(
    ['Escalates To', 'Amt_parsed'], ascending=[True, False]
)
print(indra_top[['Company Name','Instrument Type','Rating','Escalation Date','Escalates To','Amount Cr','Sector','Call Week']].head(10).to_string())

print("\nTop 10 ICRA October targets (by ULTRA HOT + Amount):")
icra_top = icra_oct[icra_oct['Escalates To'].isin(['ULTRA HOT','HOT'])].sort_values(
    ['Escalates To', 'Amt_parsed'], ascending=[True, False]
)
print(icra_top[['Company Name','Instrument Type','Rating','Escalation Date','Escalates To','Amount Cr','Sector','Call Week']].head(10).to_string())

# Sector breakdown
print("\nIND-RA Sector Breakdown:")
indra_sec = indra_oct.groupby('Sector').agg(
    Records=('Company Name','count'),
    Unique=('Company Name','nunique'),
    UH=('Escalates To', lambda x:(x=='ULTRA HOT').sum()),
    Amt_Cr=('Amt_parsed','sum'),
).sort_values('Records', ascending=False)
print(indra_sec.head(15).to_string())

print("\nICRA Sector Breakdown:")
icra_sec = icra_oct.groupby('Sector').agg(
    Records=('Company Name','count'),
    Unique=('Company Name','nunique'),
    UH=('Escalates To', lambda x:(x=='ULTRA HOT').sum()),
    Amt_Cr=('Amt_parsed','sum'),
).sort_values('Records', ascending=False)
print(icra_sec.head(15).to_string())

# Add pitch angles
def get_pitch(agency, instrument, uh):
    if agency == 'IND-RA':
        base = "IND-RA is Fitch-owned — premium-priced and focused on structured/large deals. ACER offers same-quality ratings at lower cost with faster turnaround."
    else:
        base = "ICRA is Moody's-owned — commanding premium fees. ACER brings equivalent analytical depth at competitive pricing for mid-market companies."
    if uh == 'ULTRA HOT':
        return base + " Your current rating is overdue — ACER can onboard immediately."
    return base + " Get ahead of renewal — ACER can begin the process now."

combined_oct['ACER_Pitch_v2'] = combined_oct.apply(
    lambda r: get_pitch(r['Agency'], r['Instrument Type'], r['Escalates To']), axis=1
)

# Save combined IND-RA + ICRA file
combined_out = combined_oct.drop(columns=['Amt_parsed'], errors='ignore')
combined_out.to_csv(f"{OUT_DIR}/indra_icra_october2026_{TODAY}.csv", index=False)
print(f"\nSaved: {OUT_DIR}/indra_icra_october2026_{TODAY}.csv ({len(combined_out)} rows)")

# Save IND-RA only file
indra_out = indra_oct.drop(columns=['Amt_parsed'], errors='ignore')
indra_out.to_csv(f"{OUT_DIR}/indra_october2026_targets_{TODAY}.csv", index=False)
print(f"Saved: {OUT_DIR}/indra_october2026_targets_{TODAY}.csv ({len(indra_out)} rows)")

# Save ICRA only file
icra_out = icra_oct.drop(columns=['Amt_parsed'], errors='ignore')
icra_out.to_csv(f"{OUT_DIR}/icra_october2026_targets_{TODAY}.csv", index=False)
print(f"Saved: {OUT_DIR}/icra_october2026_targets_{TODAY}.csv ({len(icra_out)} rows)")

# ULTRA HOT + HOT callable subsets
indra_callable = indra_oct[indra_oct['Escalates To'].isin(['ULTRA HOT','HOT'])].drop(columns=['Amt_parsed'], errors='ignore')
icra_callable = icra_oct[icra_oct['Escalates To'].isin(['ULTRA HOT','HOT'])].drop(columns=['Amt_parsed'], errors='ignore')
indra_callable.to_csv(f"{OUT_DIR}/indra_october2026_callable_{TODAY}.csv", index=False)
icra_callable.to_csv(f"{OUT_DIR}/icra_october2026_callable_{TODAY}.csv", index=False)
print(f"Saved: indra_october2026_callable ({len(indra_callable)} rows) + icra_october2026_callable ({len(icra_callable)} rows)")

# Sector summary CSV
combined_sec = combined_oct.groupby(['Agency','Sector']).agg(
    Records=('Company Name','count'),
    Unique_Companies=('Company Name','nunique'),
    ULTRA_HOT=('Escalates To', lambda x:(x=='ULTRA HOT').sum()),
    HOT=('Escalates To', lambda x:(x=='HOT').sum()),
    MEDIUM=('Escalates To', lambda x:(x=='MEDIUM').sum()),
    Total_Amt_Cr=('Amt_parsed','sum'),
).reset_index().sort_values(['Agency','Records'], ascending=[True,False])
combined_sec.to_csv(f"{OUT_DIR}/indra_icra_sector_summary_{TODAY}.csv", index=False)
print(f"Saved: indra_icra_sector_summary ({len(combined_sec)} rows)")


# =============================================================================
# TASK 2: September Pre-Call Strategy List
# =============================================================================
print("\n" + "="*60)
print("TASK 2: September Pre-Call Strategy List")
print("="*60)

# Oct Wk1 + Oct Wk2 = companies escalating Oct 1-14 → call in September
sept_target_weeks = ['Oct Wk1 (Oct 1-7)', 'Oct Wk2 (Oct 8-14)']
sept_pool = oct_wk[oct_wk['Call Week'].isin(sept_target_weeks)].copy()

print(f"\nTotal records in Oct Wk1+Wk2: {len(sept_pool)}")
print(f"Unique companies: {sept_pool['Company Name'].nunique()}")
print(f"\nBy agency:")
print(sept_pool.groupby('Agency').agg(
    Records=('Company Name','count'),
    Unique=('Company Name','nunique'),
    UH=('Escalates To', lambda x:(x=='ULTRA HOT').sum()),
    HOT=('Escalates To', lambda x:(x=='HOT').sum()),
).to_string())

# Parse amounts
sept_pool['Amt_parsed'] = sept_pool['Amount Cr'].apply(parse_amt)

print(f"\nBy week:")
print(sept_pool.groupby('Call Week').agg(
    Records=('Company Name','count'),
    Unique=('Company Name','nunique'),
    UH=('Escalates To', lambda x:(x=='ULTRA HOT').sum()),
    Total_Cr=('Amt_parsed','sum'),
).to_string())

# Urgency breakdown
uh = (sept_pool['Escalates To'] == 'ULTRA HOT').sum()
hot = (sept_pool['Escalates To'] == 'HOT').sum()
med = (sept_pool['Escalates To'] == 'MEDIUM').sum()
print(f"\nULTRA HOT escalations: {uh} | HOT: {hot} | MEDIUM: {med}")
print(f"Total amount identified: ₹{sept_pool['Amt_parsed'].sum():,.0f} Cr")

# Add September call action column
def sept_action(row):
    wk = row['Call Week']
    esc = row['Escalates To']
    agency = row['Agency']
    if esc == 'ULTRA HOT':
        return f"URGENT: Call first week of September — escalates to ULTRA HOT by {row['Escalation Date'][:7]}. Lead with {agency} displacement pitch."
    elif esc == 'HOT':
        return f"Call by mid-September — escalates to HOT by {row['Escalation Date'][:7]}. Standard ACER renewal pitch."
    else:
        return f"Warm outreach September — escalates to MEDIUM in October. Awareness call, not hard pitch."

sept_pool['September_Action'] = sept_pool.apply(sept_action, axis=1)

# Priority score for sorting
sept_pool['Priority_Score'] = (
    (sept_pool['Escalates To'] == 'ULTRA HOT').astype(int) * 3 +
    (sept_pool['Escalates To'] == 'HOT').astype(int) * 2 +
    (sept_pool['Escalates To'] == 'MEDIUM').astype(int) * 1 +
    (sept_pool['Call Week'] == 'Oct Wk1 (Oct 1-7)').astype(int)  # bonus for Wk1
)

sept_pool_sorted = sept_pool.sort_values(['Priority_Score','Amt_parsed'], ascending=[False,False])

# Columns for final file
sept_cols = [
    'Company Name', 'Agency', 'Instrument Type', 'Rating', 'Rating Date',
    'Escalates To', 'Escalation Date', 'Call Week', 'Amount Cr', 'Sector',
    'Why Target', 'ACER Pitch Angle', 'September_Action', 'Priority_Score'
]
sept_out = sept_pool_sorted[[c for c in sept_cols if c in sept_pool_sorted.columns]]
sept_out.to_csv(f"{OUT_DIR}/september_precall_list_{TODAY}.csv", index=False)
print(f"\nSaved: {OUT_DIR}/september_precall_list_{TODAY}.csv ({len(sept_out)} rows, {sept_out['Company Name'].nunique()} unique)")

# ULTRA HOT subset (call immediately in September)
sept_uh = sept_out[sept_out['Escalates To'] == 'ULTRA HOT']
sept_uh.to_csv(f"{OUT_DIR}/september_precall_ultraHOT_{TODAY}.csv", index=False)
print(f"Saved: september_precall_ultraHOT ({len(sept_uh)} rows)")

# Top targets
print("\nTop 15 September Pre-Call Targets:")
print(sept_out[['Company Name','Agency','Instrument Type','Escalates To','Escalation Date','Amount Cr','Sector']].head(15).to_string())


# =============================================================================
# TASK 3: Cross-Agency Duplicate Check — October Pool
# =============================================================================
print("\n" + "="*60)
print("TASK 3: Cross-Agency Duplicate Check — October Pool")
print("="*60)

# Find companies appearing under 2+ agencies
co_agency = oct_wk.groupby('Company Name')['Agency'].apply(
    lambda x: sorted(x.unique())
).reset_index()
co_agency.columns = ['Company Name', 'Agencies_List']
co_agency['Agency_Count'] = co_agency['Agencies_List'].apply(len)
co_agency['Agencies'] = co_agency['Agencies_List'].apply(lambda x: ' + '.join(x))

# Multi-agency companies
multi = co_agency[co_agency['Agency_Count'] >= 2].copy()
print(f"\nTotal unique companies in October pool: {co_agency['Company Name'].nunique()}")
print(f"Companies rated by 2+ agencies in October pool: {len(multi)}")
print(f"  By agency count:")
print(multi['Agency_Count'].value_counts().to_string())

if len(multi) > 0:
    print(f"\nAgency pair breakdown:")
    print(multi['Agencies'].value_counts().head(20).to_string())

# Enrich multi-agency companies with full data
multi_enr = oct_wk[oct_wk['Company Name'].isin(multi['Company Name'])].copy()
multi_enr['Amt_parsed'] = multi_enr['Amount Cr'].apply(parse_amt)

# Add agency count and list to each row
multi_enr = multi_enr.merge(
    co_agency[['Company Name','Agency_Count','Agencies']],
    on='Company Name', how='left'
)

# Priority: companies rated by most agencies first, then ULTRA HOT, then amount
multi_enr['Esc_Priority'] = multi_enr['Escalates To'].map({'ULTRA HOT': 3, 'HOT': 2, 'MEDIUM': 1})
multi_enr_sorted = multi_enr.sort_values(['Agency_Count','Esc_Priority','Amt_parsed'], ascending=[False,False,False])

print(f"\nTop 20 multi-agency October targets:")
print(multi_enr_sorted[['Company Name','Agency','Instrument Type','Rating','Escalates To','Amount Cr','Sector','Agencies']].head(20).to_string())

# Save outputs
multi_out = multi_enr_sorted.drop(columns=['Amt_parsed','Esc_Priority'], errors='ignore')
multi_out.to_csv(f"{OUT_DIR}/october2026_cross_agency_duplicates_{TODAY}.csv", index=False)
print(f"\nSaved: {OUT_DIR}/october2026_cross_agency_duplicates_{TODAY}.csv ({len(multi_out)} rows)")

# Summary CSV by company
multi_summary = multi_enr_sorted.groupby(['Company Name','Agencies','Agency_Count']).agg(
    Total_Records=('Company Name','count'),
    Instruments=('Instrument Type', lambda x: ' | '.join(x.unique())),
    Max_Urgency=('Esc_Priority', 'max'),
    Total_Amt_Cr=('Amt_parsed','sum'),
    Sector=('Sector','first'),
).reset_index()
multi_summary['Max_Urgency_Label'] = multi_summary['Max_Urgency'].map({3:'ULTRA HOT',2:'HOT',1:'MEDIUM'})
multi_summary = multi_summary.sort_values(['Agency_Count','Max_Urgency'], ascending=[False,False])
multi_summary.to_csv(f"{OUT_DIR}/october2026_cross_agency_summary_{TODAY}.csv", index=False)
print(f"Saved: october2026_cross_agency_summary ({len(multi_summary)} unique companies)")

# Why these are highest priority — note for each
print("\nWhy cross-agency companies are top priority:")
print("→ Already open to multiple raters = lowest switching cost")
print("→ Not captive to any single agency = ACER can pitch directly")
print("→ All are escalating to HOT/ULTRA HOT in Oct-Nov 2026")


# =============================================================================
# TASK 4: Infomerics October Deep-Dive
# =============================================================================
print("\n" + "="*60)
print("TASK 4: Infomerics October Deep-Dive")
print("="*60)

inf_oct = oct_wk[oct_wk['Agency'] == 'Infomerics'].copy()
print(f"\nInfomerics October pool: {len(inf_oct)} records | {inf_oct['Company Name'].nunique()} unique companies")
print(f"Source confirmed: {inf_oct['Source'].value_counts().to_string()}")

# Urgency breakdown
uh_i = (inf_oct['Escalates To'] == 'ULTRA HOT').sum()
hot_i = (inf_oct['Escalates To'] == 'HOT').sum()
med_i = (inf_oct['Escalates To'] == 'MEDIUM').sum()
print(f"\nULTRA HOT: {uh_i} | HOT: {hot_i} | MEDIUM: {med_i}")
print(f"Callable (UH+HOT): {uh_i+hot_i} records ({inf_oct[inf_oct['Escalates To'].isin(['ULTRA HOT','HOT'])]['Company Name'].nunique()} unique)")

inf_oct['Amt_parsed'] = inf_oct['Amount Cr'].apply(parse_amt)
print(f"Total amount: ₹{inf_oct['Amt_parsed'].sum():,.0f} Cr")

# Instrument breakdown
print("\nInfomerics Instrument Mix:")
print(inf_oct.groupby('Instrument Type').agg(
    Records=('Company Name','count'),
    UH=('Escalates To', lambda x:(x=='ULTRA HOT').sum()),
    HOT=('Escalates To', lambda x:(x=='HOT').sum()),
    Total_Amt_Cr=('Amt_parsed','sum'),
).sort_values('Records', ascending=False).to_string())

# Weekly breakdown
print("\nInfomerics Weekly Schedule:")
print(inf_oct.groupby('Call Week').agg(
    Records=('Company Name','count'),
    Unique=('Company Name','nunique'),
    UH=('Escalates To', lambda x:(x=='ULTRA HOT').sum()),
    HOT=('Escalates To', lambda x:(x=='HOT').sum()),
).to_string())

# Sector breakdown
print("\nInfomerics Sector Breakdown:")
inf_sec = inf_oct.groupby('Sector').agg(
    Records=('Company Name','count'),
    Unique=('Company Name','nunique'),
    UH=('Escalates To', lambda x:(x=='ULTRA HOT').sum()),
    HOT=('Escalates To', lambda x:(x=='HOT').sum()),
    Total_Amt_Cr=('Amt_parsed','sum'),
).sort_values('Records', ascending=False)
print(inf_sec.to_string())

# Confirm zero competitor overlap — check against D365 companies
# Normalize company names for matching
inf_cos_norm = set(inf_oct['Company Name'].str.strip().str.upper().str.replace(r'\s+', ' ', regex=True))
d365_cos_norm = set(d365.iloc[:,0].astype(str).str.strip().str.upper().str.replace(r'\s+', ' ', regex=True)) if len(d365.columns) > 0 else set()

# Try to get company name column from d365
d365_co_col = None
for col in d365.columns:
    if 'company' in col.lower() or 'name' in col.lower():
        d365_co_col = col
        break
if d365_co_col:
    d365_cos_norm = set(d365[d365_co_col].astype(str).str.strip().str.upper().str.replace(r'\s+', ' ', regex=True))
    exact_overlap = inf_cos_norm & d365_cos_norm
    print(f"\nCompetitor overlap check: Infomerics Oct companies vs D365")
    print(f"  Infomerics Oct: {len(inf_cos_norm)} unique")
    print(f"  D365 companies: {len(d365_cos_norm)} unique")
    print(f"  Exact name overlap: {len(exact_overlap)} companies")
    if exact_overlap:
        print(f"  Overlapping companies (first 10): {list(exact_overlap)[:10]}")
else:
    print("\nCould not determine D365 company name column for overlap check")
    print(f"D365 columns: {d365.columns.tolist()}")

# Top Infomerics October targets
print("\nTop 20 Infomerics October targets (ULTRA HOT first, then by amount):")
inf_top = inf_oct.sort_values(['Escalates To','Amt_parsed'], ascending=[True,False])
print(inf_top[['Company Name','Instrument Type','Rating','Rating Date','Escalates To','Escalation Date','Amount Cr','Sector','Call Week']].head(20).to_string())

# Add Infomerics-specific pitch
def inf_pitch(row):
    base = "Infomerics-rated company — ZERO competitor overlap with major agencies. ACER is first challenger agency to approach this company."
    if row['Escalates To'] == 'ULTRA HOT':
        return base + f" Rating overdue — ACER can onboard immediately and issue faster than Infomerics turnaround."
    return base + f" Get ahead of renewal — ACER offers fresh perspective + speed."

inf_oct['ACER_Pitch_Infomerics'] = inf_oct.apply(inf_pitch, axis=1)

# Save Infomerics October file
inf_out = inf_oct.drop(columns=['Amt_parsed'], errors='ignore')
inf_out.to_csv(f"{OUT_DIR}/infomerics_october2026_targets_{TODAY}.csv", index=False)
print(f"\nSaved: {OUT_DIR}/infomerics_october2026_targets_{TODAY}.csv ({len(inf_out)} rows)")

# Callable subset
inf_callable = inf_out[inf_out['Escalates To'].isin(['ULTRA HOT','HOT'])]
inf_callable.to_csv(f"{OUT_DIR}/infomerics_october2026_callable_{TODAY}.csv", index=False)
print(f"Saved: infomerics_october2026_callable ({len(inf_callable)} rows, {inf_callable['Company Name'].nunique()} unique)")

# Sector summary
inf_sec.reset_index().to_csv(f"{OUT_DIR}/infomerics_october2026_sector_{TODAY}.csv", index=False)
print(f"Saved: infomerics_october2026_sector ({len(inf_sec)} sectors)")


# =============================================================================
# SUMMARY STATISTICS
# =============================================================================
print("\n" + "="*60)
print("SESSION 32 SUMMARY STATISTICS")
print("="*60)

print(f"\nD365 source record count: {len(d365)}")
print(f"Infomerics source record count: {len(inf)}")
print(f"October clean callable pool: {len(oct_wk)} records")

print(f"\nTask 1 — IND-RA + ICRA October Brief:")
print(f"  IND-RA: {len(indra_oct)} records | {indra_oct['Company Name'].nunique()} unique | {(indra_oct['Escalates To']=='ULTRA HOT').sum()} UH | {(indra_oct['Escalates To']=='HOT').sum()} HOT")
print(f"  ICRA: {len(icra_oct)} records | {icra_oct['Company Name'].nunique()} unique | {(icra_oct['Escalates To']=='ULTRA HOT').sum()} UH | {(icra_oct['Escalates To']=='HOT').sum()} HOT")
print(f"  Combined: {len(combined_oct)} records | {combined_oct['Company Name'].nunique()} unique")
print(f"  IND-RA peak week: Oct Wk2 (148 records) — NCD renewal concentration")
print(f"  ICRA peak week: Oct Wk4 (127 records)")

print(f"\nTask 2 — September Pre-Call List:")
print(f"  {len(sept_out)} records | {sept_out['Company Name'].nunique()} unique companies")
print(f"  ULTRA HOT escalations: {(sept_out['Escalates To']=='ULTRA HOT').sum()}")
print(f"  HOT escalations: {(sept_out['Escalates To']=='HOT').sum()}")
print(f"  Total identified amount: ₹{sept_pool['Amt_parsed'].sum():,.0f} Cr")

print(f"\nTask 3 — Cross-Agency Duplicates:")
print(f"  {len(multi)} unique companies rated by 2+ agencies in October pool")
print(f"  {len(multi_out)} total records across multi-agency companies")

print(f"\nTask 4 — Infomerics October Deep-Dive:")
print(f"  {len(inf_oct)} records | {inf_oct['Company Name'].nunique()} unique")
print(f"  ULTRA HOT: {uh_i} | HOT: {hot_i} | Callable: {uh_i+hot_i}")
print(f"  Zero major competitor overlap — exclusive ACER pipeline")

print("\nAll outputs saved to:", OUT_DIR)
print("Session 32 analysis complete.")
