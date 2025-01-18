#  首先，因为集合是无序的，所以集合不支持：下标索引访问
#  但是集合和列表一样，是允许修改的，所以我们来看看集合的修改方法

my_set1 = {"banana", "Hello", "world", "apple"}
my_set2 = {"apple", "张三", "李四", "王五", "赵六", "banana"}
test = {"1": "3", "age": 13}
print(my_set2)
print(test)
# #  新增一个元素
# my_set1.add("human")
print(my_set1)
# #  随机取出一个元素，并且这个元素在原集合中会被清除
# new_set = my_set1.pop()
# print(my_set1)
# #  删除指定元素，找不到会报错
# my_set1.remove("Hello")
# print(my_set1)
# #  删除指定元素，找不到不会报错
# my_set1.discard("Hello")
# print(my_set1)


# my_set3 = {"a", "b", "c", "d", "1", "2"}
# my_set4 = {"1", "2", "A", "B", "C", "D"}
#  找出my_set3中在my_set4里没有的元素生成新的集合，原来的集合不做修改
# my_set5 = my_set3.difference(my_set4)
# my_set5 = my_set3 - my_set4
# print(my_set5)
# 功能：对比集合1和集合2，在集合1内，删除和集合2相同的元素。
# 结果：集合1被修改，集合2不变

# my_set4.difference_update(my_set3)
# print(my_set4)
# print(my_set3)
#  生成一个合并的集合
# my_set6 = my_set4.union(my_set3)
# my_set6 = my_set4 | my_set3
# print(my_set6)
#  集合长度
# print(len(my_set6))

# 两个集合共有元素，生成新的集合
# x = my_set3.intersection(my_set4)
# x = my_set3 & my_set4
# print(x)
# 修改my_set3为两个集合共有元素的集合
# my_set3.intersection_update(my_set4)
# print(my_set3)
# 如果两个集合没有交集，就返回True，否则返回false
# test1 = {"1", "2", "3"}
# test2 = {"2", "4"}
# print(my_set3.isdisjoint(test1))
# 判断一个集合是否包含另一个集合的所有元素
# print(my_set3.issuperset(test2))
# 判断一个集合全部元素被另一个集合包含
# print(my_set3.issubset(test1))

# 两个集合合并并且去除相同元素后的新集合
# y = test1.symmetric_difference(test2)
# y = test1 ^ test2

# 两个集合合并并且去除相同元素后的集合覆盖到test1
# test1.symmetric_difference_update(test2)
# test1.add("1")  #  重复元素不添加，会自动去重
# test1.add("5")
# print(test1)


#  集合不支持下标索引，因此也不支持while循环
# for i in my_set6:
#     print(i)
