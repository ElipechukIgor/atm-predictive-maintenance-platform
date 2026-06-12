# Bronze Layer
# Kafka -> AWS S3 -> Databricks Bronze

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.json("s3://atm-monitoring/raw/")

df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("atm_bronze")
