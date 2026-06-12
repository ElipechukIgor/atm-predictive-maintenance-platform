# ATM Predictive Maintenance Platform

![AWS](https://img.shields.io/badge/AWS-S3-orange)
![Kafka](https://img.shields.io/badge/Kafka-Streaming-black)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-blue)
![Databricks](https://img.shields.io/badge/Databricks-Lakehouse-red)
![PySpark](https://img.shields.io/badge/PySpark-Data%20Engineering-orange)

## Project Overview

Real-time Data Engineering Platform for ATM monitoring and predictive maintenance.

This project simulates an enterprise-grade streaming architecture using Apache Kafka, Apache Airflow, AWS S3, Databricks and Delta Lake.

The platform ingests ATM telemetry events, stores them in AWS S3, orchestrates processing with Airflow and generates business-ready analytics in Databricks.

---

## Architecture

```text
ATM Producer
      ↓
Apache Kafka
      ↓
Kafka Consumer
      ↓
AWS S3 (Raw Layer)
      ↓
Apache Airflow
      ↓
Databricks Bronze
      ↓
Databricks Silver
      ↓
Databricks Gold
      ↓
Operational Dashboard
```

---

## Technology Stack

- Python
- Apache Kafka
- Apache Airflow
- AWS S3
- Databricks
- PySpark
- Delta Lake
- SQL
- Docker

---

## Project Structure

```text
atm-predictive-maintenance-platform
│
├── airflow/
├── consumer/
├── producer/
├── datalake/
├── notebooks/
├── docs/
├── infra/
├── README.md
├── requirements.txt
└── .env.example
```

---

## Data Pipeline

### Bronze Layer

Raw ATM telemetry events.

### Silver Layer

Data cleansing and enrichment.

### Gold Layer

Business KPIs and operational metrics.

Generated tables:

- atm_health_summary
- atm_critical_ranking
- city_failure_summary
- atm_cash_replenishment

---

## Dashboard KPIs

- Total ATM Events
- Failure Events
- High Temperature Alerts
- Low Cash Alerts
- Failures by City
- Top Critical ATMs

---

## Documentation

Detailed documentation is available in:

- docs/airflow_pipeline.md
- docs/s3_ingestion.md
- docs/gold_tables.md
- docs/dashboard.md

---

## Future Improvements

- ML-based failure prediction
- Real-time alerting
- Databricks Workflows integration
- Infrastructure as Code (Terraform)

---

## Author

Igor Elipechuk

Data Engineer | AWS | Databricks | PySpark
