from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql.types import *

#pyspark.sql.SparkSession builder from Session
spark=SparkSession.builder\
.master("local")\
.appName("DataFrame Load")\
.getOrCreate()


# spark is from the previous example.
# Create a simple DataFrame, stored into a partition directory
sc = spark.sparkContext

squaresDF = spark.createDataFrame(sc.parallelize(range(1, 6))
                                  .map(lambda i: Row(single=i, double=i ** 2)))
squaresDF.write.parquet("file:///data/test_table/key=1")

# Create another DataFrame in a new partition directory,
# adding a new column and dropping an existing column
cubesDF = spark.createDataFrame(sc.parallelize(range(6, 11))
                                .map(lambda i: Row(single=i, triple=i ** 3)))
cubesDF.write.parquet("file:///data/test_table/key=2")

# Read the partitioned table
mergedDF = spark.read.option("mergeSchema", "true").parquet("file:///data/test_table")
mergedDF.printSchema()
