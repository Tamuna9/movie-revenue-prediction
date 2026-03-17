import pandas as pd

df = pd.read_csv("data/tmdb_5000_movies.csv")

print(df.head())
print()
print(df.columns.tolist())
print()
print(df.info())
