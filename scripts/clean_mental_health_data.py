import pandas as pd
import glob
import os

BASE_PATH = "/opt/airflow/data"

os.makedirs(
    f"{BASE_PATH}/cleaned",
    exist_ok=True
)

raw_files = glob.glob(
    f"{BASE_PATH}/raw/*.csv"
)

latest_file = max(
    raw_files,
    key=os.path.getctime
)

df = pd.read_csv(latest_file)

print("Cleaning data...")

df.drop_duplicates(inplace=True)

df.columns = [
    col.strip().lower()
    for col in df.columns
]

categorical_cols = [
    "gender",
    "country",
    "job_role",
    "industry",
    "work_mode"
]

for col in categorical_cols:

    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .str.title()
    )

cleaned_path = (
    f"{BASE_PATH}/cleaned/cleaned_data.csv"
)

df.to_csv(cleaned_path, index=False)

print("Cleaning completed")