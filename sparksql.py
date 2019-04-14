from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
df = spark.read.json("/home/xuyou/spark-2.2.0-bin-hadoop2.7/examples/src/main/resources/people.json")
# Displays the content of the DataFrame to stdout
df.show()
