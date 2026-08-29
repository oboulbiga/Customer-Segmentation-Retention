import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

csv_path = BASE_DIR / "data" / "processed" / "online_retail_clean.csv"
db_path = BASE_DIR / "sql" / "online_retail.db"

print(f"Reading: {csv_path}")

df = pd.read_csv(csv_path)

print(f"Rows loaded from CSV: {len(df):,}")

conn = sqlite3.connect(db_path)

df.to_sql(
    "online_retail",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("SQLite database created successfully.")
print(f"Database: {db_path}")