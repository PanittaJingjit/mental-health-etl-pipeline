import pandas as pd
from sqlalchemy import create_engine

BASE_PATH = "/opt/airflow/data"

df = pd.read_csv(
    f"{BASE_PATH}/transformed/transformed_data.csv"
)

print("Loading into MySQL warehouse...")

engine = create_engine(
    "mysql+pymysql://airflow:airflow@mysql:3306/mental_health_db"
)

df.to_sql(
    "fact_employee_mental_health",
    engine,
    if_exists="replace",
    index=False
)

print("Warehouse loading completed")