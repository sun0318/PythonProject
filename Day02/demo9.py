"""
使用{}存储原始，每一个元素是一个键值对
每一个键值对包含Key和Value（用冒号分隔）
键值对之间使用逗号分隔
Key和Value可以是任意类型的数据（key不可为字典）
Key不可重复，重复会对原有数据覆盖

"""
my_dict = {
    "name": "Ask",
    "age": 20,
    "gender": "male",
    "hobby": {"hot": "music", "normal": "drawing"}
}
# 取值方法1
# x = my_dict.get("name")
# print(x)
# y = my_dict.get("hobby").get("hot")
# print(y)

# 取值方法2
# x = my_dict["name"]
# print(x)
# y = my_dict["hobby"]["hot"]
# print(y)

#  新增元素
# my_dict["height"] = "180"
# print(my_dict)

#  更新元素
# my_dict["height"] = "176"
# print(my_dict)

#  删除元素
# pop函数会返回删除元素的value
# my_dict.pop("age")
# print(my_dict)
#  数组返回所有的key
# print(my_dict.keys())
#  数组返回所有的value
# print(my_dict.values())

#  循环遍历字典 字典没有下标，因此跟集合{}一样也不能用while遍历
# keys = my_dict.keys()
# for key in keys:
#     print(my_dict[key])

