from pyspark import SparkConf, SparkContext
conf=(SparkConf()
        .setMaster("local")
        .setAppName("readSimpleCSV"))
sc=SparkContext(conf=conf)

c1=sc.textFile("/data/cust1.csv") \
    .map(lambda line: line.split(",")) \
    .collect()
print("C1 = ",c1)
print("type(C1) = ",type(c1))

c2=sc.textFile("/data/cust2.csv") \
    .map(lambda line: line.split(",")) \
    .collect()
print("C2 = ",c2)
print("type(C2) = ",type(c2))

