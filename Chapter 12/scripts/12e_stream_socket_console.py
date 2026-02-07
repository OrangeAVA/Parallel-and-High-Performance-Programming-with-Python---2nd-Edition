
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

spark = SparkSession.builder.appName("Structured Streaming Console").master("local[*]").getOrCreate()

lines = (spark.readStream
    .format("socket")
    .option("host","localhost")
    .option("port", 9999)
    .load())

words = lines.select(explode(split(lines.value, " ")).alias("word"))
counts = words.groupBy("word").count()

query = (counts.writeStream
    .outputMode("complete")
    .format("console")
    .start())

query.awaitTermination(60)
spark.stop()
