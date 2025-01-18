# # 第一阶段考试题
#
# 1.
# 简述解释型语言和编译型语言的区别。
# 解释性语言
# 2.
# 罗列你听说过的编程语言。
# C C++ C# JAVA JAVASCRIPT PYTHON PHP
# 3.
# 简述位和字节的关系？
#
# 4.
# 简述你理解的
# ascii、unicode、utf - 8、gbk
# 编码。
# - ascii，一个字节，8位，有2**8 =256个符号代表。
# - unicode，万国码，包含了全球所有文字和二进制之间的一个对应关系。（ucs2或ucs4）
# - utf - 8，对unicode字符集的码位进行压缩处理，间接也维护了字符和二进制的对照表。
# - gbk，包含中国、日本韩国等亚洲国家的文字和二进制的对照表。
#
# 5.
# py2和py3默认解释器编码分别是什么？如何在代码中修改解释器的编码？
# py2是ascii码
# py3默认是utf-8
# 6.
# pass的作用？
# 结束标识
# 7.
# is和 == 的区别？
#  == 判断两个值是否相等、is判断两个地址是否一致
# 8.
# 列举你了解的Python2和Python3的区别。
# python3.6后有dict有序
# 9.
# 变量名的命名规范有哪些？
#  不能用python关键字
# 名字用数字、下划线、和字母组成，数字不能放最前面
# 名字要见名字知其意
# 10.
# 都有那些值转换为布尔值时为False？
# int 值0、空字符串、空数组、空元组、空字典、空集合
# 11.
# 简述如下三个变量的区别。
#
# ```python
# v1 = (1)
# v2 = (1,)
# v3 = 1
# ```
#(1)是整型，（1,）带了逗号，标识元组
# 12.
# 你所学的数据类型中哪些是可变的类型？
# list set dict
# 13.
# 你所学的数据类型中哪些是可哈希的类型？
# 除了list set dict的其他数据类型
# 14.
# 你所学的数据类型中哪些是有序的？
# 字符串、元组、列表、字典（python3.6）
# 15.
# 列举你能记得的如下数据类型的方法（独有功能）。
#
# - str
# startwith
# endwith
# strip
# upper
# lower
# - list
# append
# remove
# extend
# pop
# remove
# sort
# sorted

# - dict
# get
# keys
# values
# items
# update
#
# 16.
# 请将字符
# `name = "wupeiqi"
# ` 翻转。
# new_name  = name[::-1]
#
# 17.
# 进制之间如何进行转换？
# 先转十进制，再转其他进制 bin(),oct(),int( data, base=),hex()
# 18.
# 循环过程中
# break和continue的作用是什么？
# break终止循环、continue跳出此次循环，进入下次循环
# 19.
# 看代码写结果
#
# ```python
# v1 = 1 or 9 and 88 or [11, 22] and (1, 2, 3)
# True
#
# v2 = 1 > 5 or "alex" and {"K1": "v1"} or 888
# True
# print(v1, v2)
#True True
# ```
#
# 20.
# 看代码写结果
#
# ```python
# info = [
#     {'k1': (1), 'k2': {'k9': 'luffy', 'k10': '武沛齐'}},
#     (11, 22, 33, 44),
#     {199, 2, 3, 4, 5},
#     True,
#     ['李杰', 'alex', {'extra': ("alex", [18, 20], 'eric')}]
# ]
# ```
#
# - 利用索引获取
# "luffy"
# print(info[0]['k2']['k9'])
# - 利用索引获取
# 44
# print(info[1][3])
# # - 删除k10对应的键值对
# b = info[0]['k2'].pop('k10')
# print(info)
# - 在
dict_data = {'extra': ("alex", [18, 20], 'eric')}
# 字典中添加一个键值对
# `"name": "武沛齐"
dict_data['name']='武沛齐'
# `
# - 在集合
a = {199, 2, 3, 4, 5}
# 中添加一个
# "北京"
a.add('北京')
print(a)
# - 将列表中的True修改为
# "真"

# - 在列表
c = [18, 20]
# 的第0个索引位置插入
# 666
c.insert(0,666)
print(c)
#
# 21.
# 判断下面的代码是否正确？正确的话则写出结果，否则标明错误。
#
# ```python
v1 = (11, 22, 33)
v2 = (11)
v3 = {11, 2, 33}
v4 = {11, 2, ("alex", "eric"), 33}
# 错误、集合里不能放集合（不可hash）
# v5 = {11, 2, ("alex", {"北京", "上海"}, "eric"), 33}
# ```
#
# 22.
# 看代码写结果
#
# ```python
# v1 = [11, 22, 33]
# v2 = [11, 22, 33]
# v1.append(666)
#
# print(v1)
# [11, 22, 33，666]
# print(v2)
# [11, 22, 33]
# ```
#
# 23.
# 看代码写结果
#
# ```python
# v1 = [11, 22, 33]
# v2 = v1
# v1.append(666)
#
# print(v1)
# [11, 22, 33,666]
# print(v2)
# [11, 22, 33,666]
# ```
#
# 24.
# 看代码写结果
#
# ```python
# v1 = [1, 2, 3, 4, 5]
# v2 = [v1, v1, v1]
# v2[1][0] = 111
# v2[2][0] = 222
#
# print(v1)
# [1, 2, 3, 4, 5]
# print(v2)
# [[1, 2, 3, 4, 5],[111, 2, 3, 4, 5],[222, 2, 3, 4, 5]]
# ```
#
# 25.
# 写代码实现，循环提示用户输入内容（Q或q终止），并将内容用
# "_"
# 连接起来。
# data_list = []
# while True:
#     text = input("请输入（Q/q退出）：")
#     if text.upper() == "Q":
#         break
#     data_list.append(text)
#
# result = "_".join(data_list)
# print(result)
#
# 26.
# 写代码实现，将IP转换为整数。
#
# > 如
stra = '10.3.9.12'
# 转换规则为：
# > 10
# 00001010
# > 3
# 00000011
# > 9
# 00001001
# > 12
# 00001100
# > 再将以上二进制拼接起来，然后再进行一次翻转。
# >
# > 最终将翻转之后的二进制转换为整型。
# lint = 0
# str1 = ""
# for num in stra.split('.'):
#     bin_num = bin(int(num))[2:].zfill(8)
#     str1 += str(bin_num)
# print(int(str1[::-1],base=2))
#
# 27.
# 写代码实现，车牌的区域划分。

#
# ```python
# car_list = ['鲁A32444', '沪B12333', '京B8989M', '京C49678', '黑C46555', '晋B25041', '沪C34567']
# info = set()
# for item in car_list:
#     city = item[0]
#     if city in info:
#         info[city] = info[city] + 1
#     else:
#         info[city] = 1
#
# print(info)
# # 根据以上代码获取各省车牌数量，例如：info = {"沪":2,"京":2 ...}
# ```
#
# 28.
# 写代码实现，数据格式化处理。
#
# ```python
# text = """id,name,age,phone,job
#     1,alex,22,13651054608,IT
#     2,wusir,23,13304320533,Tearcher
#     3,老男孩,18,1333235322,IT"""
#
# # 将上述数据处理为如下格式的结果：
# #    info = [{'id':'1','name':'alex','age':'22','phone':'13651054608','job':'IT'},.... ..]
# # 提示：text的内容是根据 \n 分割（\n表示回车换行）。
#
# text_list = text.split("\n")
# # 拆分第一行
# title = text_list[0].split(",")
# id = title[0]
# name = title[1]
# age = title[2]
# phone = title[3]
# job = title[4]
# info = list()
# # 从第二行开始循环拆分
# for text_line in text_list[1:]:
#     data = text_line.split(',')
#     data_dict = dict()
#     data_dict[id]=data[0].strip()
#     data_dict[name] = data[1].strip()
#     data_dict[age] = data[2].strip()
#     data_dict[phone] = data[3].strip()
#     data_dict[job] = data[4].strip()
#     info.append(data_dict)
# print(info)

# ```
#
# 29.
# 写代码实现
# 累乘计算器。
#
# ```python
# content = input("请输入内容:")  # 用户可能输入 5*9*99.... 或 5* 9 * 10 * 99 或 5 * 9 * 99...
#
# # 补充代码实现
# ```
# result = 1
# num_list = content.split("*")  # ["5","9","99"]
# for num in num_list:
#     result = result * int(num)
#
# print(result)
# 30.
# 使用for循环实现输出
# 9 * 9
# 乘法表
#
# ```
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}\t'.format(i,j,i * j) , end="")
#     print("")
#
# 31.
# 补充代码实现《棋牌游戏11点》
#
# 需求：
#
# - 生成一副扑克牌（自己设计扑克牌的结构，小王和大王可以分别用14、15
# 表示 ）
#
# - 3
# 个玩家
#
# ```python
# user_list = ["alex", "武沛齐", "李路飞"]
# ```
#
# - 发牌规则
#
# - 默认先给用户发一张牌，其中
# J、Q、K、小王、大王代表的值为0.5，其他就是则就是当前的牌面值。
# - 用户根据自己的情况判断是否继续要牌。
# - 要，则再给他发一张。
# - 不要，则开始给下个玩家发牌。
# - 如果用户手中的所有牌相加大于11，则表示爆了，此人的分数为0，并且自动开始给下个人发牌。
#
# - 最终计算并获得每个玩家的分值，例如：
#
# ```python
# result = {
#     "alex": 8,
#     "武沛齐": 9,
#     "李路飞": 0
# }
# ```
#
# 必备技术点：随机抽排
#
# ```python
# import random
#
# total_poke_list = [("红桃", 1), ("黑桃", 2), ("大王", 15), ("小王", 14)]
#
# # 随机生成一个数，当做索引。
# index = random.randint(0, len(total_poke_list) - 1)
# # 获取牌
# print("抽到的牌为：", total_poke_list[index])
# # 踢除这张牌
# total_poke_list.pop(index)
#
# print("抽完之后，剩下的牌为：", total_poke_list)
# ```
#
# 代码示例：（请补充实现）
#
# ```python
# result = {}
# user_list = ["alex", "武沛齐", "李路飞"]
# # 补充代码
#    import random

#     result = {}
#
#     user_list = ["alex", "武沛齐", "李路飞"]
#
#     # 1. 生成一副扑克牌
#     total_poke_list = [ ("小王",14),("大王",15) ]
# color_list = ["红桃", "黑桃", "方片", "梅花"]
#     num_list = []
# for num in range(1, 14):
#         num_list.append(num)
#     for color in color_list:
#         for num in num_list:
#             item = (color, num,)
#             total_poke_list.append(item)
#
#     # 2. 发牌 -> ["alex", "武沛齐", "李路飞"]
#     for user in user_list:
#         # 给用户发第一张牌
#         score = 0
#         index = random.randint(0, len(total_poke_list) - 1)
#         poke = total_poke_list.pop(index) # ("花色",值)
#         # JQK表示 0.5 点
#         value = poke[1]
#         if poke[1] > 10:
#             value = 0.5
#         score += value
#         print("给{}发的牌：{}{}，此刻所有牌面值总和:{}".format(user, poke[0], poke[1], score))
#
#         # 用户选择是否继续要
#         while True:
#             choice = input("是否继续要牌(Y/N)？")
#             choice = choice.upper()
#
#             # 用户输入的不是Y/N/y/n
#             if choice not in {"Y", "N"}:
#                 print("输入错误，请重新输入。")
#                 continue
#
#             # 用户输入N，不继续要牌了
#             if choice == "N":
#                 print("{}不要拍了".format(user))
#                 break
#
#             # 继续要拍（再随机抽取一张）
#             index = random.randint(0, len(total_poke_list) - 1)
#             poke = total_poke_list.pop(index)
#             value = poke[1]
#             if poke[1] > 10:
#                 value = 0.5
#             score += value
#
#             print("给{}发的牌：{}{}，此刻所有牌面值总和:{}".format(user, poke[0], poke[1], score))
#
#             # 大于11点，则用户爆了且分值变为0
#             if score > 11:
#                 print("用户{}爆了".format(user))
#                 score = 0
#                 break
#
#         result[user] = score
#
#     print(result)
#
# print(result)
# ```
#
#
#
#
