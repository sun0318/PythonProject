class Base(object):

    # def __init__(self):
    #     print("初始化Base")

    def message(self, num):
        print("Base.message", num)
        super().message(1000)


class Bar(object):
    def __init__(self):
        print("初始化bar")

    def message(self, num):
        print("Bar.message", num)


class Bar1(object):
    def __init__(self):
        print("初始化Bar1")

    def message(self, num):
        print("Bar1.message", num)


class Foo(Base, Bar, Bar1):

    def __init__(self):
        print("这里是Foo的init方法")
        super(Foo, self).__init__()



obj = Foo()
# obj.message(1)

