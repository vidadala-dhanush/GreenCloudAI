import pandas as pd
from backend.greencloud_ai import analyze_cloud_data

df = pd.read_csv("dataset/cloud_usage.csv")

result = analyze_cloud_data(df)

print(result.head())