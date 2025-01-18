"""
构建一个列表，列表里面是三种不同尺寸的T恤衫，每个尺寸都有两个颜色（列表里面的元素为元组类型）。
colors = ['black', 'white'] sizes = ['S', 'M', 'L']
"""
# clothes_list = [(i,j) for i in ['black', 'white'] for j in ['S', 'M', 'L']]
# print(clothes_list)

"""
用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
"""
# 解决map()方法报错的问题
# import os
# os.environ['PYSPARK_PYTHON'] = "D:/Python310/python.exe"
# from pyspark import SparkConf, SparkContext
# conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# sc = SparkContext(conf=conf)
# l=[{'name':'alex'},{'name':'y'}]
# rdd1 = sc.parallelize(l)
# rdd2 = rdd1.map(lambda x : {"name":x["name"] + "sb"})
# print(rdd2.collect())

l=[{'name':'alex'},{'name':'y'}]
new_l = map(lambda x : {"name" : x["name"] + "sb"} , l)
print(list(new_l))
"""
用filter来处理,得到股票价格大于20的股票名字
"""
# import os
# os.environ['PYSPARK_PYTHON'] = "D:/Python310/python.exe"
# from pyspark import SparkConf, SparkContext
# conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# sc = SparkContext(conf=conf)
# shares={ 'IBM':36.6, 'Lenovo':23.2, 'oldboy':21.2, 'ocean':10.2, }
# rdd1 = sc.parallelize(shares)
# rdd2 = rdd1.filter(lambda x: shares[x]>20 )
# print(rdd2.collect())

shares={ 'IBM':36.6, 'Lenovo':23.2, 'oldboy':21.2, 'ocean':10.2, }
filter_shares = filter(lambda x :shares[x]>20,shares)
print(list(filter_shares))

