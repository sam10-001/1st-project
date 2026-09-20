import pandas as pd
df = pd.read_csv("exoplanets.csv", comment="#") #tells pandas to ignore any line starting with #
print (df.head())
print(df.columns)
print(df.columns.tolist())
