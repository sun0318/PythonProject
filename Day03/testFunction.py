# 控制权限，让外围只能调用数组里定义的函数
__all__ = ["add"]


def add(x, y):
    print(x + y)


def minus(x, y):
    print(x - y)
#  调用自己内部函数做测试时，记得写main判断，否则别人调用宝时会自动执行add方法
# if __name__ == '__main__':
# add(1, 5)