from kafka import KafkaConsumer
import json
import pandas as pd
import boto3
import os
from io import BytesIO
from datetime import datetime, timezone

BUCKET_NAME = "atm-maintenance-streaming-igor-2026"
S3_PREFIX = "raw/atm_events"

consumer = KafkaConsumer(
    "atm_events",
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    group_id=None,
    value_deserializer=lambda value: json.loads(value.decode("utf-8")),
    consumer_timeout_ms=30000
)

s3_client = boto3.client("s3")

batch = []
batch_size = 20

print("Kafka → S3 iniciado. Pressione CTRL + C para parar.")

def upload_batch_to_s3(records):
    if not records:
        return

    now = datetime.now(timezone.utc)

    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    file_name = f"atm_events_{timestamp}.parquet"

    s3_key = f"{S3_PREFIX}/year={year}/month={month}/day={day}/{file_name}"

    df = pd.DataFrame(records)

    buffer = BytesIO()
    df.to_parquet(buffer, index=False)
    buffer.seek(0)

    s3_client.put_object(
        Bucket=BUCKET_NAME,
        Key=s3_key,
        Body=buffer.getvalue()
    )

    print(f"Arquivo enviado para S3: s3://{BUCKET_NAME}/{s3_key} | registros: {len(records)}")


try:
    for message in consumer:
        print("Mensagem recebida:", message.value)
        event = message.value

        event["kafka_topic"] = message.topic
        event["kafka_partition"] = message.partition
        event["kafka_offset"] = message.offset
        event["ingestion_timestamp"] = datetime.now(timezone.utc).isoformat()

        batch.append(event)

        if len(batch) >= batch_size:
            upload_batch_to_s3(batch)
            batch = []

except KeyboardInterrupt:
    if batch:
        upload_batch_to_s3(batch)

    print("Consumer finalizado.")
