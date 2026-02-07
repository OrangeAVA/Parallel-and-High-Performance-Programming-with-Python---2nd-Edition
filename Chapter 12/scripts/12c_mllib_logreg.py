
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

spark = SparkSession.builder.appName("MLlib Logistic Regression").master("local[*]").getOrCreate()

data = [
    (25, 30000, 1, 0),
    (35, 50000, 0, 1),
    (45, 100000, 1, 1),
    (22, 35000, 0, 0),
    (44, 60000, 1, 1),
    (33, 35000, 1, 1),
    (50, 22000, 0, 0),
    (30, 47000, 0, 1),
    (48, 50000, 1, 1),
]
columns = ["Age", "Salary", "Subscriber", "Purchased"]
df = spark.createDataFrame(data, schema=columns)

assembler = VectorAssembler(inputCols=["Age","Salary","Subscriber"], outputCol="features")
df2 = assembler.transform(df)

train, test = df2.randomSplit([0.8, 0.2], seed=42)

lr = LogisticRegression(featuresCol="features", labelCol="Purchased")
model = lr.fit(train)

pred = model.transform(test)
pred.select("features","Purchased","prediction","probability").show(truncate=False)

evaluator = BinaryClassificationEvaluator(labelCol="Purchased", rawPredictionCol="rawPrediction")
auc = evaluator.evaluate(pred)
print(f"AUC: {auc:.4f}")

spark.stop()
