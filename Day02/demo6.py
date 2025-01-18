# 元组数据不可修改，除了里面的数组
#  字符串
cityList = ("岳阳")
#  元组 当数据只有一个时，后面需要加上逗号，否则会被认定为字符串
cityList2 = ("岳阳",)
city = "岳阳"
print(city == cityList)  # True
print(cityList[0])  # 只返回 岳
print(cityList2[0]) # 返回 岳阳
namelist = ("张三", "李四")

# 元组数据不可修改，数组内的值可以修改，但是不能替换成其他数组或其他类型
cityList3 = ("岳阳", [1, 2, 3], 9, 8, 9)
# cityList3[0] = "长沙" 会报错，不能修改
# cityList3[1] = [8, 9]  报错，不能替换数组
cityList3[1][0] = 7
print(cityList3)  # ('岳阳', [7, 2, 3])
#  可以对其数组进行操作
str1 = cityList3[1]
str1.remove(2)
print(cityList3)
#  其他方法 index() count()
print(cityList3.index(9))
print(cityList3.count(9))


