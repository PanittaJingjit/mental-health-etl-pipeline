# 🧠 Mental Health ETL Pipeline

A production-grade ETL (Extract, Transform, Load) pipeline for processing employee mental health survey data — from raw CSV ingestion through cleaning, validation, feature engineering, and warehouse loading, fully orchestrated with Apache Airflow.

---

## 📁 Project Structure

```
mental_health_etl/
├── data/
│   ├── source/           # Original source CSV files
│   ├── raw/              # Timestamped raw snapshots (immutable)
│   ├── cleaned/          # Deduplicated and standardized data
│   ├── validated/        # Quality-checked data
│   └── transformed/      # Analytics-ready data with engineered features
├── ingest_mental_health_data.py
├── clean_mental_health_data.py
├── validate_mental_health_data.py
├── transform_mental_health_data.py
├── load_to_mysql.py
└── mental_health_etl_pipeline_dag.py
```

---

## 🔄 Pipeline Overview

Source CSV
↓
[1] Ingest      →  data/raw/
↓
[2] Clean       →  data/cleaned/
↓
[3] Validate    →  data/validated/
↓
[4] Transform   →  data/transformed/
↓
[5] Load        →  MySQL Warehouse (fact_employee_mental_health)

---

## 🗂️ Pipeline Stages

### 1. Ingestion — `ingest_mental_health_data.py`

Reads the source CSV and saves a timestamped snapshot into the raw layer.

- **Input:** `data/source/mental_health_2026.csv`
- **Output:** `data/raw/mental_health_raw_YYYYMMDD_HHMMSS.csv`

The raw layer is **immutable** — it acts as a source of truth for data recovery, audit tracking, and pipeline reprocessing.

---

### 2. Cleaning — `clean_mental_health_data.py`

Standardizes and cleans the raw dataset.

- **Input:** `data/raw/`
- **Output:** `data/cleaned/`

Tasks performed:

| Task | Description |
|------|-------------|
| Remove duplicates | Eliminates repeated records from ingestion or source bugs |
| Normalize columns | Converts headers to `snake_case` (e.g. `Work Mode` → `work_mode`) |
| Standardize categories | Unifies inconsistent values (e.g. `male`, `MALE`, ` Male` → `Male`) |

---

### 3. Validation — `validate_mental_health_data.py`

Checks data quality before loading into the warehouse. **Pipeline halts automatically if validation fails.**

- **Input:** `data/cleaned/`
- **Output:** `data/validated/`

Validation rules:

| Field | Valid Range |
|-------|-------------|
| `burnout_score` | 0 – 10 |
| `phq9_score` | 0 – 27 |
| `gad7_score` | 0 – 21 |
| `sleep_hours_per_night` | 0 – 24 |

---

### 4. Transformation — `transform_mental_health_data.py`

Performs feature engineering to create analytics-ready metrics.

- **Input:** `data/validated/`
- **Output:** `data/transformed/`

Engineered features:

| Feature | Logic | Purpose |
|---------|-------|---------|
| `burnout_risk_flag` | `burnout_score >= 7` | Flags high-risk employees |
| `sleep_deficit` | `8 - sleep_hours_per_night` | Measures sleep shortage vs. 8hr baseline |
| `wellbeing_index` | Composite of work-life balance, job satisfaction, social support, stress, burnout | Single KPI for overall employee wellbeing |

---

### 5. Load — `load_to_mysql.py`

Loads the transformed dataset into the MySQL data warehouse.

- **Input:** `data/transformed/`
- **Target Table:** `fact_employee_mental_health`

Uses SQLAlchemy to connect, auto-create the table if needed, and insert the data — enabling SQL analytics, BI dashboards, and ML model integration.

---

## ⚙️ Orchestration — Apache Airflow

**File:** `mental_health_etl_pipeline_dag.py`

Airflow manages the full pipeline as a DAG (Directed Acyclic Graph):

- Schedules pipeline runs automatically
- Enforces task dependencies
- Handles retries on failure
- Stops downstream tasks if any stage fails
- Provides full pipeline visibility via DAG UI

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Apache Airflow
- MySQL
- pandas, SQLAlchemy

### Installation

```bash
pip install pandas sqlalchemy apache-airflow pymysql
```

### Run Manually (without Airflow)

```bash
python ingest_mental_health_data.py
python clean_mental_health_data.py
python validate_mental_health_data.py
python transform_mental_health_data.py
python load_to_mysql.py
```

### Run with Airflow

```bash
# Copy the DAG file to your Airflow DAGs folder
cp mental_health_etl_pipeline_dag.py $AIRFLOW_HOME/dags/

# Start Airflow
airflow standalone
```

Then navigate to `http://localhost:8080` and trigger the `mental_health_etl_pipeline` DAG.

---

## 🏗️ Architecture

data/source/      →   Raw CSV files (never modified)
data/raw/         →   Immutable timestamped snapshots
data/cleaned/     →   Deduplicated, standardized data
data/validated/   →   Quality-checked, range-validated data
data/transformed/ →   Feature-engineered, analytics-ready data
MySQL Warehouse   →   Centralized storage for BI & analytics

---

## 📊 Warehouse Table

**Table:** `fact_employee_mental_health`

Key columns include original survey fields plus engineered features:
- `burnout_risk_flag` — boolean high-risk indicator
- `sleep_deficit` — hours below recommended sleep
- `wellbeing_index` — composite wellness score

---

## 📌 Design Principles

- **Immutable raw layer** — source data is never modified
- **Fail-fast validation** — bad data stops the pipeline before it reaches the warehouse
- **Reproducibility** — timestamped snapshots enable full pipeline replay
- **Separation of concerns** — each stage has a single, well-defined responsibility

---

## 📄 License

MIT License
