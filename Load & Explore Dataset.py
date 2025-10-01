import pandas as pd

# Load the metadata file 
df = pd.read_csv("metadata.csv")

# Quick exploration
print(df.head())
print(df.info())
print(df.describe(include='all'))