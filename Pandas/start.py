import pandas as pd


matches_file_path = 'archive\\matches.csv'
df = pd.read_csv(matches_file_path)
### Find total wins per team
group_by = df.groupby(['winner']).size()
print(group_by)
#### Find the highest scoring match
# df['result_margin'].max()
# max_margin = df['target_runs'].max()
# print('Highest Scoring Match :',max_margin)
# print()
# print(df[df['result_margin'] == 146].shape)

### Step 12: Sort matches by date
# sorted_data = df.sort_values('date',ascending=False)
# print(sorted_data)
# print(df['date'])
# MI_Season_wins = df[df['winner']=='Mumbai Indians']
# print(MI_Season_wins['season'].value_counts())

# MI_wins = df[df['winner'] == 'Mumbai Indians']
# print(MI_wins.head())
# print(df['winner'].value_counts())  #from winner col how many time won by single team count

# print(df['method'].unique())
# df_dropna = df.dropna(axis='columns')
# print(df_dropna)  #remove null value col
# print(df.isnull().sum()) # it will give just count of null in col or row
# print(df.isnull())  #bool value True for null value
# print(df.notna())   ##bool value True for value
# print(df.notna().sum()) # it will give just count of value in col or row
# df.info()

# print(df.head())

# print(df.tail())
