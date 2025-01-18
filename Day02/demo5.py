namelist = ["孙悟空", 1,  2,  3,  "张三", "李四", "王五", "赵六", "张三"]
#  元素长度
print(len(namelist))
#  元素在数组中出现的次数，并非所有元素个数
print(namelist.count("张三"))
#  取第一个元素
print(namelist[0])
#  取最后一个元素
print(namelist[-1])
#  index获取数据下标位置
print(namelist.index("张三"))
#  新增元素 方法1
namelist.append("刘七")
print(namelist)
#  新增元素 方法2 insert(下标, 元素)
namelist.insert(1, "孙八")
print(namelist)
#  删除元素 方法1
namelist.remove("李四")
print(namelist)
#  删除元素方法2 pop(下标)
namelist.pop(1)
print(namelist)
#  移除某个元素的第一个，并非所有
namelist.remove("张三")
print(namelist)
#  排序 只能排序同类型，如果数组中既有数字又有字符串，则会报错
# namelist.sort()
# print(namelist)
#  按长度排序
# namelist.sort(key=len)
# print(namelist)
#  排序生成新的数组，原数组数据不变
# newArray = sorted(namelist)
# print("新数组", newArray)
#  清除所有数据
namelist.clear()
print(namelist)
#  while循环访问数组 while可以加条件
# i = 0
# while i< len(namelist):
#     print(namelist[i])
#     i +=1
# #  for 循环访问数组 不可以加条件，设定参数名，循环输出参数
# for i in namelist:
#     print(i)