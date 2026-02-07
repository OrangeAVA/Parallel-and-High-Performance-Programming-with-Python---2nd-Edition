
# Chapter 12 — PySpark (Code & Notebooks)

This package contains runnable **scripts** and **Jupyter notebooks** that mirror the examples in Chapter 12.

> ⚠️ Most examples are designed for **Linux** (Ubuntu-like). On macOS they usually work; on Windows use WSL2 or Docker.

## Prerequisites

- **Java JDK 8+** (Spark 3.5 works well with Java 11; Java 21 also works). Example on Ubuntu:
  ```bash
  sudo apt-get update && sudo apt-get install -y openjdk-21-jdk
  echo 'JAVA_HOME="/usr/lib/jvm/java-21-openjdk-amd64"' | sudo tee -a /etc/environment
  source /etc/environment
  ```
- **Python 3.9+** and a virtual env:
  ```bash
  python3 -m venv pyspark-env
  source pyspark-env/bin/activate
  pip install -U pip
  ```
- **PySpark** and utilities:
  ```bash
  pip install pyspark==3.5.4 pandas pyarrow dask[dataframe] graphframes
  ```
  > The `graphframes` Python wrapper still requires the **GraphFrames JAR** (see below).

### Spark UI
When a Spark app is running locally, the UI is at http://localhost:4040

## Kafka (optional sections)

- Download Apache Kafka (e.g. 3.9.0) and run **ZooKeeper** and the **Broker** in two terminals.
- Create topic: `kafka-topics.sh --create --topic word_topic --bootstrap-server localhost:9092`
- Producer: `kafka-console-producer.sh --topic word_topic --bootstrap-server localhost:9092`

**Spark <-> Kafka package** is auto-fetched in the examples via:
```
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4
```
(Scala 2.12 line; adjust if your Spark uses another Scala version).

## GraphFrames JAR
Download the GraphFrames JAR that matches your Spark/Scala (example):
```
wget https://repos.spark-packages.org/graphframes/graphframes/0.8.4-spark3.5-s_2.12/graphframes-0.8.4-spark3.5-s_2.12.jar -O jars/graphframes-0.8.4-spark3.5-s_2.12.jar
```
Run scripts with:
```
spark-submit --jars jars/graphframes-0.8.4-spark3.5-s_2.12.jar scripts/12i_graphframes_pagerank.py
```

## Layout

- **notebooks/** — Jupyter notebooks mirroring the chapter
- **scripts/** — Python scripts runnable with `python` or `spark-submit`
- **data/** — small CSV used by examples
- **output/**, **checkpoints/** — write destinations for streaming examples

## Quick starts

### 1) Basic DataFrame & SQL
```bash
python scripts/12a_basics_dataframe_sql.py
```

### 2) RDD Word Count
```bash
python scripts/12b_rdd_wordcount.py
```

### 3) MLlib Logistic Regression
```bash
python scripts/12c_mllib_logreg.py
```

### 4) Optimizations (partitioning, cache, broadcast, combineByKey)
```bash
python scripts/12d_optimizations.py
```

### 5) Structured Streaming (socket -> console)
Terminal A:
```bash
nc -lk 9999
```
Terminal B:
```bash
python scripts/12e_stream_socket_console.py
```

### 6) Structured Streaming (socket -> Parquet)
```bash
rm -rf output checkpoints && mkdir output checkpoints
python scripts/12f_stream_socket_parquet.py
python scripts/12g_read_parquet.py
```

### 7) Kafka Structured Streaming
Start Kafka (ZooKeeper + Broker), create topic `word_topic`, then:
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4 scripts/12h_kafka_streaming.py
```

### 8) GraphFrames (PageRank)
```bash
spark-submit --jars jars/graphframes-0.8.4-spark3.5-s_2.12.jar scripts/12i_graphframes_pagerank.py
```

## Notes
- Switch `.master("local[*]")` to your cluster master URL (e.g. `spark://<HOST>:7077`) when running on a cluster.
- For S3/HDFS sinks, see inline comments in the scripts.
