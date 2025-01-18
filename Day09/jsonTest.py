import json
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Python310/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("spark_app")
conf.set("spark.default.parallelism","1")
sc = SparkContext(conf=conf)
rdd = sc.textFile("D:\数据分析\课件\第15章资料\资料\search_log.txt")
# print(rdd.collect())
# 打印输出：热门搜索时间段（小时精度）Top3
rddtop3 = rdd.map(lambda x:x.split("\t")).\
    map(lambda x: (x[0][:2],1)).\
    reduceByKey(lambda x,y :x+y).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).take(3)
# .map(lambda x: (x[0][:2],1))
# print(rddtop3)
# 打印输出：热门搜索词Top3
rddtop4 = rdd.map(lambda x:x.split("\t")).\
    map(lambda x:(x[2],int(x[3]))).\
    reduceByKey(lambda x,y:x+y).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).take(3)
# print(rddtop4)
# 打印输出：统计黑马程序员关键字在哪个时段被搜索最多
rddtop5 = rdd.map(lambda x:x.split("\t")).\
    filter(lambda x:x[2]=="itheima").\
    map(lambda x:(x[0][:2],int(x[3]))).\
    reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False,numPartitions=1).take(1)
# print(rddtop5)
# 将数据转换为JSON格式，写出为文件
rdd6 = rdd.map(lambda x:x.split("\t")).\
    map(lambda x:{"time":x[0],"id":x[1],"keyword":x[2],"count":x[3],"num":x[4],"url":x[5]}).\
    saveAsTextFile("jsondata")
