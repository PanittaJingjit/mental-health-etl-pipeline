FROM apache/airflow:2.9.1

USER airflow

RUN pip install --no-cache-dir \
    pandas \
    numpy \
    sqlalchemy==1.4.52 \
    pymysql \
    great-expectations \
    loguru

