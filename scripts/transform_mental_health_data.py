import pandas as pd
import os

BASE_PATH = "/opt/airflow/data"

os.makedirs(
    f"{BASE_PATH}/transformed",
    exist_ok=True
)

df = pd.read_csv(
    f"{BASE_PATH}/validated/validated_data.csv"
)

print("Transforming data...")

df["burnout_risk_flag"] = (
    df["burnout_score"] >= 7
)

df["sleep_deficit"] = (
    8 - df["sleep_hours_per_night"]
)

df["wellbeing_index"] = (
    df["work_life_balance_score"]
    + df["job_satisfaction_score"]
    + df["social_support_score"]
    - df["stress_score"]
    - df["burnout_score"]
)

transformed_path = (
    f"{BASE_PATH}/transformed/transformed_data.csv"
)

df.to_csv(transformed_path, index=False)

print("Transformation completed")