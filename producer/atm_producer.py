from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime, timezone

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value, ensure_ascii=False).encode("utf-8")
)

atm_ids = ["ATM_1001", "ATM_1002", "ATM_1003", "ATM_1004", "ATM_1005"]
cities = ["Curitiba", "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre"]
states = {
    "Curitiba": "PR",
    "São Paulo": "SP",
    "Rio de Janeiro": "RJ",
    "Belo Horizonte": "MG",
    "Porto Alegre": "RS"
}

def get_status(event):
    if event["temperature"] >= 80 or event["cpu_usage"] >= 90 or event["cash_level"] <= 10:
        return "CRITICAL"
    if event["temperature"] >= 70 or event["cpu_usage"] >= 80 or event["cash_level"] <= 20:
        return "WARNING"
    return "NORMAL"

while True:
    city = random.choice(cities)

    event = {
        "atm_id": random.choice(atm_ids),
        "city": city,
        "state": states[city],
        "temperature": round(random.uniform(25, 95), 2),
        "cpu_usage": round(random.uniform(10, 100), 2),
        "cash_level": random.randint(0, 100),
        "network_latency_ms": random.randint(10, 600),
        "event_time": datetime.now(timezone.utc).isoformat()
    }

    event["status"] = get_status(event)

    producer.send("atm_events", event)
    producer.flush()

    print(f"Sent event: {event}")

    time.sleep(2)
