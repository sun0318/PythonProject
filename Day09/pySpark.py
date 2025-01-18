from pyspark import SparkConf, SparkContext
# 解决map()方法报错的问题
import os
os.environ['PYSPARK_PYTHON'] = "D:/Python310/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)

# parallelize方法加载容器数据
# print(sc.version)
# rdd1 = sc.parallelize([1, 2, 3, 4, 5])

# filter
# newstr = rdd1.filter(lambda x:x%2==0)
# print(newstr.collect())


# rdd2 = sc.parallelize("this is a string")
# # collect得到的结果是数组，字典只会输出Keys
# print(rdd1.collect())
# textFile加载文件数据
# rdd = sc.textFile("hello.txt")
# print(rdd.collect())
# def func(data):
#     return data * 10

# map(处理的函数，一条条处理数据的逻辑)，返回一个新的rdd，逻辑简单的话也可以用lambda来写逻辑
# rdd2 = rdd1.map(func)
# rdd2 = rdd1.map(lambda x: x * 10)
# print(rdd2.collect())

# data=["apple banana pear","apple banana pear","apple banana pear"]

# rdd10 = sc.parallelize(data)
# map处理数组的结果[['apple', 'banana', 'pear'], ['apple', 'banana', 'pear'], ['apple', 'banana', 'pear']]
# rdd11= rdd10.map(lambda x : x.split(" "))
# flatMap解除数组嵌套 处理数组的结果 ['apple', 'banana', 'pear', 'apple', 'banana', 'pear', 'apple', 'banana', 'pear']
# rdd11= rdd10.flatMap(lambda x : x.split(" "))
# print(rdd11.collect())

# reduceByKey 按照key值分组
# data1 = [("男",100),("男",100),("女",100),("女",100),("女",100),(1,199),(1,1)]
#
# rdddata = sc.parallelize(data1)
# rdddata1 = rdddata.reduceByKey(lambda x,y:x + y)
# print(rdddata1.collect())

sortdata = [("Ask",2,"male"),("Ask",1,"male"),("Ask",4,"male"),("Ask",3,"male")]
rdddata = sc.parallelize(sortdata)
# x[]下标 表示要排序的参数值，ascending = True升序，False降序
final_rdd= rdddata.sortBy(lambda x:x[1],ascending=False,numPartitions=1)
print(final_rdd.collect())
