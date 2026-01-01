import pandas as pd
import numpy as np

df = pd.DataFrame({
    "team1": ["Alice", "Bob", "Charlie",'KD'],
    "team2": ['RAM', "VK", "RS","KL"],
    'winner': ['Alice','VK','RS','dw']
})
print(df)
print()
# print(df.loc[df["std"] > 2])
# print()
# print(df.loc[df["std"] >= 1,'std'])
# print()
# df.loc[df["Name"] == "Alice", "Age"] = 26
# print(df)
#    df.loc[:,"Country"] = ["USA", "UK", "Canada"]
# df['winner_flag'] = np.nan
df.loc[df['winner'] == df['team1'], 'winner_flag'] = 1
df.loc[df["winner"] == df["team2"], "winner_flag"]= -1
print()
print(df)