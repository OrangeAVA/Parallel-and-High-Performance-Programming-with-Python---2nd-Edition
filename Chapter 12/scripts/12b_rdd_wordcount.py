
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RDD WordCount").master("local[*]").getOrCreate()

lines = ["PySpark is powerful and fast",
         "Distributed computing is useful for large datasets",
         "PySpark supports parallel computing",
         "with Spark we can process large volumes of data"]

rdd = spark.sparkContext.parallelize(lines)

words = rdd.flatMap(lambda line: line.split(" "))
word_pairs = words.map(lambda w: (w.lower(), 1))
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

df_word_counts = word_counts.toDF(["Word", "Count"]).orderBy("Count", ascending=False)
df_word_counts.show(truncate=False)

spark.stop()
