# ATM Predictive Maintenance Platform

![AWS](https://img.shields.io/badge/AWS-S3-orange)
![Kafka](https://img.shields.io/badge/Kafka-Streaming-black)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-blue)
![Databricks](https://img.shields.io/badge/Databricks-Lakehouse-red)
![PySpark](https://img.shields.io/badge/PySpark-Data_Engineering-orange)
![Delta Lake](https://img.shields.io/badge/Delta_Lake-Storage-green)

---

## 🚀 Project Overview

The ATM Predictive Maintenance Platform is an end-to-end Data Engineering project that simulates a real-world banking environment for ATM monitoring and predictive maintenance.

The platform continuously generates ATM telemetry events, streams them through Apache Kafka, orchestrates ingestion with Apache Airflow, stores raw data in AWS S3, and processes business-ready analytics using Databricks Lakehouse Architecture.

This project demonstrates modern Data Engineering practices including:

- Streaming Data Pipelines
- Data Lakehouse Architecture
- Cloud Data Storage
- Workflow Orchestration
- Data Quality
- Bronze / Silver / Gold Layers
- Business Analytics

---

## 🎯 Business Problem

Banks operate thousands of ATMs distributed across multiple cities and states.

Unexpected ATM failures may result in:

- Service interruptions
- Customer dissatisfaction
- Operational inefficiencies
- Increased maintenance costs
- Revenue loss

This platform enables proactive monitoring and predictive maintenance by identifying operational anomalies before critical failures occur.

---

## 🏗️ Architecture

```text
ATM Telemetry Producer
          │
          ▼
     Apache Kafka
          │
          ▼
    Apache Airflow
          │
          ▼
        AWS S3
          │
          ▼
Databricks Bronze Layer
          │
          ▼
Databricks Silver Layer
          │
          ▼
Databricks Gold Layer
          │
          ▼
Business Dashboard
```

---

## 📊 End-to-End Data Flow

### 1. Event Generation

A Python Producer simulates ATM telemetry data including:

- Temperature
- CPU Usage
- Cash Level
- Network Latency
- Operational Status
- Event Timestamp

---

### 2. Kafka Streaming

Events are published to Kafka topics in real time.

Examples:

```json
{
  "atm_id": "ATM_1001",
  "city": "Curitiba",
  "state": "PR",
  "temperature": 84,
  "cpu_usage": 92,
  "cash_level": 14,
  "network_latency_ms": 250,
  "status": "CRITICAL",
  "event_time": "2026-06-07T23:18:00"
}
```

---

### 3. Airflow Orchestration

Apache Airflow orchestrates ingestion workflows and automates movement of streaming files into AWS S3.

---

### 4. AWS S3 Landing Zone

Raw telemetry data is stored in S3 as the system's landing zone.

```text
s3://atm-predictive-maintenance/
│
├── raw/
├── processed/
└── archive/
```

---

### 5. Databricks Bronze Layer

Raw events are ingested into Delta tables.

Responsibilities:

- Schema capture
- Raw data preservation
- Historical storage

---

### 6. Databricks Silver Layer

Data cleansing and enrichment.

Responsibilities:

- Data quality validation
- Type conversions
- Null handling
- Feature engineering
- Business rule enforcement

---

### 7. Databricks Gold Layer

Business-ready datasets.

Generated tables:

### atm_health_summary

ATM-level operational metrics.

### city_failure_summary

Failure aggregation by city.

### atm_critical_ranking

Critical ATM ranking.

---

## 📂 Repository Structure

```text
atm-predictive-maintenance-platform/
│
├── airflow/
│   ├── dags/
│   │   └── atm_airflow_s3_pipeline.py
│   └── docker-compose.yml
│
├── consumer/
│   └── 02_kafka_to_s3.py
│
├── producer/
│   └── atm_producer.py
│
├── notebooks/
│   ├── 01_bronze_ingestion.py
│   ├── 02_silver_transformations.py
│   ├── 03_gold_kpis.py
│   └── 04_dashboard_queries.sql
│
├── datalake/
│
├── docs/
│   ├── airflow_pipeline.md
│   ├── dashboard.md
│   ├── gold_tables.md
│   └── s3_ingestion.md
│
├── images/
│   ├── airflow_pipeline.png
│   ├── dashboard.png
│   ├── gold_tables.png
│   └── s3_ingestion.png
│
├── infra/
│   └── docker-compose.yml
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🛠️ Technology Stack

### Streaming

- Apache Kafka
- Kafka Producer

### Workflow Orchestration

- Apache Airflow

### Cloud

- AWS S3

### Processing

- Databricks
- Apache Spark
- PySpark

### Storage

- Delta Lake

### Programming

- Python
- SQL

### Analytics

- Databricks Dashboards

---

## 📈 Dashboard KPIs

The Databricks dashboard provides operational visibility into ATM health metrics.

### Total ATM Events

Total telemetry events processed.

### Failure Events

Total ATM failures detected.

### High Temperature Alerts

ATMs operating above safe temperature thresholds.

### Low Cash Alerts

ATMs requiring cash replenishment.

### Failures by City

Failure distribution across cities.

### Top Critical ATMs

Ranking of the most problematic ATMs.

---

## 📷 Dashboard

> Replace this image with your dashboard screenshot.

```markdown
![Dashboard](images/dashboard.png)
```

---

## 📷 Gold Analytics Tables

> Replace this image with your Gold Layer screenshot.

```markdown
![Gold Tables](images/gold_tables.png)
```

---

## 📷 Airflow Pipeline

> Replace this image with your Airflow DAG screenshot.

```markdown
![Airflow Pipeline](images/airflow_pipeline.png)
```

---

## 📷 S3 Data Ingestion

> Replace this image with your AWS S3 ingestion screenshot.

```markdown
![S3 Ingestion](images/s3_ingestion.png)
```

---

## 📊 Gold Layer Tables

### atm_health_summary

Tracks ATM health indicators.

| Column | Description |
|----------|-------------|
| atm_id | ATM identifier |
| city | ATM city |
| state | ATM state |
| total_events | Total telemetry events |
| failure_events | Failure count |
| high_temperature_events | High temperature occurrences |
| high_cpu_events | High CPU usage occurrences |
| low_cash_events | Low cash occurrences |

---

### city_failure_summary

Aggregated failures by city.

| Column | Description |
|----------|-------------|
| city | City |
| state | State |
| total_events | Total events |
| total_atms | Number of ATMs |
| failure_events | Failure count |

---

### atm_critical_ranking

Ranks the most critical ATMs.

| Column | Description |
|----------|-------------|
| atm_id | ATM identifier |
| failure_events | Failure count |
| risk_score | Risk indicator |

---

## 🎯 Skills Demonstrated

This project demonstrates hands-on experience with:

- Data Engineering
- Data Lakehouse Architecture
- Streaming Data Pipelines
- Apache Kafka
- Apache Airflow
- AWS S3
- Databricks
- Delta Lake
- PySpark
- SQL Analytics
- Dashboard Development
- Data Quality Engineering
- Cloud Data Platforms

---

## 🔮 Future Improvements

- Spark Structured Streaming
- Predictive Machine Learning Models
- CI/CD Pipeline
- Infrastructure as Code
- Monitoring and Alerting
- Automated Data Quality Checks

---

## 👨‍💻 Author

### Igor Elipechuk

Data Engineer | AWS | Databricks | PySpark

**LinkedIn**

https://www.linkedin.com/in/igor-elipechuk

**GitHub**

https://github.com/ElipechukIgor

---

⭐ If you found this project useful, consider giving it a star.
