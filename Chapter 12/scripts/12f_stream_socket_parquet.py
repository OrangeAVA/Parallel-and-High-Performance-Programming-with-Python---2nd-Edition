
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, current_timestamp, window

spark = SparkSession.builder.appName("Structured Streaming Parquet").master("local[*]").getOrCreate()

lines = (spark.readStream
    .format("socket")
    .option("host","localhost")
    .option("port", 9999)
    .load())

with_ts = lines.withColumn("timestamp", current_timestamp())
words = with_ts.select(explode(split(with_ts.value, " ")).alias("word"), "timestamp")

counts = (words
    .withWatermark("timestamp","10 seconds")
    .groupBy(window("timestamp","1 minute"), "word")
    .count())

query = (counts.writeStream
    .outputMode("append")  # requires watermark
    .format("parquet")
    .option("path","output")
    .option("checkpointLocation","checkpoints")
    .start())

query.awaitTermination(300)
spark.stop()
