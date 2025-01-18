from pyspark import SparkConf, SparkContext
# 解决map()方法报错的问题
import os

os.environ['PYSPARK_PYTHON'] = "D:/Python310/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 文件存储分区，方法一
# conf.set("spark.default.parallelism","1")
sc = SparkContext(conf=conf)
rdd = sc.textFile("hello.txt")
rdd2 = rdd.flatMap(lambda x: x.split(" "))
rddlist = rdd2.map(lambda x: (x, 1)).map()
rddlist2 = rddlist.reduceByKey(lambda x, y: x + y, 1)
print(rddlist2.collect())
# savaAsTextFile
rddlist2.saveAsTextFile("a.txt")
