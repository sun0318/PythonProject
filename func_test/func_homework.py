"""
v = [ lambda :x  for x in range(10)]
print(v)
print(v[0])
print(v[0]())
"""

"""
v = [i for i in range(10,0,-1) if i > 5]
print(v)
"""

"""
data = [lambda x:x*i for i in range(10)]
print(data)
print(data[0](2))
print(data[0](2) == data[8](2))
"""

"""
data_list = [11,22,33,"alex",455,'eirc']

new_data_list = [i for i in data_list if type(i)!= str] # 请在[]中补充代码实现。
print(new_data_list)
# 提示：可以用type判断类型
"""

"""
请用列表推导式实现，对data_list中的每个元素判断，如果是字符串类型，则计算长度作为元素放在新列表的元素中；如果是整型，则让其值+100 作为元素放在新的列表的元素中。
data_list = [11,22,33,"alex",455,'eirc']

new_data_list = [i if type(i) == str else i+100 for i in data_list ] # 请在[]中补充代码实现。
print(new_data_list)

# 提示：可以基于三元运算实现
"""

"""
data_list = [
    (1,'alex',19),
    (2,'老男',84),
    (3,'老女',73)
]

info_dict = {
    "{}:{}".format(i[0],i) for i in data_list
}
print(sorted(info_dict))
# 请使用推导式将data_list构造生如下格式：
"""

"""
info_dict = {
    1:(1,'alex',19),
    2:(2,'老男',84),
    3:(3,'老女',73)
}
"""

"""
有4个人玩扑克牌比大小，请对比字典中每个人的牌的大小，并输入优胜者的姓名（值大的胜利，不必考虑A）

player = {
    "武沛齐": ["红桃", 10],
    "alex": ["红桃", 8],
    'eric': ["黑桃", 3],
    'killy': ["梅花", 12],
}

winner = max(player, key=lambda x: player[x][1])  # 使用 max 函数找出值最大的键

print("优胜者的姓名是:", winner)
"""

"""
1 1 2 3 5 8 13 21 34 55
"""
def fib(max_count):
    a, b = 1, 1
    for _ in range(max_count):
        yield a
        a, b = b, a + b



count = input("请输入要生成斐波那契数列的个数：")
count = int(count)
fib_generator = fib(count)
for num in fib_generator:
    print(num)









