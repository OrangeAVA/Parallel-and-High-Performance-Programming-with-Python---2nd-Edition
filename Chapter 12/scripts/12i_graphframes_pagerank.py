
from pyspark.sql import SparkSession
from graphframes import GraphFrame

spark = SparkSession.builder.appName("GraphFrames PageRank").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

vertices = spark.createDataFrame([
    ("1", "Robert"),
    ("2", "Jean"),
    ("3", "Joe"),
    ("4", "David"),
    ("5", "Martin"),
    ("6", "Grace"),
    ("7", "Jessica"),
    ("8", "Mike")
], ["id", "name"])

edges = spark.createDataFrame([
    ("1", "2", "friends"),
    ("2", "3", "colleagues"),
    ("3", "4", "family"),
    ("4", "1", "friends"),
    ("5", "1", "friends"),
    ("5", "3", "colleagues"),
    ("6", "3", "family"),
    ("6", "7", "friends"),
    ("7", "5", "colleagues"),
    ("8", "6", "friends"),
    ("8", "7", "family"),
    ("2", "8", "colleagues")
], ["src", "dst", "relationship"])

g = GraphFrame(vertices, edges)

print("Vertices:"); g.vertices.show()
print("Edges:"); g.edges.show()

pr = g.pageRank(resetProbability=0.15, maxIter=10)
print("PageRank:"); pr.vertices.orderBy("pagerank", ascending=False).show()

spark.stop()
