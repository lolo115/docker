from pyspark.sql import SparkSession
from pyspark.sql.types import *

#pyspark.sql.SparkSession builder from Session
spark=SparkSession.builder\
.master("spark://master:7077")\
.appName("DataFrame Load and append in Parquet")\
.config('spark.executor.memory', '1g')\
.config('spark.executor.cores', '2')\
.config('spark.cores.max', '2')\
.config('spark.driver.memory','512m')\
.getOrCreate()


print(type(spark))

# Schema definition (not mandatory)
df_schema = [StructField('id', IntegerType(), True), StructField('name', StringType(), True), StructField('money', FloatType(), True)]
df_struct = StructType(fields=df_schema)

# DataFrame creation from CSV
df1=spark.read.csv(path='/data/cust1.csv', sep=',',schema=df_struct)
print("DF1")
df1.show()
print("type(DF1) = ",type(df1))

df2=spark.read.csv(path='/data/cust2.csv', sep=',',schema=df_struct)
print("DF2")
df2.show()
print("type(DF2) = ",type(df2))

# write dataframes content into Parquet files (df1 in overwrite mode, and df2 in append mode)
df1.write.parquet(path="/data/cust1.parquet",mode="overwrite")
df2.write.parquet(path="/data/cust1.parquet",mode="append")

print("DF3")
df3=spark.read.schema(df_struct).parquet("/data/cust1.parquet")
df3.show()
print("type(DF3) = ",type(df3))

