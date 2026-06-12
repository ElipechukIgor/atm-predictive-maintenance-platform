# Gold Layer
# Business KPIs

from pyspark.sql.functions import *

silver_df = spark.table("atm_silver")

gold_df = (
    silver_df
    .groupBy("city")
    .agg(
        count("*").alias("total_events"),
        sum("failure_events").alias("failure_events")
    )
)

gold_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("atm_gold_city_metrics")
