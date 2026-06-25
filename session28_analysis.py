#!/usr/bin/env python3
"""
ACER Intelligence — Session 28 Analysis
Date: 2026-06-25
Tasks:
  1. October 2026 Calling Calendar (April 2026 cohort + all Oct-Nov escalations)
  2. Energy NCD Consolidated Calling List (all agencies)
  3. ICRA NCD vs CARE NCD Comparison (revenue, segment profiles)
"""

import pandas as pd
import numpy as np
from datetime import datetime, date
import os
import re

TODAY = date(2026, 6, 25)
SESSION_DIR = "intelligence_outputs/session_20260625/csv"
os.makedirs(SESSION_DIR, exist_ok=True)

print("=" * 70)
print("ACER Intelligence — Session 28")
print(f"Analysis date: {TODAY}")
print("=" * 70)

# ─────────────────────────────────────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────────────────────────────────────
print("\n[LOADING DATA]")
d365_raw = pd.read_excel("d365_data.xlsx")
info_raw = pd.read_excel("infomerics.json.xlsx")
print(f"  D365: {len(d365_raw):,} records loaded")
print(f"  Infomerics: {len(info_raw):,} records loaded")

# ─────────────────────────────────────────────────────────────────────────────
# CLEAN D365
# ─────────────────────────────────────────────────────────────────────────────
d365 = d365_raw.copy()
d365.rename(columns={"Output source file name: W11": "Company Name"}, inplace=True)
d365 = d365[d365["Agency"].isin(["CRISIL","CARE","ICRA","IND-RA","ACUITE","BRICKWORK"])].copy()
d365.reset_index(drop=True, inplace=True)

def parse_date_d365(val):
    if pd.isna(val): return pd.NaT
    s = str(val).strip()
    for fmt in ["%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y"]:
        try: return pd.to_datetime(s, format=fmt)
        except: pass
    try: return pd.to_datetime(s, dayfirst=True)
    except: return pd.NaT

d365["Rating_Date"] = d365["Date"].apply(parse_date_d365)
d365["is_INC"] = d365["Company/Issuer not cooperating"].str.strip().str.upper() == "Y"
d365["Days_Since"] = d365["Rating_Date"].apply(
    lambda x: (TODAY - x.date()).days if pd.notna(x) else np.nan
)

def urgency(days):
    if pd.isna(days): return "UNKNOWN"
    if days >= 365: return "ULTRA HOT"
    if days >= 270: return "HOT"
    if days >= 180: return "MEDIUM"
    return "LOW"

d365["Urgency"] = d365["Days_Since"].apply(urgency)

def std_instrument(i):
    if pd.isna(i): return 'Other'
    il = str(i).strip().lower()
    if 'non-government' in il or 'ncd' in il or 'debenture' in il or 'bond' in il: return 'NCD/Bond'
    if 'term loan' in il or il == 'tl': return 'Term Loan'
    if 'bank guarantee' in il or il == 'bg': return 'Bank Guarantee'
    if 'letter of credit' in il or il == 'lc' or 'l/c' in il: return 'Letter of Credit'
    if 'non-fund' in il or 'nfb' in il: return 'Non-Fund-Based'
    if ('fund' in il and 'based' in il) or il == 'fb': return 'Fund-Based'
    if 'commercial paper' in il or il == 'cp': return 'Commercial Paper'
    if 'cash credit' in il or il == 'cc' or 'overdraft' in il: return 'Cash Credit/OD'
    if 'working capital' in il: return 'Working Capital'
    return str(i).strip()

d365["Instrument_Std"] = d365["Instrument"].apply(std_instrument)

def parse_amount(v):
    if pd.isna(v): return np.nan
    if isinstance(v, (int, float)): return float(v) if not (isinstance(v, float) and np.isnan(v)) else np.nan
    s = str(v).lower().replace(',', '').strip()
    m = re.search(r'\d+\.?\d*', s)
    if m:
        try:
            val = float(m.group())
        except ValueError:
            return np.nan
        if 'lakh' in s or 'lac' in s: val /= 100
        return val
    return np.nan

d365["Amount_Cr"] = d365["Ammount"].apply(parse_amount)

valid_d365 = d365[d365["Rating_Date"].notna()].copy()
print(f"  D365 valid dates: {len(valid_d365):,} records")
print(f"  D365 INC records: {d365['is_INC'].sum():,}")

# ─────────────────────────────────────────────────────────────────────────────
# CLEAN INFOMERICS
# ─────────────────────────────────────────────────────────────────────────────
info = info_raw.copy()

def parse_date_info(val):
    if pd.isna(val): return pd.NaT
    s = str(val).strip()
    for fmt in ["%B %d, %Y", "%d %B %Y", "%b %d, %Y", "%d-%m-%Y", "%Y-%m-%d"]:
        try: return pd.to_datetime(s, format=fmt)
        except: pass
    try: return pd.to_datetime(s)
    except: return pd.NaT

info["Rating_Date"] = info["Date"].apply(parse_date_info)
info["is_INC"] = info["Current Ratings"].str.contains("INC", na=False, case=False)
info["Days_Since"] = info["Rating_Date"].apply(
    lambda x: (TODAY - x.date()).days if pd.notna(x) else np.nan
)
info["Urgency"] = info["Days_Since"].apply(urgency)
# Infomerics amount is in "Size" column e.g. "Rs. 9.00 Cr."
info["Amount_Cr"] = info["Size"].apply(parse_amount) if "Size" in info.columns else np.nan

print(f"  Infomerics valid dates: {info['Rating_Date'].notna().sum():,}")
print(f"  Infomerics INC records: {info['is_INC'].sum():,}")

# ─────────────────────────────────────────────────────────────────────────────
# SECTOR + SUBSECTOR CLASSIFICATION (defined early — used throughout)
# ─────────────────────────────────────────────────────────────────────────────
SECTOR_PATTERNS = {
    'Steel & Metals':     r'steel|metal|iron|alumin|copper|zinc|tin|ferro|alloy|rolling|wire|pipe|tube|casting|forging',
    'Agro/Food':          r'agro|food|rice|sugar|cotton|grain|wheat|dal|oil mill|flour|poultry|dairy|spice|tea|coffee|tobacco|seed|farm|fert|pesticide|crop|mandi',
    'Construction':       r'construct|infra|build|cement|sand|stone|brick|tiles|real estate|realt|property|housing|township|developer',
    'Manufacturing':      r'manufactur|engineer|fabricat|component|assembly|industrial|equipment|machin',
    'Chemicals/Pharma':   r'chem|pharma|drug|\bapi\b|solvent|dye|pigment|polymer|plastic|rubber|petro|lubric|paint|varnish|resin|adhesive',
    'Textiles':           r'textile|garment|yarn|fabric|weav|spinning|knitting|cloth|apparel|fashion|silk|jute|fibre|fiber',
    'BFSI':               r'\bnbfc\b|\bnbf\b|finance|bank|lending|microfinance|mfi|housing finance|insurance|leasing|asset management|securities|stock|broker|mutual fund|wealth',
    'Energy':             r'energy|power|solar|wind|renew|electric|generat|turbine|coal\b|oil\b|gas\b|fuel|petrol|diesel|thermal|hydro',
    'Healthcare':         r'hospital|health|medical|clinic|diagnostic|lab|nursing|biotech|life science',
    'Logistics':          r'logistic|transport|shipping|freight|cargo|warehou|cold chain|courier|truck|fleet|port|aviation',
    'IT/Technology':      r'\bit\b|software|tech|digital|telecom|communicat|network|data|cloud|app|e-commerce|internet',
    'Automobiles':        r'auto|vehicle|\bcar\b|\bbike\b|motor|tyre|component|ancillar',
    'Mining/Minerals':    r'mining|mineral|quarry|granite|marble|coal mine|iron ore|bauxite|limestone',
    'Education':          r'school|college|university|educat|institute|academy|coaching|training',
    'Jewellery/Gems':     r'jewel|gem|diamond|gold|silver|ornament|bullion',
    'Paper/Packaging':    r'paper|packaging|cardboard|corrugat|carton|\bbag\b|sack|print|ink',
    'Hotels/Tourism':     r'hotel|resort|hospitality|tourism|travel|restaurant|cafe',
    'Trading/Exports':    r'trad|export|import|merchant|wholesale|distribut|dealer',
}

def classify_sector(name):
    if pd.isna(name): return 'Other'
    n = str(name).lower()
    for sector, pat in SECTOR_PATTERNS.items():
        if re.search(pat, n): return sector
    return 'Other'

def classify_energy_sub(name):
    if pd.isna(name): return 'Other Energy'
    n = str(name).lower()
    if re.search(r'solar|wind|renew|green', n): return 'Renewable Energy'
    if re.search(r'power|electric|generat|turbine|thermal', n): return 'Power/Generation'
    if re.search(r'coal|mine', n): return 'Coal/Mining'
    if re.search(r'oil|gas|petro|fuel|diesel|refin', n): return 'Oil & Gas'
    if re.search(r'hydro', n): return 'Hydro Power'
    return 'Other Energy'

d365["Sector"] = d365["Company Name"].apply(classify_sector)
info["Sector"] = info["Company Name"].apply(classify_sector)

# ─────────────────────────────────────────────────────────────────────────────
# TASK 1: OCTOBER 2026 CALLING CALENDAR
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("TASK 1: OCTOBER 2026 CALLING CALENDAR")
print("=" * 70)

# April 2026 INC cohort summary
d365_inc = d365[d365["is_INC"] & d365["Rating_Date"].notna()].copy()
info_inc = info[info["is_INC"] & info["Rating_Date"].notna()].copy()

d365_inc["RatingYear"]  = d365_inc["Rating_Date"].dt.year
d365_inc["RatingMonth"] = d365_inc["Rating_Date"].dt.month
info_inc["RatingYear"]  = info_inc["Rating_Date"].dt.year
info_inc["RatingMonth"] = info_inc["Rating_Date"].dt.month

apr26_d365 = d365_inc[(d365_inc["RatingYear"]==2026) & (d365_inc["RatingMonth"]==4)]
apr26_info = info_inc[(info_inc["RatingYear"]==2026) & (info_inc["RatingMonth"]==4)]

print(f"\nApril 2026 INC cohort — D365: {len(apr26_d365):,} records, {apr26_d365['Company Name'].nunique():,} unique companies")
print("  By Agency:")
print(apr26_d365.groupby("Agency")["Company Name"].nunique().sort_values(ascending=False).to_string())
print(f"\nApril 2026 INC cohort — Infomerics: {len(apr26_info):,} records, {apr26_info['Company Name'].nunique():,} unique companies")

# Urgency at Oct 1 and Nov 1 for April cohort
OCT_1  = date(2026, 10, 1)
NOV_1  = date(2026, 11, 1)
NOV_30 = date(2026, 11, 30)

def days_at(rd, target_date):
    if pd.isna(rd): return np.nan
    try: return (target_date - rd.date()).days
    except: return np.nan

d365_apr = apr26_d365.copy()
d365_apr["Days_Oct1"] = d365_apr["Rating_Date"].apply(lambda x: days_at(x, OCT_1))
d365_apr["Days_Nov1"] = d365_apr["Rating_Date"].apply(lambda x: days_at(x, NOV_1))
d365_apr["Urg_Oct1"]  = d365_apr["Days_Oct1"].apply(urgency)
d365_apr["Urg_Nov1"]  = d365_apr["Days_Nov1"].apply(urgency)

print(f"\nApril 2026 cohort urgency transitions:")
print(f"  Current (Jun 25): {d365_apr.groupby('Urgency')['Company Name'].nunique().to_dict()}")
print(f"  At Oct  1 2026:   {d365_apr.groupby('Urg_Oct1')['Company Name'].nunique().to_dict()}")
print(f"  At Nov  1 2026:   {d365_apr.groupby('Urg_Nov1')['Company Name'].nunique().to_dict()}")

# ── OCTOBER–NOVEMBER 2026 FULL ESCALATION CALENDAR ──────────────────────────
# For EVERY INC company, check if any urgency threshold (MEDIUM/HOT/ULTRA HOT)
# falls within Oct 1 – Nov 30, 2026.
# threshold dates: entry into MEDIUM = rd+180, HOT = rd+270, ULTRA HOT = rd+365

def make_calendar_rows(df, company_col, agency_val, instr_col, rating_col, amount_col):
    rows = []
    for _, row in df.iterrows():
        company   = row[company_col]
        agency    = agency_val if agency_val else row.get("Agency","")
        instr     = row.get(instr_col, "")
        rating    = row.get(rating_col, "")
        rd        = row["Rating_Date"]
        days_now  = row["Days_Since"]
        cur_urg   = row["Urgency"]
        sector    = row["Sector"]
        amt       = row.get(amount_col, np.nan)

        if pd.isna(rd): continue

        for threshold_days, esc_label in [(180,"MEDIUM"),(270,"HOT"),(365,"ULTRA HOT")]:
            esc_date = (rd + pd.Timedelta(days=threshold_days)).date()
            if esc_date < OCT_1 or esc_date > NOV_30:
                continue
            # Only include if company hasn't already hit this threshold
            if pd.notna(days_now) and days_now >= threshold_days:
                continue
            rows.append({
                "Company Name":      company,
                "Agency":            agency,
                "Instrument Type":   str(instr),
                "Rating":            str(rating),
                "Rating Date":       rd.strftime("%d-%b-%Y"),
                "Current Urgency":   cur_urg,
                "Escalates To":      esc_label,
                "Escalation Date":   str(esc_date),
                "Escalation Month":  esc_date.strftime("%B %Y"),
                "Days Since (Jun 25)": int(days_now) if pd.notna(days_now) else "",
                "Amount Cr":         round(float(amt),2) if pd.notna(amt) else "",
                "Sector":            sector,
                "Source":            "Infomerics" if agency_val=="Infomerics" else "D365",
                "Why Target":        f"INC rating hits {esc_label} threshold on {esc_date} — first call window",
                "ACER Pitch Angle":  f"Get ahead of the Oct/Nov renewal rush; start ACER process now before {agency} backlog builds"
            })
    return rows

# D365 INC entries
d365_rows = make_calendar_rows(
    d365_inc, "Company Name", None, "Instrument_Std", "Rating", "Amount_Cr"
)

# Infomerics INC entries
info_instr_col = "Instruments" if "Instruments" in info_inc.columns else "Instrument"
info_rows = make_calendar_rows(
    info_inc, "Company Name", "Infomerics", info_instr_col, "Current Ratings", "Amount_Cr"
)

oct_df = pd.DataFrame(d365_rows + info_rows)
print(f"\nOct–Nov 2026 calling calendar (all escalations):")
print(f"  Total records: {len(oct_df):,}")
if len(oct_df) > 0:
    print(f"  Unique companies: {oct_df['Company Name'].nunique():,}")
    print(f"\n  By Escalates To:")
    print(oct_df.groupby("Escalates To")["Company Name"].nunique().sort_values(ascending=False).to_string())
    print(f"\n  By Escalation Month:")
    print(oct_df.groupby("Escalation Month")["Company Name"].nunique().sort_values(ascending=False).to_string())
    print(f"\n  By Agency:")
    print(oct_df.groupby("Agency")["Company Name"].nunique().sort_values(ascending=False).to_string())
    print(f"\n  By Sector:")
    print(oct_df.groupby("Sector")["Company Name"].nunique().sort_values(ascending=False).head(10).to_string())

# Sort by escalation date then esc type priority
esc_order = {"ULTRA HOT":0,"HOT":1,"MEDIUM":2}
oct_df["_esc_sort"] = oct_df["Escalates To"].map(esc_order).fillna(3)
oct_df_sorted = oct_df.sort_values(["Escalation Date","_esc_sort"]).drop("_esc_sort",axis=1)

# Save files
out_full = f"{SESSION_DIR}/october2026_calling_calendar_20260625.csv"
oct_df_sorted.to_csv(out_full, index=False)
print(f"\n  Saved (full calendar): {out_full} ({len(oct_df_sorted):,} rows)")

# HOT and ULTRA HOT escalations only
oct_hot_plus = oct_df_sorted[oct_df_sorted["Escalates To"].isin(["HOT","ULTRA HOT"])].copy()
out_hot = f"{SESSION_DIR}/october2026_hot_ultraHOT_20260625.csv"
oct_hot_plus.to_csv(out_hot, index=False)
print(f"  Saved (HOT+ escalations): {out_hot} ({len(oct_hot_plus):,} rows, {oct_hot_plus['Company Name'].nunique():,} unique)")

# April 2026 cohort detail
apr_cohort_rows = []
for _, row in d365_apr.iterrows():
    amt = row.get("Amount_Cr", np.nan)
    apr_cohort_rows.append({
        "Company Name":       row["Company Name"],
        "Agency":             row["Agency"],
        "Instrument Type":    row["Instrument_Std"],
        "Rating":             row.get("Rating",""),
        "Rating Date":        row["Rating_Date"].strftime("%d-%b-%Y"),
        "Days Since (Jun 25)": int(row["Days_Since"]) if pd.notna(row["Days_Since"]) else "",
        "Current Urgency":    row["Urgency"],
        "Urgency at Oct 1":   row["Urg_Oct1"],
        "Urgency at Nov 1":   row["Urg_Nov1"],
        "Amount Cr":          round(float(amt),2) if pd.notna(amt) else "",
        "Sector":             row["Sector"],
        "Why Target":         "April 2026 INC cohort — enters MEDIUM urgency by Nov 1 2026"
    })
apr_df = pd.DataFrame(apr_cohort_rows)
out_apr = f"{SESSION_DIR}/april2026_cohort_detail_20260625.csv"
apr_df.to_csv(out_apr, index=False)
print(f"  Saved (April 2026 cohort): {out_apr} ({len(apr_df):,} rows, {apr_df['Company Name'].nunique():,} unique)")

# Monthly summary
if len(oct_df) > 0:
    monthly = oct_df.groupby(["Escalation Month","Escalates To","Agency"]).agg(
        Companies=("Company Name","nunique"),
        Records=("Company Name","count")
    ).reset_index().sort_values(["Escalation Month","Escalates To"])
    out_monthly = f"{SESSION_DIR}/october2026_monthly_summary_20260625.csv"
    monthly.to_csv(out_monthly, index=False)
    print(f"  Saved (monthly summary): {out_monthly} ({len(monthly):,} rows)")

# ─────────────────────────────────────────────────────────────────────────────
# TASK 2: ENERGY NCD CONSOLIDATED CALLING LIST
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("TASK 2: ENERGY NCD CONSOLIDATED CALLING LIST")
print("=" * 70)

energy_ncd_d365 = d365_inc[
    (d365_inc["Sector"] == "Energy") &
    (d365_inc["Instrument_Std"] == "NCD/Bond")
].copy()

print(f"\nEnergy NCD INC (D365): {len(energy_ncd_d365):,} records, {energy_ncd_d365['Company Name'].nunique():,} unique companies")
print("  By Agency:")
print(energy_ncd_d365.groupby("Agency")["Company Name"].nunique().sort_values(ascending=False).to_string())
print("  By Urgency:")
print(energy_ncd_d365.groupby("Urgency")["Company Name"].nunique().sort_values(ascending=False).to_string())

# Infomerics energy NCD (Infomerics instrument column = "Instruments")
info_instr_col = "Instruments" if "Instruments" in info_inc.columns else "Instrument"
info_energy_mask = (
    (info_inc["Sector"] == "Energy") &
    info_inc[info_instr_col].fillna("").str.lower().str.contains("ncd|debenture|bond|non-government", na=False)
)
info_energy_ncd = info_inc[info_energy_mask].copy()
print(f"\nEnergy NCD INC (Infomerics): {len(info_energy_ncd):,} records, {info_energy_ncd['Company Name'].nunique() if len(info_energy_ncd)>0 else 0:,} unique companies")

# Build consolidated list
def build_energy_ncd_row(row, agency_override=None):
    company = row["Company Name"]
    agency  = agency_override or row.get("Agency","")
    instr   = row.get("Instrument_Std", row.get(info_instr_col if agency_override else "Instrument_Std", "NCD/Bond"))
    rating  = row.get("Rating", row.get("Current Ratings",""))
    rd      = row["Rating_Date"]
    days    = row["Days_Since"]
    urg     = row["Urgency"]
    amt     = row.get("Amount_Cr", np.nan)
    return {
        "Company Name":    company,
        "Current Rater":   agency,
        "Instrument":      str(instr),
        "Rating":          str(rating),
        "Rating Date":     rd.strftime("%d-%b-%Y") if pd.notna(rd) else "",
        "Days Since Rating": int(days) if pd.notna(days) else "",
        "Urgency":         urg,
        "Amount Cr":       round(float(amt),2) if pd.notna(amt) else "",
        "Sector":          "Energy",
        "Sub-Sector":      classify_energy_sub(company),
        "Source":          "Infomerics" if agency_override else "D365",
        "Why Target":      f"Energy NCD INC at {agency} ({int(days) if pd.notna(days) else '?'} days) — SEBI CRA license mandate for NCD",
        "ACER Pitch Angle": f"NCD rated INC by {agency} — ACER specialises in energy sector NCD; 2-3 week completion"
    }

energy_rows = []
for _, row in energy_ncd_d365.iterrows():
    energy_rows.append(build_energy_ncd_row(row))
if len(info_energy_ncd) > 0:
    for _, row in info_energy_ncd.iterrows():
        r = row.copy()
        r["Instrument_Std"] = row.get(info_instr_col, "NCD/Bond")
        energy_rows.append(build_energy_ncd_row(r, agency_override="Infomerics"))

energy_ncd_df = pd.DataFrame(energy_rows)

urg_order = {"ULTRA HOT":0,"HOT":1,"MEDIUM":2,"LOW":3,"UNKNOWN":4}
energy_ncd_df["_sort"] = energy_ncd_df["Urgency"].map(urg_order).fillna(4)
energy_ncd_df = energy_ncd_df.sort_values(["_sort","Amount Cr"], ascending=[True,False]).drop("_sort",axis=1)

print(f"\nConsolidated Energy NCD INC: {len(energy_ncd_df):,} records, {energy_ncd_df['Company Name'].nunique():,} unique companies")
if len(energy_ncd_df) > 0:
    print("  By Agency:")
    print(energy_ncd_df.groupby("Current Rater")["Company Name"].nunique().sort_values(ascending=False).to_string())
    print("  By Urgency:")
    print(energy_ncd_df.groupby("Urgency")["Company Name"].nunique().sort_values(ascending=False).to_string())
    print("  By Sub-Sector:")
    print(energy_ncd_df.groupby("Sub-Sector")["Company Name"].nunique().sort_values(ascending=False).to_string())
    energy_ncd_df["Amount_Num"] = pd.to_numeric(energy_ncd_df["Amount Cr"], errors='coerce')
    amt_num = energy_ncd_df["Amount_Num"]
    print(f"\n  Total identified NCD amount: ₹{amt_num.sum():,.1f} Cr")
    print(f"  Avg NCD amount: ₹{amt_num.mean():,.1f} Cr | Median: ₹{amt_num.median():,.1f} Cr")
    print("\n  Top 15 by Amount:")
    top15 = energy_ncd_df[amt_num.notna()].nlargest(15, "Amount_Num")
    for _, r in top15.iterrows():
        print(f"    {str(r['Company Name'])[:45]:45s}  ₹{r['Amount_Num']:>8.1f} Cr  {r['Urgency']:10s}  {r['Current Rater']}")
    energy_ncd_df = energy_ncd_df.drop("Amount_Num", axis=1)

out_energy = f"{SESSION_DIR}/energy_ncd_inc_all_agencies_20260625.csv"
energy_ncd_df.to_csv(out_energy, index=False)
print(f"\n  Saved: {out_energy} ({len(energy_ncd_df):,} rows)")

energy_hot = energy_ncd_df[energy_ncd_df["Urgency"].isin(["ULTRA HOT","HOT"])].copy()
out_energy_hot = f"{SESSION_DIR}/energy_ncd_hot_only_20260625.csv"
energy_hot.to_csv(out_energy_hot, index=False)
print(f"  Saved (HOT+ only): {out_energy_hot} ({len(energy_hot):,} rows, {energy_hot['Company Name'].nunique():,} unique)")

if len(energy_ncd_df) > 0:
    agency_sum = energy_ncd_df.groupby(["Current Rater","Urgency"]).agg(
        Companies=("Company Name","nunique"),
        Records=("Company Name","count"),
    ).reset_index()
    out_agency_sum = f"{SESSION_DIR}/energy_ncd_agency_summary_20260625.csv"
    agency_sum.to_csv(out_agency_sum, index=False)
    print(f"  Saved (agency summary): {out_agency_sum} ({len(agency_sum):,} rows)")

# ─────────────────────────────────────────────────────────────────────────────
# TASK 3: ICRA NCD vs CARE NCD COMPARISON
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("TASK 3: ICRA NCD vs CARE NCD COMPARISON")
print("=" * 70)

icra_ncd = d365_inc[(d365_inc["Agency"]=="ICRA") & (d365_inc["Instrument_Std"]=="NCD/Bond")].copy()
care_ncd = d365_inc[(d365_inc["Agency"]=="CARE") & (d365_inc["Instrument_Std"]=="NCD/Bond")].copy()

print(f"\nICRA NCD INC: {len(icra_ncd):,} records, {icra_ncd['Company Name'].nunique():,} unique companies")
print(f"CARE NCD INC: {len(care_ncd):,} records, {care_ncd['Company Name'].nunique():,} unique companies")

def ncd_stats(df, label):
    print(f"\n--- {label} NCD INC STATS ---")
    print(f"  Records: {len(df):,} | Unique companies: {df['Company Name'].nunique():,}")
    print(f"  Urgency:")
    print(df.groupby("Urgency")["Company Name"].nunique().sort_values(ascending=False).to_string())
    amt = pd.to_numeric(df["Amount_Cr"], errors='coerce')
    print(f"  Amount (Cr) — total: ₹{amt.sum():,.1f} | mean: ₹{amt.mean():,.1f} | median: ₹{amt.median():,.1f} | max: ₹{amt.max():,.1f}")
    print(f"  Top sectors:")
    print(df.groupby("Sector")["Company Name"].nunique().sort_values(ascending=False).head(8).to_string())
    print(f"  Top ratings:")
    print(df["Rating"].value_counts().head(8).to_string())
    return float(amt.sum()), float(amt.mean()), float(amt.median())

icra_total, icra_mean, icra_med = ncd_stats(icra_ncd, "ICRA")
care_total, care_mean, care_med = ncd_stats(care_ncd, "CARE")

# Per-company aggregation for top 20
def top_by_amount(df, agency_label, n=20):
    agg = df.groupby("Company Name").agg(
        Agency=("Agency","first"),
        Count=("Instrument_Std","count"),
        Total_Amt=("Amount_Cr","sum"),
        Max_Amt=("Amount_Cr","max"),
        Rating=("Rating", lambda x: x.mode()[0] if len(x)>0 else ""),
        Latest_Date=("Rating_Date","max"),
        Urgency=("Urgency", lambda x: x.mode()[0] if len(x)>0 else ""),
        Days_Since=("Days_Since","max"),
        Sector=("Sector","first")
    ).reset_index()
    agg["Latest_Date_Str"] = agg["Latest_Date"].dt.strftime("%d-%b-%Y")
    agg = agg.sort_values("Total_Amt", ascending=False).head(n)
    return agg

icra_top20 = top_by_amount(icra_ncd, "ICRA")
care_top20 = top_by_amount(care_ncd, "CARE")

print(f"\n--- ICRA NCD INC Top 20 by Amount ---")
for i, r in enumerate(icra_top20.itertuples(), 1):
    amt = r.Total_Amt if pd.notna(r.Total_Amt) else 0
    print(f"  {i:2d}. {str(r._1)[:45]:45s}  ₹{amt:>8.1f} Cr  {r.Urgency:10s}  {r.Sector}")

print(f"\n--- CARE NCD INC Top 20 by Amount ---")
for i, r in enumerate(care_top20.itertuples(), 1):
    amt = r.Total_Amt if pd.notna(r.Total_Amt) else 0
    print(f"  {i:2d}. {str(r._1)[:45]:45s}  ₹{amt:>8.1f} Cr  {r.Urgency:10s}  {r.Sector}")

# Build comparison file — top 20 from each
comp_rows = []
for rank, r in enumerate(icra_top20.itertuples(), 1):
    amt = r.Total_Amt if pd.notna(r.Total_Amt) else 0
    comp_rows.append({
        "Agency": "ICRA",
        "Company Name": r._1,
        "Total Amount Cr": round(float(amt),2) if pd.notna(amt) else "",
        "Instrument Count": r.Count,
        "Rating": r.Rating,
        "Latest Rating Date": r.Latest_Date_Str,
        "Days Since Rating": int(r.Days_Since) if pd.notna(r.Days_Since) else "",
        "Urgency": r.Urgency,
        "Sector": r.Sector,
        "Rank (within ICRA NCD)": rank,
        "Why Target": f"ICRA NCD INC — ₹{round(float(amt),1)} Cr; {r.Urgency} priority",
        "ACER Pitch Angle": f"ICRA rated NCD INC — ACER provides faster NCD rating; avg ICRA NCD mandate ₹{icra_mean:.0f} Cr"
    })
for rank, r in enumerate(care_top20.itertuples(), 1):
    amt = r.Total_Amt if pd.notna(r.Total_Amt) else 0
    comp_rows.append({
        "Agency": "CARE",
        "Company Name": r._1,
        "Total Amount Cr": round(float(amt),2) if pd.notna(amt) else "",
        "Instrument Count": r.Count,
        "Rating": r.Rating,
        "Latest Rating Date": r.Latest_Date_Str,
        "Days Since Rating": int(r.Days_Since) if pd.notna(r.Days_Since) else "",
        "Urgency": r.Urgency,
        "Sector": r.Sector,
        "Rank (within CARE NCD)": rank,
        "Why Target": f"CARE NCD INC — ₹{round(float(amt),1)} Cr; {r.Urgency} priority",
        "ACER Pitch Angle": f"CARE rated NCD INC — ACER provides faster NCD rating; avg CARE NCD mandate ₹{care_mean:.0f} Cr"
    })

comp_df = pd.DataFrame(comp_rows)
out_comp = f"{SESSION_DIR}/icra_vs_care_ncd_comparison_20260625.csv"
comp_df.to_csv(out_comp, index=False)
print(f"\n  Saved (comparison top 20 each): {out_comp} ({len(comp_df):,} rows)")

# Full lists
def save_full_ncd(df, label):
    out = df[["Company Name","Agency","Instrument_Std","Rating","Rating_Date","Days_Since","Urgency","Amount_Cr","Sector"]].copy()
    out.columns = ["Company Name","Agency","Instrument","Rating","Rating Date","Days Since","Urgency","Amount Cr","Sector"]
    out["Rating Date"] = df["Rating_Date"].dt.strftime("%d-%b-%Y")
    out = out.sort_values("Amount Cr", ascending=False)
    fname = f"{SESSION_DIR}/{label.lower()}_ncd_inc_full_20260625.csv"
    out.to_csv(fname, index=False)
    print(f"  Saved ({label} NCD INC full): {fname} ({len(out):,} rows)")
    return out

icra_full = save_full_ncd(icra_ncd, "icra")
care_full = save_full_ncd(care_ncd, "care")

# Summary stats table
icra_uh  = icra_ncd[icra_ncd["Urgency"]=="ULTRA HOT"]["Company Name"].nunique()
care_uh  = care_ncd[care_ncd["Urgency"]=="ULTRA HOT"]["Company Name"].nunique()
icra_hot = icra_ncd[icra_ncd["Urgency"]=="HOT"]["Company Name"].nunique()
care_hot = care_ncd[care_ncd["Urgency"]=="HOT"]["Company Name"].nunique()

print(f"\n--- ICRA vs CARE NCD COMPARISON TABLE ---")
print(f"  {'Metric':<38} {'ICRA':>12} {'CARE':>12}")
print(f"  {'-'*64}")
print(f"  {'INC companies (NCD)':<38} {icra_ncd['Company Name'].nunique():>12,} {care_ncd['Company Name'].nunique():>12,}")
print(f"  {'Total Amount Identified (₹ Cr)':<38} {icra_total:>12,.1f} {care_total:>12,.1f}")
print(f"  {'Avg per Record (₹ Cr)':<38} {icra_mean:>12,.1f} {care_mean:>12,.1f}")
print(f"  {'Median Amount (₹ Cr)':<38} {icra_med:>12,.1f} {care_med:>12,.1f}")
print(f"  {'ULTRA HOT companies':<38} {icra_uh:>12,} {care_uh:>12,}")
print(f"  {'HOT companies':<38} {icra_hot:>12,} {care_hot:>12,}")
print(f"  {'Callable now (UH+HOT)':<38} {icra_uh+icra_hot:>12,} {care_uh+care_hot:>12,}")

# Sector comparison
icra_sectors = icra_ncd.groupby("Sector")["Company Name"].nunique().sort_values(ascending=False)
care_sectors = care_ncd.groupby("Sector")["Company Name"].nunique().sort_values(ascending=False)
sector_comp = pd.DataFrame({
    "ICRA NCD INC Companies": icra_sectors,
    "CARE NCD INC Companies": care_sectors
}).fillna(0).astype(int)
sector_comp["Total"] = sector_comp.sum(axis=1)
sector_comp = sector_comp.sort_values("Total", ascending=False)
out_sector_comp = f"{SESSION_DIR}/icra_care_ncd_sector_comparison_20260625.csv"
sector_comp.reset_index().rename(columns={"index":"Sector"}).to_csv(out_sector_comp, index=False)
print(f"\n  Saved (sector comparison): {out_sector_comp} ({len(sector_comp):,} rows)")

# ─────────────────────────────────────────────────────────────────────────────
# FINAL SUMMARY
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("SESSION 28 — FINAL SUMMARY")
print("=" * 70)
print(f"\n  D365: {len(d365_raw):,} records | Infomerics: {len(info_raw):,} records")
print(f"\n  TASK 1 — OCTOBER 2026 CALLING CALENDAR:")
print(f"    Total records (Oct–Nov escalations): {len(oct_df):,}")
print(f"    Unique companies: {oct_df['Company Name'].nunique() if len(oct_df)>0 else 0:,}")
print(f"    HOT/ULTRA HOT escalations: {len(oct_hot_plus):,} records, {oct_hot_plus['Company Name'].nunique():,} unique")
print(f"    April 2026 cohort: {len(apr_df):,} records, {apr_df['Company Name'].nunique():,} unique (enter MEDIUM Oct–Nov)")
print(f"\n  TASK 2 — ENERGY NCD INC:")
print(f"    Total: {len(energy_ncd_df):,} records, {energy_ncd_df['Company Name'].nunique() if len(energy_ncd_df)>0 else 0:,} unique")
print(f"    Callable HOT+: {len(energy_hot):,} records, {energy_hot['Company Name'].nunique():,} unique")
print(f"\n  TASK 3 — ICRA vs CARE NCD COMPARISON:")
print(f"    ICRA: {icra_ncd['Company Name'].nunique():,} cos, ₹{icra_total:,.1f} Cr | callable: {icra_uh+icra_hot:,}")
print(f"    CARE: {care_ncd['Company Name'].nunique():,} cos, ₹{care_total:,.1f} Cr | callable: {care_uh+care_hot:,}")
print(f"\n[DONE] All outputs → intelligence_outputs/session_20260625/csv/")
