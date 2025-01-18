"""
def outter(origin):
    def inner(*args, **kwargs):
        res = origin(*args, **kwargs)
        print("after")
        return res
    return inner

@outter
def func(a1):
    return a1 + "傻叉"

@outter
def base(a1,a2):
    return a1 + a2 + '傻缺'

@outter
def foo(a1,a2,a3,a4):
    return a1 + a2 + a3 + a4 + '傻蛋'

func("11")
base("11","22")
foo("11","22","33","44")
"""
"""
1.  请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：将被装饰的函数执行5次，讲每次执行函数的结果按照顺序放到列表中，最终返回列表。

    ```python
    import random 


    def func():
        return random.randint(1,4)

    result = func() # 内部自动执行5次，并将每次执行的结果追加到列表最终返回给result
    print(result) 
    ```

import random

def outter(orgin):
    def inner():
        result = list()
        for i in range(0,5):
            res = orgin()
            result.append(res)
        return result
    return inner

@outter
def func():
    return random.randint(1, 4)


result = func()  # 内部自动执行5次，并将每次执行的结果追加到列表最终返回给result
print(result)
"""
"""
1.  请为以下函数编写一个装饰器，添加上装饰器后可以实现： 检查文件所在路径（文件件）是否存在，如果不存在自动创建文件夹（保证写入文件不报错）。

    ```python
    def write_user_info(path):
        file_obj = open(path, mode='w', encoding='utf-8')
        file_obj.write("武沛齐")
        file_obj.close()

    write_user_info('/usr/bin/xxx/xxx.png')
    ```


import os
def outter(origin):
    def inner(*args, **kwargs):
        path_dir = os.path.dirname(*args)
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
        res = origin(*args,**kwargs)
        return res
    return inner


@outter
def write_user_info(path):
    file_obj = open(path, mode='w', encoding='utf-8')
    file_obj.write("武沛齐")
    file_obj.close()


write_user_info('usr/bin/xxx/aaa.txt')

"""
"""
def get_data():
    scores = []

    def inner(val):
        scores.append(val)
        print(scores)

    return inner


func = get_data()

func(10)
func(20)
func(30)
"""
"""
name = "武沛齐"


def foo():
    print(name)


def func():
    name = "root"
    foo()


func()
"""
"""
name = "武沛齐"


def func():
    name = "root"

    def foo():
        print(name)

    foo()


func()
"""
"""
def func(val):
    def inner(a1, a2):
        return a1 + a2 + val

    return inner


data_list = []

for i in range(10):
    data_list.append(func(i))

print(data_list)
"""
"""
def func(val):
    def inner(a1, a2):
        return a1 + a2 + val

    return inner


data_list = []

for i in range(10):
    data_list.append(func(i))

v1 = data_list[0](11,22)
v2 = data_list[2](33,11)

print(v1)
print(v2)
"""
