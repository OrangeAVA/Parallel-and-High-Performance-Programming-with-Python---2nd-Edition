
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read Parquet").master("local[*]").getOrCreate()
df = spark.read.parquet("output")
df.show(truncate=False)
df.printSchema()

# SQL-style aggregation
df.createOrReplaceTempView("words")
result = spark.sql("SELECT word, SUM(count) as total FROM words GROUP BY word ORDER BY total DESC")
result.show()

spark.stop()

# Optional: Pandas & Dask
try:
    import pandas as pd
    pdf = pd.read_parquet("output")
    print("\nPandas head():")
    print(pdf.head())
except Exception as e:
    print("Pandas read_parquet skipped:", e)

try:
    import dask.dataframe as dd
    ddf = dd.read_parquet("output")
    print("\nDask head():")
    print(ddf.head())
except Exception as e:
    print("Dask read_parquet skipped:", e)
