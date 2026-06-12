
from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="atm_airflow_s3_pipeline",
    description="Orchestrates Kafka consumer ingestion into AWS S3 for ATM predictive maintenance pipeline.",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["atm", "kafka", "s3", "airflow", "databricks"],
) as dag:

    start = EmptyOperator(
        task_id="start"
    )

    kafka_to_s3 = BashOperator(
        task_id="kafka_consumer_to_s3",
        bash_command="""
        echo "Starting Kafka consumer to S3 ingestion..."
        python /opt/project/consumer/02_kafka_to_s3.py
        echo "Kafka to S3 ingestion completed."
        """
    )

    validate_s3_upload = BashOperator(
        task_id="validate_s3_upload",
        bash_command="""
        echo "Validating S3 target path..."
        python - <<'PY'
import boto3

bucket = "atm-maintenance-streaming-igor-2026"
prefix = "raw/atm_events/"

s3 = boto3.client("s3")
response = s3.list_objects_v2(
    Bucket=bucket,
    Prefix=prefix,
    MaxKeys=10
)

if "Contents" not in response:
    raise Exception("No files found in S3 raw path.")

print("S3 validation successful.")
print(f"Bucket: {bucket}")
print(f"Prefix: {prefix}")
print(f"Files found: {len(response['Contents'])}")

for obj in response["Contents"]:
    print(obj["Key"])
PY
        """
    )

    run_bronze = BashOperator(
        task_id="run_bronze",
        bash_command="""
        echo "===================================="
        echo "DATBRICKS BRONZE"
        echo "Executar notebook:"
        echo "03_load_bronze_from_s3"
        echo "===================================="
        """
    )

    run_silver = BashOperator(
        task_id="run_silver",
        bash_command="""
        echo "===================================="
        echo "DATBRICKS SILVER"
        echo "Executar notebook:"
        echo "01_build_silver_atm_events"
        echo "===================================="
        """
    )

    run_gold = BashOperator(
       task_id="run_gold",
       bash_command="""
       echo "===================================="
       echo "DATBRICKS GOLD"
       echo "Executar notebook:"
       echo "01_build_gold_atm_kpis"
       echo "===================================="
       """
    )

    run_quality = BashOperator(
       task_id="run_quality",
       bash_command="""
       echo "===================================="
       echo "DATA QUALITY"
       echo "Verificar:"
       echo "- temperatura > 0"
       echo "- cpu_usage <= 100"
       echo "- cash_level >= 0"
       echo "- registros nulos"
       echo "===================================="
       """
    )

    end = EmptyOperator(
        task_id="end"
    )

    start >> kafka_to_s3 >> validate_s3_upload >> run_bronze >> run_silver >> run_gold >> run_quality >> end
