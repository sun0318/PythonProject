# ## 作业
#
# 1.
# 根据需求写代码
#
# ```python
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# #
# # # 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic["k4"]="v4"
# print(dic)
# # # 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic["k1"] = "alex"
# print(dic)
# # # 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic["k3"].append(44)
# print(dic)
# # # 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic["k3"].insert(0,18)
# print(dic)
# ```
#
# 2.
# 根据需求写代码
#
# ```python
# dic1 = {
#     'name': ['alex', 2, 3, 5],
#     'job': 'teacher',
#     'oldboy': {'alex': ['python1', 'python2', 100]}
# }
# #
# # 1，将name对应的列表追加⼀个元素’wusir’。
# dic1["name"].append("wusir")
# print(dic1)
# # 2，将name对应的列表中的alex全变成大写。
# dic1["name"][0]=dic1["name"][0].upper()
# print(dic1)
# # 3，oldboy对应的字典加⼀个键值对’⽼男孩’:’linux’。
# old = {'⽼男孩':'linux'}
# dic1['oldboy']["老男孩"]="linux"
# print(dic1)
# # 4，将oldboy对应的字典中的alex对应的列表中的python2删除
# dic1['oldboy']['alex'].remove("python2")
# print(dic1)
# ```
#
# 3.
# 循环提示用户输入，并将输入内容添加到字典中（如果输入N或n则停止循环）
#
# ```python
# 例如：用户输入
# x1 | wupeiqi, 则需要再字典中添加键值对
# {'x1': "wupeiqi"}
# ```
# info_dict=dict()
# print("请输入信息：")
# while True:
#     input_info = input().upper()
#     if input_info == "N":
#         print(info_dict)
#         break
#     else:
#         info = input_info.split("|")
#         info_dict[info[0]]=info[1]
# 4.
# 判断以下值那个能做字典的key ？那个能做集合的元素？
#
# - 1
# - -1
# - ""
# - None
# - [1, 2]
# - (1,)
# - {11, 22, 33, 4}
# - {'name': 'wupeiq', 'age': 18}
#
# 5.
# 将字典的键和值分别追加到
# key_list
# 和
# value_list
# 两个列表中，如：
#
# ```python
# key_list = []
# value_list = []
# info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# # ```
# key_list.append(info.keys())
# print(key_list)
# value_list.append(info.values())
# print(value_list)
# 6.
# 字典
dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
#
# ```python
# a.请循环输出所有的key
# for key in dic.keys():
#     print(key)
# # b.请循环输出所有的value
# for value in dic.values():
#     print(value)
# # c.请循环输出所有的key和value
# for key in dic.keys():
#     print(key ,dic[key])
# for k, v in dic.items():
#     print(k, v)
# ```
#
# 7.
# 请循环打印k2对应的值中的每个元素。
#
# ```python
# info = {
#     'k1': 'v1',
#     'k2': [('alex'), ('wupeiqi'), ('oldboy')],
# }
# k2 = info['k2']
# for k2_value in k2:
#     print(k2_value)
# ```
#
# 8.
# 有字符串
# d = dict()
# a =  "k: 1|k1:2|k2:3  |k3 :4"
# # 处理成字典
# # {'k': 1, 'k1': 2....}
# b = a.split("|")
# for v1 in range(len(b)):
#     c = b[v1].split(":")
#     d[c[0]]=int(c[1].strip())
# print(d)
#
# 9.
# 写代码
#
# ```python
# """
# 有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
#
#    result = {'k1':[],'k2':[]}
# """
# ```
# result = dict()
# k1 =list()
# k2 =list()
# li = [11,22,33,44,55,66,77,88,99,90]
# for v1 in li:
#     if v1 > 66:
#         k1.append(v1)
#     else:
#         k2.append(v1)
# result['k1']=k1
# result['k2']=k2
# print(result)
# 11.
# 输出商品列表，用户输入序号，显示用户选中的商品
#
# ```python
# """
# 商品列表：
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
# 要求:
# 1：页面显示 序号 + 商品名称 + 商品价格，如：
#       1 电脑 1999
#       2 鼠标 10
#       ...
count = 0
new_goods = dict()
for good in goods:
    count += 1
    name = good['name']
    price = good['price']
    new_goods[str(count)] = good
    # print("{} {} {}".format(count,name,price))
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 4：用户输入Q或者q，退出程序。
while True:
    num= input("请输入商品号:").upper()
    if num == 'Q':
        break
    elif num not in new_goods.keys():
        print("商品的序号有误，请重新输入")
    else:
        print("商品名称：{}，商品价格：{}".format(new_goods[num]['name'],new_goods[num]['price']))
# print(new_goods)


# """
# ```