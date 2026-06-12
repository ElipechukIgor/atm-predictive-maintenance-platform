# ATM Predictive Maintenance Platform

![AWS](https://img.shields.io/badge/AWS-S3-orange)
![Kafka](https://img.shields.io/badge/Kafka-Streaming-black)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-blue)
![Databricks](https://img.shields.io/badge/Databricks-Lakehouse-red)
![PySpark](https://img.shields.io/badge/PySpark-Data_Engineering-orange)
![Delta Lake](https://img.shields.io/badge/Delta_Lake-Storage-green)

---

## Project Overview

Real-time Data Engineering Platform for ATM monitoring and predictive maintenance.

This project simulates an enterprise-grade streaming architecture using Apache Kafka, Apache Airflow, AWS S3, Databricks and Delta Lake.

The platform ingests ATM telemetry events, stores them in AWS S3, orchestrates processing with Airflow and generates business-ready analytics in Databricks.

---

## Business Problem

Banks operate thousands of ATMs distributed across multiple cities.

Unexpected ATM failures can result in:

- Service interruptions
- Customer dissatisfaction
- Increased maintenance costs
- Operational inefficiencies

This platform demonstrates how modern Data Engineering architectures can proactively identify ATM anomalies before critical failures occur.

---

## Architecture

```text
ATM Producer
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
Databricks Bronze
      │
      ▼
Databricks Silver
      │
      ▼
Databricks Gold
      │
      ▼
Business Dashboard
```

---

## Architecture Diagram

![Architecture](docs/images/airflow_pipeline.png)

---

## Dashboard

![Dashboard](docs/images/dashboard.png)

---

## Gold Analytics Tables

![Gold Tables](docs/images/gold_tables.png)

---

## S3 Data Ingestion

![S3 Ingestion](docs/images/s3_ingestion.png)

---

## Technology Stack

### Streaming

- Apache Kafka
- Kafka Producer

### Orchestration

- Apache Airflow

### Cloud

- AWS S3

### Processing

- Databricks
- Apache Spark
- PySpark

### Storage

- Delta Lake

### Analytics

- SQL
- Databricks Dashboards

---

## Data Pipeline

### Bronze Layer

Raw ATM telemetry ingestion.

Examples:

- temperature
- cpu_usage
- cash_level
- network_latency_ms
- status
- event_time

---

### Silver Layer

Data cleansing and enrichment.

Transformations:

- Schema enforcement
- Data quality validation
- Null handling
- Business rule application

---

### Gold Layer

Business-ready datasets.

Generated tables:

### atm_health_summary

ATM operational metrics.

### city_failure_summary

Failure aggregation by city.

### atm_critical_ranking

Ranking of critical ATMs.

---

## Dashboard KPIs

### Total ATM Events

Total telemetry events processed.

### Failure Events

Detected ATM failures.

### High Temperature Alerts

ATMs exceeding temperature thresholds.

### Low Cash Alerts

ATMs requiring replenishment.

### Failures by City

Operational failures aggregated by city.

### Top Critical ATMs

Ranking of ATMs with the highest failure rate.

---

## Repository Structure

```text
atm-predictive-maintenance-platform/
│
├── airflow/
│   ├── dags/
│   │   └── atm_airflow_s3_pipeline.py
│   └── docker-compose.yml
│
├── producer/
│   └── atm_producer.py
│
├── consumer/
│   └── 02_kafka_to_s3.py
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
│   ├── s3_ingestion.md
│   └── images/
│       ├── airflow_pipeline.png
│       ├── dashboard.png
│       ├── gold_tables.png
│       └── s3_ingestion.png
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

## Skills Demonstrated

- Data Engineering
- Streaming Data Pipelines
- Apache Kafka
- Apache Airflow
- AWS S3
- Databricks
- Delta Lake
- PySpark
- SQL Analytics
- Data Quality
- Dashboard Development
- Lakehouse Architecture

---

## Future Improvements

- Spark Structured Streaming
- Machine Learning Failure Prediction
- CI/CD Pipeline
- Infrastructure as Code
- Monitoring and Alerting

---

## Release

Current Release:

```text
v1.0.0
```

Published on GitHub Releases.

---

## Author

### Igor Elipechuk

Data Engineer | AWS | Databricks | PySpark

LinkedIn:

https://www.linkedin.com/in/igor-elipechuk

GitHub:

https://github.com/ElipechukIgor

---

⭐ If you found this project useful, consider giving it a star.
