"""
ACER Intelligence — Session 23 Analysis
Date: 2026-06-22
Tasks:
  1. ACUITE 2026 acceleration + geographic breakdown
  2. Feb 2026 CARE cohort targeting (120+ days overdue)
  3. Infomerics ULTRA HOT × D365 multi-agency cross-match
"""

import pandas as pd
import numpy as np
from datetime import datetime, date
import os
import re

TODAY = date(2026, 6, 22)
SESSION_DIR = "intelligence_outputs/session_20260622/csv"
os.makedirs(SESSION_DIR, exist_ok=True)

print("=" * 70)
print("ACER Intelligence — Session 23")
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

def parse_date_d365(val):
    if pd.isna(val):
        return pd.NaT
    s = str(val).strip()
    for fmt in ["%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y"]:
        try:
            return pd.to_datetime(s, format=fmt)
        except:
            pass
    try:
        return pd.to_datetime(s, dayfirst=True)
    except:
        return pd.NaT

d365["Rating_Date"] = d365["Date"].apply(parse_date_d365)
d365["is_INC"] = d365["Company/Issuer not cooperating"].str.strip().str.upper() == "Y"

# Days since rating
d365["Days_Since"] = d365["Rating_Date"].apply(
    lambda x: (TODAY - x.date()).days if pd.notna(x) else np.nan
)

def urgency(days):
    if pd.isna(days):
        return "UNKNOWN"
    if days >= 365:
        return "ULTRA HOT"
    if days >= 270:
        return "HOT"
    if days >= 180:
        return "MEDIUM"
    return "LOW"

d365["Urgency"] = d365["Days_Since"].apply(urgency)

valid_d365 = d365[d365["Rating_Date"].notna()].copy()
print(f"  D365 valid dates: {len(valid_d365):,} records")
print(f"  D365 INC records: {d365['is_INC'].sum():,}")

# ─────────────────────────────────────────────────────────────────────────────
# CLEAN INFOMERICS
# ─────────────────────────────────────────────────────────────────────────────
info = info_raw.copy()

def parse_date_info(val):
    if pd.isna(val):
        return pd.NaT
    s = str(val).strip()
    for fmt in ["%B %d, %Y", "%d %B %Y", "%b %d, %Y", "%d-%m-%Y", "%Y-%m-%d"]:
        try:
            return pd.to_datetime(s, format=fmt)
        except:
            pass
    try:
        return pd.to_datetime(s)
    except:
        return pd.NaT

info["Rating_Date"] = info["Date"].apply(parse_date_info)
info["is_INC"] = info["Current Ratings"].str.contains("INC", na=False, case=False)
info["Days_Since"] = info["Rating_Date"].apply(
    lambda x: (TODAY - x.date()).days if pd.notna(x) else np.nan
)
info["Urgency"] = info["Days_Since"].apply(urgency)
print(f"  Infomerics INC: {info['is_INC'].sum():,} records")

# ─────────────────────────────────────────────────────────────────────────────
# GEO INFERENCE HELPER
# ─────────────────────────────────────────────────────────────────────────────
STATE_KEYWORDS = {
    "Gujarat": ["gujarat","ahmedabad","surat","vadodara","rajkot","gandhinagar","anand",
                "bharuch","bhavnagar","junagadh","mehsana","morbi","vapi","mundra",
                " pvt. ltd., surat"," pvt. ltd., ahmedabad"],
    "Maharashtra": ["maharashtra","mumbai","pune","nagpur","nashik","aurangabad",
                   "thane","kolhapur","solapur","navi mumbai","pimpri","amravati",
                   "bandra","andheri","goregaon"],
    "Rajasthan": ["rajasthan","jaipur","jodhpur","udaipur","kota","bikaner","ajmer",
                  "bhilwara","sikar","alwar","pali","barmer"],
    "Tamil Nadu": ["tamil","chennai","coimbatore","madurai","tiruppur","salem","erode",
                   "tirunelveli","vellore","trichy","tirupur"],
    "Uttar Pradesh": ["uttar pradesh"," up ","noida","kanpur","lucknow","agra",
                      "varanasi","allahabad","prayagraj","meerut","ghaziabad",
                      "firozabad","moradabad","aligarh"],
    "Delhi NCR": ["delhi","new delhi","gurugram","gurgaon","faridabad"],
    "West Bengal": ["west bengal","kolkata","calcutta","howrah","durgapur","asansol",
                    "siliguri","bardhaman"],
    "Karnataka": ["karnataka","bengaluru","bangalore","mysuru","mysore","hubli",
                  "mangalore","belgaum","dharwad"],
    "Punjab/Haryana": ["punjab","haryana","ludhiana","amritsar","jalandhar",
                       "chandigarh","ambala","panipat","hisar","rohtak","karnal"],
    "Madhya Pradesh": ["madhya pradesh"," mp ","indore","bhopal","gwalior","jabalpur",
                       "ujjain","rewa"],
    "Andhra/Telangana": ["andhra","telangana","hyderabad","visakhapatnam",
                         "vijayawada","warangal","guntur","tirupati"],
    "Odisha": ["odisha","orissa","bhubaneswar","cuttack","rourkela","sambalpur"],
    "Bihar/Jharkhand": ["bihar","jharkhand","patna","ranchi","jamshedpur",
                        "dhanbad","muzaffarpur"],
    "Chhattisgarh": ["chhattisgarh","raipur","bhilai","bilaspur","durg"],
    "Himachal Pradesh": ["himachal","shimla","manali","dharamsala"],
    "Uttarakhand": ["uttarakhand","dehradun","haridwar","roorkee","haldwani"],
    "Kerala": ["kerala","kochi","thiruvananthapuram","calicut","kozhikode","thrissur"],
    "Goa": ["goa","panaji","vasco"],
    "Assam": ["assam","guwahati","dibrugarh","silchar"],
}

def infer_state(name):
    if pd.isna(name):
        return "Unknown"
    n = str(name).lower()
    for state, keywords in STATE_KEYWORDS.items():
        for kw in keywords:
            if kw in n:
                return state
    return "Unknown"

# ─────────────────────────────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════
# TASK 1: ACUITE 2026 ACCELERATION + GEOGRAPHIC BREAKDOWN
# ══════════════════════════════════════════════════════════════════════════════
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("TASK 1: ACUITE 2026 ACCELERATION — GEOGRAPHIC BREAKDOWN")
print("=" * 70)

acuite_all = valid_d365[valid_d365["Agency"] == "ACUITE"].copy()
acuite_inc = acuite_all[acuite_all["is_INC"]].copy()
print(f"  ACUITE total records: {len(acuite_all):,}")
print(f"  ACUITE INC records:   {len(acuite_inc):,}")
print(f"  ACUITE unique companies (all): {acuite_all['Company Name'].nunique():,}")
print(f"  ACUITE unique INC companies:   {acuite_inc['Company Name'].nunique():,}")

# Monthly trend
acuite_inc["Year"]  = acuite_inc["Rating_Date"].dt.year
acuite_inc["Month"] = acuite_inc["Rating_Date"].dt.month
acuite_inc["Month_Str"] = acuite_inc["Rating_Date"].dt.to_period("M").astype(str)

# Monthly counts of INC companies
monthly_inc = (
    acuite_inc.groupby("Month_Str")["Company Name"]
    .nunique()
    .reset_index()
    .rename(columns={"Company Name": "INC_Companies"})
    .sort_values("Month_Str")
)

# Monthly counts of all rated companies (to compute INC rate)
acuite_all["Month_Str"] = acuite_all["Rating_Date"].dt.to_period("M").astype(str)
monthly_all = (
    acuite_all.groupby("Month_Str")["Company Name"]
    .nunique()
    .reset_index()
    .rename(columns={"Company Name": "Total_Companies"})
)

monthly_trend = monthly_all.merge(monthly_inc, on="Month_Str", how="left")
monthly_trend["INC_Companies"] = monthly_trend["INC_Companies"].fillna(0).astype(int)
monthly_trend["INC_Rate_Pct"] = (monthly_trend["INC_Companies"] / monthly_trend["Total_Companies"] * 100).round(1)

# Filter to 2025 onwards for trend analysis
trend_focus = monthly_trend[monthly_trend["Month_Str"] >= "2025-01"].copy()

print(f"\n  ACUITE Monthly INC Trend (2025-2026):")
print(f"  {'Month':<12} {'Total':>8} {'INC':>8} {'INC%':>8}")
print(f"  {'-'*40}")
for _, row in trend_focus.iterrows():
    print(f"  {row['Month_Str']:<12} {row['Total_Companies']:>8,} {row['INC_Companies']:>8,} {row['INC_Rate_Pct']:>7.1f}%")

# Compare to CARE April spike (233 companies) for context
care_monthly = (
    valid_d365[(valid_d365["Agency"] == "CARE") & valid_d365["is_INC"]]
    .copy()
)
care_monthly["Month_Str"] = care_monthly["Rating_Date"].dt.to_period("M").astype(str)
care_april2026 = care_monthly[care_monthly["Month_Str"] == "2026-04"]["Company Name"].nunique()
print(f"\n  Reference: CARE April 2026 INC companies = {care_april2026:,}")

# Find ACUITE peak month
if len(trend_focus) > 0:
    acuite_peak = trend_focus.loc[trend_focus["INC_Companies"].idxmax()]
    print(f"  ACUITE peak month: {acuite_peak['Month_Str']} = {acuite_peak['INC_Companies']:,} companies ({acuite_peak['INC_Rate_Pct']:.1f}%)")

# Geographic breakdown of ALL ACUITE INC companies
acuite_inc["Inferred_State"] = acuite_inc["Company Name"].apply(infer_state)
geo_breakdown = acuite_inc.groupby("Inferred_State")["Company Name"].nunique().reset_index()
geo_breakdown.columns = ["State", "INC_Companies"]
geo_breakdown = geo_breakdown.sort_values("INC_Companies", ascending=False)

print(f"\n  ACUITE INC Geographic Breakdown:")
for _, row in geo_breakdown.iterrows():
    pct = row["INC_Companies"] / acuite_inc["Company Name"].nunique() * 100
    print(f"    {row['State']:<25} {row['INC_Companies']:>5,}  ({pct:.1f}%)")

# Build full output file
acuite_inc_out = acuite_inc.copy()
acuite_inc_out["Inferred_State"] = acuite_inc_out["Company Name"].apply(infer_state)
acuite_inc_out["Geo_Signal"] = acuite_inc_out["Inferred_State"].apply(
    lambda x: "State inferred from name" if x != "Unknown" else "Unknown"
)
acuite_inc_out["Why_Target"] = "ACUITE INC — accelerating INC pattern in 2025-2026; dissatisfied client"
acuite_inc_out["ACER_Pitch"] = "ACUITE has marked you non-cooperative — ACER offers faster turnaround and analyst access"

acuite_out = acuite_inc_out[[
    "Company Name","Rating_Date","Agency","Instrument","Grade","Rating",
    "Ammount","Days_Since","Urgency","Inferred_State","Geo_Signal",
    "Year","Month","Month_Str","Why_Target","ACER_Pitch"
]].copy()
acuite_out.rename(columns={"Rating_Date":"Rating_Date_Parsed","Ammount":"Amount_Cr"}, inplace=True)
acuite_out = acuite_out.sort_values(["Urgency","Days_Since"],
    key=lambda x: x.map({"ULTRA HOT":0,"HOT":1,"MEDIUM":2,"LOW":3,"UNKNOWN":4})
    if x.name == "Urgency" else x, ascending=[True, False])

acuite_out_path = f"{SESSION_DIR}/acuite_2026_acceleration_geo_20260622.csv"
acuite_out.to_csv(acuite_out_path, index=False)
print(f"\n  Saved: {acuite_out_path} ({len(acuite_out):,} rows)")

# Also save monthly trend
monthly_trend_path = f"{SESSION_DIR}/acuite_monthly_inc_trend_20260622.csv"
monthly_trend.to_csv(monthly_trend_path, index=False)
print(f"  Saved: {monthly_trend_path} ({len(monthly_trend):,} rows)")

# ─────────────────────────────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════
# TASK 2: FEB 2026 CARE COHORT TARGETING
# ══════════════════════════════════════════════════════════════════════════════
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("TASK 2: FEB 2026 CARE COHORT — TARGETED CALL LIST")
print("=" * 70)

care_inc_all = valid_d365[(valid_d365["Agency"] == "CARE") & valid_d365["is_INC"]].copy()
care_inc_all["Month_Str"] = care_inc_all["Rating_Date"].dt.to_period("M").astype(str)

care_feb = care_inc_all[care_inc_all["Month_Str"] == "2026-02"].copy()
print(f"  CARE INC records from Feb 2026:    {len(care_feb):,}")
print(f"  Unique companies:                  {care_feb['Company Name'].nunique():,}")

# Days since Feb 2026 (as of 2026-06-22)
# Feb 2026 = ~115-143 days ago
days_range = care_feb["Days_Since"].describe()
print(f"  Days since rating — min: {care_feb['Days_Since'].min():.0f}, max: {care_feb['Days_Since'].max():.0f}, mean: {care_feb['Days_Since'].mean():.0f}")

# Urgency breakdown
print(f"\n  Urgency breakdown:")
for urg, cnt in care_feb["Urgency"].value_counts().items():
    pct = cnt/len(care_feb)*100
    print(f"    {urg:<12}: {cnt:>5,} ({pct:.1f}%)")

# Instrument breakdown
print(f"\n  Instrument breakdown:")
inst_breakdown = care_feb.groupby("Instrument")["Company Name"].nunique().sort_values(ascending=False)
for inst, cnt in inst_breakdown.items():
    print(f"    {inst:<45}: {cnt:>5,}")

# Grade/Rating breakdown
print(f"\n  Grade/Risk breakdown:")
for grade, cnt in care_feb["Grade"].value_counts().items():
    print(f"    {grade:<30}: {cnt:>5,}")

# Build full call list
care_feb_out = care_feb.copy()
care_feb_out["Inferred_State"] = care_feb_out["Company Name"].apply(infer_state)

def care_feb_pitch(row):
    days = row["Days_Since"]
    inst = str(row["Instrument"])
    if days >= 180:
        urgency_msg = "120+ days overdue — prime window to approach before company gives up on ratings entirely"
    else:
        urgency_msg = "90-120 days INC — fresh enough that they remember the INC decision"
    return f"CARE INC since Feb 2026: {urgency_msg}. Instrument: {inst}. ACER can rerate quickly."

care_feb_out["Why_Target"] = care_feb_out.apply(
    lambda r: f"CARE INC Feb 2026 — {r['Days_Since']:.0f} days overdue; instrument: {r['Instrument']}", axis=1
)
care_feb_out["ACER_Pitch"] = care_feb_out.apply(care_feb_pitch, axis=1)

# Prioritize: longer overdue first, then by instrument (Term Loans > NCD > BG > LC)
inst_priority = {"Non-government debt": 1, "Term loans": 2, "Bank Guarantee": 3,
                 "Fund based financial facility/instrument": 4, "Letter of Credit": 5}
care_feb_out["Inst_Priority"] = care_feb_out["Instrument"].map(inst_priority).fillna(6)
care_feb_out = care_feb_out.sort_values(["Inst_Priority","Days_Since"], ascending=[True, False])

cols_out = ["Company Name","Rating_Date","Agency","Instrument","Grade","Rating",
            "Ammount","Days_Since","Urgency","Inferred_State","Why_Target","ACER_Pitch"]
care_feb_final = care_feb_out[cols_out].rename(columns={"Rating_Date":"Rating_Date_Parsed","Ammount":"Amount_Cr"})

care_feb_path = f"{SESSION_DIR}/care_feb2026_cohort_20260622.csv"
care_feb_final.to_csv(care_feb_path, index=False)
print(f"\n  Saved: {care_feb_path} ({len(care_feb_final):,} rows)")

# Cross-check: compare Feb 2026 to other months for context
print(f"\n  CARE INC monthly volumes (2026):")
care_2026 = care_inc_all[care_inc_all["Month_Str"] >= "2026-01"].copy()
for month, grp in care_2026.groupby("Month_Str"):
    n = grp["Company Name"].nunique()
    print(f"    {month}: {n:>5,} companies")

# ─────────────────────────────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════
# TASK 3: INFOMERICS ULTRA HOT × D365 MULTI-AGENCY CROSS-MATCH
# ══════════════════════════════════════════════════════════════════════════════
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("TASK 3: INFOMERICS ULTRA HOT × D365 MULTI-AGENCY CROSS-MATCH")
print("=" * 70)

info_inc = info[info["is_INC"]].copy()
info_ultra_hot = info_inc[info_inc["Urgency"] == "ULTRA HOT"].copy()
print(f"  Infomerics INC records:       {len(info_inc):,}")
print(f"  Infomerics INC unique companies: {info_inc['Company Name'].nunique():,}")
print(f"  Infomerics ULTRA HOT records: {len(info_ultra_hot):,}")
print(f"  Infomerics ULTRA HOT unique:  {info_ultra_hot['Company Name'].nunique():,}")

# Get all D365 companies
d365_companies = set(valid_d365["Company Name"].str.strip().str.upper())
print(f"\n  D365 unique companies: {len(d365_companies):,}")

# Normalize for matching
def normalize(name):
    if pd.isna(name):
        return ""
    n = str(name).upper().strip()
    # Remove common suffixes
    for suffix in [" PVT. LTD.", " PVT LTD", " PRIVATE LIMITED", " LIMITED",
                   " LTD.", " LTD", " PVT.", " CO.", " CORP.", " CORPORATION",
                   " INC.", " LLC", " & CO", " AND COMPANY"]:
        n = n.replace(suffix, "")
    # Remove special chars
    n = re.sub(r"[^A-Z0-9 ]", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    return n

info_ultra_hot["Normalized_Name"] = info_ultra_hot["Company Name"].apply(normalize)
d365_all_companies = valid_d365[["Company Name"]].drop_duplicates().copy()
d365_all_companies["Normalized_Name"] = d365_all_companies["Company Name"].apply(normalize)

# Build D365 lookup dict: normalized → original names list
d365_norm_dict = {}
for _, row in d365_all_companies.iterrows():
    key = row["Normalized_Name"]
    if key not in d365_norm_dict:
        d365_norm_dict[key] = []
    d365_norm_dict[key].append(row["Company Name"])

info_ultra_hot_unique = info_ultra_hot[["Company Name","Normalized_Name"]].drop_duplicates("Company Name")

# Exact match on normalized name
info_ultra_hot_unique["Exact_Match"] = info_ultra_hot_unique["Normalized_Name"].isin(d365_norm_dict)
exact_matches = info_ultra_hot_unique[info_ultra_hot_unique["Exact_Match"]].copy()
print(f"\n  Exact normalized matches: {len(exact_matches):,}")

# Fuzzy match: check if infomerics name is contained in a D365 name or vice versa
# Build a set of d365 normalized names for faster lookup
d365_norm_set = set(d365_norm_dict.keys())

def fuzzy_match(norm_name):
    if not norm_name or len(norm_name) < 4:
        return False, None
    # Check if norm_name is substring of any d365 company
    for d_name in d365_norm_set:
        if len(d_name) < 4:
            continue
        # Either direction containment (require at least 10 chars match)
        if norm_name in d_name and len(norm_name) >= 10:
            return True, d_name
        if d_name in norm_name and len(d_name) >= 10:
            return True, d_name
        # Word-by-word: at least 3 consecutive words match
        n_words = norm_name.split()
        d_words = d_name.split()
        if len(n_words) >= 3 and len(d_words) >= 3:
            n_str = " ".join(n_words[:3])
            d_str = " ".join(d_words[:3])
            if n_str == d_str and len(n_str) >= 8:
                return True, d_name
    return False, None

# Apply fuzzy matching to non-exact matches
non_exact = info_ultra_hot_unique[~info_ultra_hot_unique["Exact_Match"]].copy()
print(f"  Running fuzzy match on {len(non_exact):,} non-exact companies...")

fuzzy_results = non_exact["Normalized_Name"].apply(lambda n: fuzzy_match(n))
non_exact["Fuzzy_Match"] = fuzzy_results.apply(lambda x: x[0])
non_exact["Fuzzy_D365_Name"] = fuzzy_results.apply(lambda x: x[1])
fuzzy_hits = non_exact[non_exact["Fuzzy_Match"]].copy()
print(f"  Fuzzy matches found: {len(fuzzy_hits):,}")

# Combine exact + fuzzy
all_matched = pd.concat([
    exact_matches.assign(Match_Type="Exact", D365_Match_Name=None),
    fuzzy_hits.assign(Match_Type="Fuzzy", D365_Match_Name=fuzzy_hits["Fuzzy_D365_Name"])
], ignore_index=True)

print(f"\n  TOTAL INFOMERICS ULTRA HOT in D365: {len(all_matched):,} companies")
print(f"    Exact matches: {len(exact_matches):,}")
print(f"    Fuzzy matches: {len(fuzzy_hits):,}")

# For matched companies, pull their D365 records to get agency info
if len(all_matched) > 0:
    print(f"\n  Sample matched companies:")
    for _, row in all_matched.head(10).iterrows():
        print(f"    [{row['Match_Type']}] {row['Company Name']}")

# Build the full output — merge D365 data for matched companies
# For each matched Infomerics ULTRA HOT company, get their D365 agency footprint

# Get full infomerics data for matched companies
matched_names = set(all_matched["Company Name"].tolist())
info_matched = info_ultra_hot[info_ultra_hot["Company Name"].isin(matched_names)].copy()

# Get D365 data for matched companies (by normalized name lookup)
matched_d365_records = []
for _, row in all_matched.iterrows():
    company_name = row["Company Name"]
    norm = row["Normalized_Name"]

    # Get D365 company names that match
    if row["Match_Type"] == "Exact":
        d365_names = d365_norm_dict.get(norm, [])
    else:
        d365_fuzzy = row.get("Fuzzy_D365_Name") or row.get("D365_Match_Name")
        d365_names = d365_norm_dict.get(d365_fuzzy, []) if d365_fuzzy else []

    for d365_name in d365_names:
        d365_recs = valid_d365[valid_d365["Company Name"] == d365_name].copy()
        for _, d_row in d365_recs.iterrows():
            matched_d365_records.append({
                "Infomerics_Company": company_name,
                "D365_Company": d_row["Company Name"],
                "D365_Agency": d_row["Agency"],
                "D365_Instrument": d_row["Instrument"],
                "D365_Rating": d_row["Rating"],
                "D365_Rating_Date": d_row["Rating_Date"],
                "D365_is_INC": d_row["is_INC"],
                "D365_Days_Since": d_row["Days_Since"],
                "D365_Urgency": d_row["Urgency"],
                "Match_Type": row["Match_Type"]
            })

if matched_d365_records:
    matched_d365_df = pd.DataFrame(matched_d365_records)

    print(f"\n  D365 agency footprint for matched companies:")
    print(matched_d365_df["D365_Agency"].value_counts().to_string())

    print(f"\n  D365 INC status for matched companies:")
    print(matched_d365_df["D365_is_INC"].value_counts().to_string())

    # Find companies that are ALSO INC at D365 agencies
    d365_also_inc = matched_d365_df[matched_d365_df["D365_is_INC"]]["Infomerics_Company"].nunique()
    print(f"\n  Infomerics ULTRA HOT also INC at D365 agency: {d365_also_inc:,} companies")

# Build final output: Infomerics ULTRA HOT that appear in D365
info_ultra_hot_full = info_ultra_hot.copy()
info_ultra_hot_full["In_D365"] = info_ultra_hot_full["Company Name"].isin(matched_names)
info_ultra_hot_full["Match_Type"] = info_ultra_hot_full["Company Name"].apply(
    lambda x: "Exact" if x in set(exact_matches["Company Name"])
    else ("Fuzzy" if x in set(fuzzy_hits["Company Name"]) else "No Match")
)

# Add D365 agency summary for matched
if matched_d365_records:
    agency_summary = (
        pd.DataFrame(matched_d365_records)
        .groupby("Infomerics_Company")
        .apply(lambda df: ", ".join(sorted(set(df["D365_Agency"]))))
        .reset_index()
        .rename(columns={"Infomerics_Company":"Company Name", 0:"D365_Agencies"})
    )
    info_ultra_hot_full = info_ultra_hot_full.merge(agency_summary, on="Company Name", how="left")

    d365_inc_summary = (
        pd.DataFrame(matched_d365_records)
        .groupby("Infomerics_Company")
        .apply(lambda df: "YES" if df["D365_is_INC"].any() else "NO")
        .reset_index()
        .rename(columns={"Infomerics_Company":"Company Name", 0:"D365_Also_INC"})
    )
    info_ultra_hot_full = info_ultra_hot_full.merge(d365_inc_summary, on="Company Name", how="left")
else:
    info_ultra_hot_full["D365_Agencies"] = "N/A"
    info_ultra_hot_full["D365_Also_INC"] = "N/A"

info_ultra_hot_full["D365_Agencies"] = info_ultra_hot_full["D365_Agencies"].fillna("Not in D365")
info_ultra_hot_full["D365_Also_INC"] = info_ultra_hot_full["D365_Also_INC"].fillna("Not in D365")

info_ultra_hot_full["Why_Target"] = info_ultra_hot_full.apply(
    lambda r: (
        f"ULTRA HOT ({r['Days_Since']:.0f} days overdue) + MULTI-AGENCY: also in D365 with {r['D365_Agencies']}"
        if r["In_D365"]
        else f"ULTRA HOT Infomerics-only ({r['Days_Since']:.0f} days overdue) — exclusive opportunity"
    ), axis=1
)
info_ultra_hot_full["ACER_Pitch"] = info_ultra_hot_full.apply(
    lambda r: (
        "MAXIMUM PRIORITY — INC at Infomerics + present at multiple D365 agencies. ACER can displace all current raters with single engagement."
        if r["In_D365"]
        else "Infomerics marked you non-cooperative — ACER offers a fresh start with faster analyst access."
    ), axis=1
)

# Sort: D365 matched companies first (highest priority), then by days_since
info_ultra_hot_full["Priority_Sort"] = info_ultra_hot_full["In_D365"].apply(lambda x: 0 if x else 1)
info_ultra_hot_full = info_ultra_hot_full.sort_values(["Priority_Sort","Days_Since"], ascending=[True, False])

final_cols = ["Company Name","Date","Instruments","Size","Current Ratings","Outlook",
              "Rating_Date","Days_Since","Urgency","In_D365","Match_Type",
              "D365_Agencies","D365_Also_INC","Why_Target","ACER_Pitch"]
info_uh_out = info_ultra_hot_full[final_cols].copy()

multiagency_path = f"{SESSION_DIR}/infomerics_ultrahot_multiagency_20260622.csv"
info_uh_out.to_csv(multiagency_path, index=False)
print(f"\n  Saved: {multiagency_path} ({len(info_uh_out):,} rows)")

# Also produce the subset: only D365 matched (highest priority)
matched_only = info_uh_out[info_uh_out["In_D365"]].copy()
matched_only_path = f"{SESSION_DIR}/infomerics_ultrahot_d365_matched_20260622.csv"
matched_only.to_csv(matched_only_path, index=False)
print(f"  Saved: {matched_only_path} ({len(matched_only):,} rows — D365-matched only)")

# ─────────────────────────────────────────────────────────────────────────────
# SUMMARY PRINT
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("SESSION 23 — SUMMARY")
print("=" * 70)

# TASK 1 summary
acuite_unique = acuite_inc["Company Name"].nunique()
acuite_uh = acuite_inc[acuite_inc["Urgency"]=="ULTRA HOT"]["Company Name"].nunique()
acuite_hot = acuite_inc[acuite_inc["Urgency"]=="HOT"]["Company Name"].nunique()
acuite_peak_row = trend_focus.loc[trend_focus["INC_Companies"].idxmax()] if len(trend_focus) > 0 else None

print(f"\n  TASK 1 — ACUITE 2026 Acceleration:")
print(f"    Total ACUITE INC companies: {acuite_unique:,}")
print(f"    ULTRA HOT: {acuite_uh:,} | HOT: {acuite_hot:,} | Callable now: {acuite_uh+acuite_hot:,}")
if acuite_peak_row is not None:
    print(f"    Peak month: {acuite_peak_row['Month_Str']} ({acuite_peak_row['INC_Companies']:,} companies, {acuite_peak_row['INC_Rate_Pct']:.1f}%)")
known_states = geo_breakdown[geo_breakdown["State"] != "Unknown"]["INC_Companies"].sum()
print(f"    Geo classified: {known_states:,} of {acuite_unique:,} ({known_states/acuite_unique*100:.1f}%)")
print(f"    Files: acuite_2026_acceleration_geo_20260622.csv + acuite_monthly_inc_trend_20260622.csv")

# TASK 2 summary
care_feb_unique = care_feb["Company Name"].nunique()
care_feb_uh = care_feb[care_feb["Urgency"]=="ULTRA HOT"]["Company Name"].nunique()
care_feb_hot = care_feb[care_feb["Urgency"]=="HOT"]["Company Name"].nunique()
care_feb_medium = care_feb[care_feb["Urgency"]=="MEDIUM"]["Company Name"].nunique()
print(f"\n  TASK 2 — Feb 2026 CARE Cohort:")
print(f"    Total CARE INC companies from Feb 2026: {care_feb_unique:,}")
print(f"    ULTRA HOT: {care_feb_uh:,} | HOT: {care_feb_hot:,} | MEDIUM: {care_feb_medium:,}")
top_inst = care_feb.groupby("Instrument")["Company Name"].nunique().sort_values(ascending=False).head(3)
print(f"    Top instruments: {', '.join([f'{k} ({v})' for k,v in top_inst.items()])}")
print(f"    File: care_feb2026_cohort_20260622.csv")

# TASK 3 summary
total_uh = info_ultra_hot["Company Name"].nunique()
matched_count = len(matched_names)
print(f"\n  TASK 3 — Infomerics ULTRA HOT × D365 Cross-Match:")
print(f"    Infomerics ULTRA HOT unique companies: {total_uh:,}")
print(f"    Found in D365: {matched_count:,} ({matched_count/total_uh*100:.1f}%)")
print(f"    Exact matches: {len(exact_matches):,} | Fuzzy matches: {len(fuzzy_hits):,}")
if matched_d365_records:
    d365_also_inc = len(set([r['Infomerics_Company'] for r in matched_d365_records if r['D365_is_INC']]))
    print(f"    Also INC at D365 agencies: {d365_also_inc:,}")
print(f"    Files: infomerics_ultrahot_multiagency_20260622.csv + infomerics_ultrahot_d365_matched_20260622.csv")

print("\n  All files saved to: intelligence_outputs/session_20260622/csv/")
print("\nSession 23 analysis complete.")
