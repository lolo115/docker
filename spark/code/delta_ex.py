from pyspark.sql import SparkSession
from pyspark.sql.types import *

#pyspark.sql.SparkSession builder from Session
spark=SparkSession.builder\
.master("spark://master:7077")\
.appName("Delta Example")\
.config("spark.jars.packages", "io.delta:delta-core_2.11.0.6.1")\
.config('spark.executor.memory', '1g')\
.config('spark.executor.cores', '2')\
.config('spark.cores.max', '2')\
.config('spark.driver.memory','512m')\
.getOrCreate()


df= spark.read.csv(path="/data/ecommerce_Customers.csv",
                  header="True",
                  multiLine="True",
                  inferSchema="True").withColumnRenamed("Avg. Session Length","Avg_Session_Length")\
.withColumnRenamed("Time on App","Time_on_App")\
.withColumnRenamed("Time on Website","Time_on_Website")\
.withColumnRenamed("Length of Membership","Length_of_Membership")\
.withColumnRenamed("Yearly Amount Spent","Yearly_Amount_Spent")

df.printSchema()

df.repartition(5,"Avatar")
df.write.format("delta").mode("overwrite").save("/data/ecommerce_delta/")
