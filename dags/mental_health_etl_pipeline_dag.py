from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2026, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="mental_health_etl_pipeline",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=["mental_health", "etl"],
) as dag:

    ingest_task = BashOperator(
        task_id="ingest_data",

        bash_command=(
            "python "
            "/opt/airflow/scripts/"
            "ingest_mental_health_data.py"
        ),
    )

    clean_task = BashOperator(
        task_id="clean_data",

        bash_command=(
            "python "
            "/opt/airflow/scripts/"
            "clean_mental_health_data.py"
        ),
    )

    validate_task = BashOperator(
        task_id="validate_data",

        bash_command=(
            "python "
            "/opt/airflow/scripts/"
            "validate_mental_health_data.py"
        ),
    )

    transform_task = BashOperator(
        task_id="transform_data",

        bash_command=(
            "python "
            "/opt/airflow/scripts/"
            "transform_mental_health_data.py"
        ),
    )

    load_task = BashOperator(
        task_id="load_warehouse",

        bash_command=(
            "python "
            "/opt/airflow/scripts/"
            "load_warehouse.py"
        ),
    )

    (
        ingest_task
        >> clean_task
        >> validate_task
        >> transform_task
        >> load_task
    )