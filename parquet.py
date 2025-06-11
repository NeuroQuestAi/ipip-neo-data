import pandas as pd

csv_path = "./datasets/refined/IPIP300-SCORES.csv.gz"
df = pd.read_csv(csv_path)

parquet_path = "./datasets/refined/IPIP300-SCORES.parquet"
df.to_parquet(parquet_path, engine="pyarrow", index=False)

print(f"Saved: {parquet_path}")

csv_path = "./datasets/refined/IPIP120-SCORES.csv.gz"
df = pd.read_csv(csv_path)

parquet_path = "./datasets/refined/IPIP120-SCORES.parquet"
df.to_parquet(parquet_path, engine="pyarrow", index=False)

print(f"Saved: {parquet_path}")
