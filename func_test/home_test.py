"""
1.  一个大小为100G的文件 etl\_log.txt，要读取文件中的内容，写出具体过程代码。
"""
# import os
# size = os.path.getsize("files\stock.txt")
# with open("files\stock.txt",mode="rb") as f:
#     begin_size = 0
#     while begin_size < size:
#         data = f.read(1)
#         begin_size = begin_size + len(data)


"""
2.  编写一个函数，这个函数接受一个文件夹名称作为参数，寻找文件夹中所有文件的路径并输入（包含嵌套）。
"""
# import os
# def show_files(dir_name):
#     for base_path,folder,file_list in os.walk(dir_name):
#         for files in file_list:
#             abs_path = os.path.join(base_path,files)
#             print(abs_path)

"""
3.  以下的代码数据的结果是什么？
"""
# def extend_list(val,data=[]):
#     data.append(val)
#     return data
#
# list1 = extend_list(10)
# list2 = extend_list(123,[1])
# list3 = extend_list("a")
# list4 = extend_list(1,[555])
# list5 = extend_list("b")
#
# print(list1,list2,list3,list4,list5)

"""
4.  python代码获取命令行参数。
"""
# import sys
# print(sys.argv)
"""
5.  简述深浅拷贝？
"""
# import copy
#
# list1 = [1, 2, [3, 4]]
# list2 = copy.copy(list1)
#
# list2[1] = 5
#
# print(id(list1[2]))  # 输出：[1, 2, ['changed', 4]]
# print(id(list2[2]))  # 输出：[1, 2, ['changed', 4]]
#
# print(list1)  # 输出：[1, 2, ['changed', 4]]
# print(list2)  # 输出：[1, 2, ['changed', 4]]

"""
6.  基于推导式一行代码生成1-100以内的偶数列表。
list_data = [i for i in range(1,101) if i%2 ==0]

7.  请把以下函数转化为python lambda匿名函数

    ```python
    def add(x,y):  
        return x+y
    ```
# add=lambda (x,y):x+y 

8.  看代码写结果

    ```python
    def num():
        return [lambda x: i * x for i in range(4)]

    result = [m(2) for m in num()]
    print(result)
    ```
    [6,6,6,6]
# 6
9.  列表推导式和生成器表达式 [i % 2 for i in range(10)] 和 (i % 2 for i in range(10)) 输出结果分别是什么？
# [0,1,0,1,0,1,0,1,0]  (生成器)

10. 写装饰器

    ```python
    # 写timer装饰器实现：计算fun函数执行时间，并将结果给 result，最终打印（不必使用datetime,使用time.time即可）。
"""
# import time
# def timer(origin):
#     def inner(*args,**kwargs):
#         begin = time.time()
#         res = origin()
#         end = time.time()
#         gap = end - begin
#         print(gap)
#         return res
#     return inner
#
# @timer
# def func():
#     time.sleep(1)
#     pass
#
# result = func()
# print(result)

"""
11. re的match和search区别？
match从第一个元素开始匹配，未匹配成功返回None，search全局匹配找到第一个匹配的元素

12. 什么是正则的贪婪匹配？或 正则匹配中的贪婪模式与非贪婪模式的区别？
贪婪匹配：尽可能多的匹配字符串
非贪婪匹配：尽可能少的匹配字符串，添加?

13. sys.path.append("/root/mods")的作用？
可当成内置模块访问模块

14. 写函数

    ```python
    有一个数据结构如下所示，请编写一个函数从该结构数据中返画由指定的 字段和对应的值组成的字典。如果指定字段不存在，则跳过该字段。
    DATA = {
        "time": "2016-08-05T13:13:05",
        "some_id": "ID1234",
        "grp1": {"fld1": 1, "fld2": 2, },
        "xxx2": {"fld3": 0, "fld4": 0.4, },
        "fld6": 11,
        "fld7": 7,
        "fld46": 8
    }

    fields:由"|"连接的以fld开头的字符串, 如fld2|fld7|fld29  

    def select(fields):
        print(DATA)
        return result
    ```

15. 编写函数，实现base62encode加密（62进制），例如：

        内部维护的数据有：0123456789AB..Zab..z(10个数字+26个大写字母+26个小写字母)。
        当执行函数：
        	base62encode(1)，获取的返回值为1
        	base62encode(61)，获取的返回值为z
        	base62encode(62)，获取的返回值为10
"""
# def base62encode(num):
#     number="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#     mul,mod = divmod(num,62)
#     if not mul:
#         base62 = number[mod]
#     else:
#         base62 = number[mul] + number[mod]
#     print(base62)
#
# base62encode(12)
"""
16. 基于列表推导式一行实现输出9*9乘法表。
"""

# a = ["{}*{}={}".format(i,j,i*j) for i in range(1,10) for j in range(1,i+1)]
# a = [["{}*{}={}".format(i,j,i*j)  for j in range(1,i+1)] for i in range(1,10)]
a = [[(i,j) for j in range(1,i+1)] for i in range(1,10)]
print(a)

