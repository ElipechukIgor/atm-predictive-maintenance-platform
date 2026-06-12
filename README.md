# ATM Predictive Maintenance Platform

![AWS](https://img.shields.io/badge/AWS-S3-orange)
![Kafka](https://img.shields.io/badge/Kafka-Streaming-black)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-blue)
![Databricks](https://img.shields.io/badge/Databricks-Lakehouse-red)
![PySpark](https://img.shields.io/badge/PySpark-Data_Engineering-orange)

---

## Project Overview

Real-time Data Engineering Platform for ATM monitoring and predictive maintenance.

This project simulates an enterprise-grade streaming architecture using Apache Kafka, Apache Airflow, AWS S3, Databricks and Delta Lake.

The platform ingests ATM telemetry events, stores them in AWS S3, orchestrates processing with Airflow and generates business-ready analytics in Databricks.

---

## Business Problem

Banks operate thousands of ATMs distributed across different cities.

Unexpected failures can cause:

- Service interruption
- Customer dissatisfaction
- Operational costs
- Revenue loss

The objective of this platform is to identify operational anomalies before failures occur.

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
Dashboard & Analytics
