'''Checklist (what we'll deliver)
Read CSV/Excel into a DataFrame.
Show shape, columns, dtypes, and first/last rows.
Count missing values by column and sample missing rows.
Convert date columns to datetime.
Basic value counts for categorical fields (teams, venues, toss_winner, result).
Derive simple helpful columns (season/year, match_day, winner_flag).
Save a cleaned snapshot (CSV) for downstream tasks.
'''
import pandas as pd
import numpy as np

input_path = 'archive\\matches.csv'

# 1. Read file (auto-detect excel/csv)
if input_path.lower().endswith(('.xls', '.xlsx')):
    df = pd.read_excel(input_path)
    # print(df)
else:
    df = pd.read_csv(input_path)
    # print(df)

# 2. Quick structure
print('Shape : ', df.shape)
print('Columns :\n', df.columns.tolist())
print('Dtypes:', df.dtypes)
print('**************************************************')

# 3. Peek at data
print("\nFirst 3 rows:")
print(df.head(3))
print("\nLast 3 rows:")
print(df.tail(3))
print('**************************************************')

# 4. Missing Value
missing = df.isna().sum().sort_values(ascending=True)
print('missing\n',missing.sum())
print('missing\n',missing)

if missing.sum() > 0:
    print("\nSample rows with any missing values:")
    print(df[df.isna().any(axis=1)].head(20))
print('**************************************************')

# 5. Convert date columns where appropriate
# Try common column names; adjust if your dataset uses different names.
date_candidates = [c for c in df.columns if 'date' in c.lower()]
print("\nDetected date candidate columns:", date_candidates)

for col in date_candidates:
    df[col] = pd.to_datetime(df[col],format='%d-%m-%Y' ,errors='coerce')
    print(f"Converted {col} -> {df[col].dtype}, nulls after conversion: {df[col].isna().sum()}")


# If there is a 'season' or 'year' field missing, derive from date if possible
if 'season' not in df.columns and date_candidates:
    # pick first date column
    dcol = date_candidates[0]
    df['season'] = df[dcol].dt.year
    print("\nDerived 'season' from", dcol)

    # 6. Basic value counts for key categorical columns
cat_cols = ['team1', 'team2', 'venue', 'toss_winner', 'winner', 'result']
existing = [c for c in cat_cols if c in df.columns]
print("\nValue counts for key columns:")
for c in existing:
    print(f"\nTop values for {c}:")
    print(df[c].value_counts().head(8))


# 7. Example derived columns
# winner_flag: 1 if team1 won, -1 if team2 won, 0 for tie/no result/unknown
if {'team1', 'team2', 'winner'}.issubset(df.columns):
    # df['winner_flag'] = np.nan
    df.loc[df['winner'] == df['team1'], 'winner_flag'] = 1
    df.loc[df['winner'] == df['team2'], 'winner_flag'] = -1
    df['match_day'] = df[date_candidates[0]].dt.day_name() if date_candidates else pd.NA
    print("\nAdded columns: 'winner_flag', 'match_day' (if date present)")

# 8. Save a cleaned snapshot for downstream tasks
output_snapshot = 'C:\\Python\\DemoPractice\\Pandas\\archive\\matches.csv'
df.to_csv(output_snapshot, index=True)
print(f"\nSnapshot saved to: {output_snapshot}")

# 9. Quick summary stats
print("\nNumeric summary:")
print(df.describe(include=[np.number]).T)
print("\nAll done for Task 1.")