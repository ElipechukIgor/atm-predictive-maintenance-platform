# Silver Layer
# Data Cleansing and Enrichment

from pyspark.sql.functions import *

bronze_df = spark.table("atm_bronze")

silver_df = (
    bronze_df
    .filter(col("atm_id").isNotNull())
    .withColumn(
        "temperature_status",
        when(col("temperature") > 80, "HIGH")
        .otherwise("NORMAL")
    )
)

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("atm_silver")
