"""
函数可以接受多个参数，也可以return 多个参数，用逗号分隔
"""
# def number(x, y):
#     z1 = x + y
#     z2 = x * y
#     return z1, z2
#
#
# x, y = number(3, 4)
# print(x, y)

#  函数作为参数传递
"""
函数compute，作为参数，传入了test_func函数中使用。
test_func需要一个函数作为参数传入，这个函数需要接收2个数字进行计算，计算逻辑由这个被传入函数决定
compute函数接收2个数字对其进行计算，compute函数作为参数，传递给了test_func函数使用
最终，在test_func函数内部，由传入的compute函数，完成了对数字的计算操作
所以，这是一种，计算逻辑的传递，而非数据的传递。

"""


def test_func(compute):
    result = compute(1, 2)
    print(result)


def compute(x, y):
    return x + y


test_func(compute)
#  可以通过lambda关键字，传入一个一次性使用的lambda匿名函数,
# lambda 是关键字，表示定义匿名函数
# 传入参数表示匿名函数的形式参数，如：x, y 表示接收2个形式参数
#  函数体，就是函数的执行逻辑，要注意：只能写一行，无法写多行代码
test_func(lambda x, y: x * y)


