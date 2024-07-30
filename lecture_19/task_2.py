import pandas as pd

df = pd.read_csv('pandas.csv')
pd.rea

print(df[['Team', 'Yellow Cards',  'Red Cards']])
print(df.count().head(1))
print(df[df.Goals > 6])