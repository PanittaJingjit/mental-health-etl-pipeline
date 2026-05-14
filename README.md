# Mental Health ETL Pipeline with Airflow 
## Project Overview 
This project is an end-to-end ETL (Extract, Transform, Load) pipeline built using: 
- Apache Airflow 
- Python 
- Pandas 
- MySQL 
- Docker 

The pipeline processes a mental health and burnout dataset of 100,000 tech workers and transforms raw CSV data into an analytics-ready data warehouse table. 

The objective of this project is to simulate a real-world Data Engineering workflow including: 
- data ingestion 
- data cleaning 
- data validation 
- feature engineering 
- warehouse loading 
- orchestration with Airflow 

--- 

# Dataset 
Dataset Source: 
Mental Health and Burnout in Tech Workers 2026 
The dataset contains information about: 
- employee demographics 
- burnout levels 
- stress scores 
- sleep habits 
- therapy access 
- work-life balance 
- anxiety and depression indicators 
- workplace conditions 
Total Rows: 
- 100,000 records 
Total Columns: 
- 33 columns 
--- 
# Tech Stack 
| Tool | Purpose | 
|---|---| 
| Python | ETL scripting | 
| Pandas | Data processing | 
| Airflow | Workflow orchestration | 
| Docker | Containerized infrastructure | 
| MySQL | Data warehouse | 
| SQLAlchemy | Database connection | 
| Great Expectations | Data validation | 
| VS Code SQLTools | SQL querying | 
--- 
# Project Architecture 
```text 
Kaggle Dataset 
↓ 
Ingestion Layer 
↓ 
Raw Data Layer 
↓ 
Cleaning Layer 
↓ 
Validation Layer 
↓ 
Transformation Layer 
↓ 
MySQL Data Warehouse 
↓ 
Analytics / SQL Queries