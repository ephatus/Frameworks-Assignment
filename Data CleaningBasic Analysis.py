
import pandas as pd
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df = df.dropna(subset=['title', 'abstract', 'publish_time'])



# Papers by year
papers_per_year = df['publish_time'].dt.year.value_counts().sort_index()

# Top journals
top_journals = df['journal'].value_counts().head(10)
print("Papers per Year:\n", papers_per_year)