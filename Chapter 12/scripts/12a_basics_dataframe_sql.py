
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PySpark Basics").master("local[*]").getOrCreate()

data = [("Alice", 29, "Rome"),
        ("Bob", 35, "Milan"),
        ("Cathy", 23, "Naples"),
        ("David", 40, "Venice")]
columns = ["Name", "Age", "City"]
df = spark.createDataFrame(data, schema=columns)

print("DataFrame schema:")
df.printSchema()
print("\nDataFrame content:")
df.show()

print("\nFilter Age > 30:")
df.filter(df["Age"] > 30).show()

print("\nGroup by City, avg Age:")
df.groupBy("City").avg("Age").show()

print("\nOrder by Age desc:")
df.orderBy(df["Age"].desc()).show()

# SQL
df.createOrReplaceTempView("citizens")
print("\nSQL: Age > 30")
spark.sql("SELECT Name, Age, City FROM citizens WHERE Age > 30").show()

print("\nSQL: AVG(Age) by City")
spark.sql("SELECT City, AVG(Age) AS AvgAge FROM citizens GROUP BY City").show()

print("\nSQL: ORDER BY Age DESC")
spark.sql("SELECT * FROM citizens ORDER BY Age DESC").show()

spark.stop()
