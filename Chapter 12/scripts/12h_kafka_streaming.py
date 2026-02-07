
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, current_timestamp, window

spark = (SparkSession.builder
    .appName("Kafka Structured Streaming")
    .config("spark.jars.packages","org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4")
    .master("local[*]")
    .getOrCreate())

spark.sparkContext.setLogLevel("WARN")

kafka_df = (spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers","localhost:9092")
    .option("subscribe","word_topic")
    .load())

lines = kafka_df.selectExpr("CAST(value AS STRING)")
words = (lines.withColumn("timestamp", current_timestamp())
    .select(explode(split(lines.value," ")).alias("word"), "timestamp"))

counts = (words
    .withWatermark("timestamp","10 seconds")
    .groupBy(window("timestamp","1 minute"), "word")
    .count())

query = (counts.writeStream
    .outputMode("append")
    .format("parquet")
    .option("checkpointLocation","checkpoints")
    .option("path","output")
    .start())

query.awaitTermination(300)
spark.stop()
