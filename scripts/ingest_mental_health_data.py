import os
import pandas as pd
from datetime import datetime

BASE_PATH = "/opt/airflow/data"

SOURCE_FILE = (
    f"{BASE_PATH}/source/mental_health_2026.csv"
)

RAW_FOLDER = (
    f"{BASE_PATH}/raw"
)

os.makedirs(RAW_FOLDER, exist_ok=True)

print("Reading dataset...")

df = pd.read_csv(SOURCE_FILE)

print(f"Rows loaded: {len(df)}")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

output_file = (
    f"{RAW_FOLDER}/mental_health_raw_{timestamp}.csv"
)

df.to_csv(output_file, index=False)

print("Ingestion completed")