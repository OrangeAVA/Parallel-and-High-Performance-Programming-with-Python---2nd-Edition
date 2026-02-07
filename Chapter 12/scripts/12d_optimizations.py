
from pyspark.sql import SparkSession, functions as F
from pyspark import StorageLevel

spark = SparkSession.builder.appName("Optimizations").master("local[*]").getOrCreate()

# RDD path
rdd = spark.sparkContext.textFile("data/transactions.csv")
header = rdd.first()
data = (rdd.filter(lambda r: r != header)
           .map(lambda r: r.split(","))
           .map(lambda c: (int(c[0]), float(c[1]))))

# Partitioning & Cache
data = data.repartition(4)
data.cache()

# Broadcast for filtering
vip_users = [1, 2]
b_vips = spark.sparkContext.broadcast(vip_users)
vip_data = data.filter(lambda x: x[0] in b_vips.value)

# combineByKey to sum and avg per user
user_totals = (vip_data.combineByKey(
                    lambda v: (v,1),
                    lambda acc, v: (acc[0]+v, acc[1]+1),
                    lambda a,b: (a[0]+b[0], a[1]+b[1])
                )
                .mapValues(lambda x:(x[0], x[0]/x[1])))

print("RDD results (VIP users only):")
print(user_totals.collect())

# DataFrame path
df = spark.read.format("csv").option("header","true").option("inferSchema","true").load("data/transactions.csv")
df.groupBy("user_id").agg(
    F.sum("amount").alias("total_amount"),
    F.avg("amount").alias("avg_amount")
).orderBy("user_id").show()

spark.stop()
