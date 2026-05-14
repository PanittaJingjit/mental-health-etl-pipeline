import pandas as pd
import os

BASE_PATH = "/opt/airflow/data"

os.makedirs(
    f"{BASE_PATH}/validated",
    exist_ok=True
)

df = pd.read_csv(
    f"{BASE_PATH}/cleaned/cleaned_data.csv"
)

print("Validating dataset...")

assert (
    df["burnout_score"]
    .between(0, 10)
    .all()
)

assert (
    df["phq9_score"]
    .between(0, 27)
    .all()
)

assert (
    df["gad7_score"]
    .between(0, 21)
    .all()
)

assert (
    df["sleep_hours_per_night"]
    .between(0, 24)
    .all()
)

validated_path = (
    f"{BASE_PATH}/validated/validated_data.csv"
)

df.to_csv(validated_path, index=False)

print("Validation completed")