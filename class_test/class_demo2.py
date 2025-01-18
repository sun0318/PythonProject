# class Person(object):
#     __a = 2222
#     a = 3333
#
#     @classmethod
#     def sleep(cls):
#         # cls.eat()
#         print(cls.a, cls)
#
#     @staticmethod
#     def eat():
#         print(1)
#         # raise ValueError("值错误！！！")
#
#     @staticmethod
#     def run():
#         print(1)
#         # raise ValueError("值错误！！！")
#
#     @property
#     def __drink(self):
#         print(11111)
#         print(self.__a)
#
#     def __str__(self):
#         return "87987329478"
# p1 = Person()
# print(dir(p1))
# Person.eat()
# Person.sleep()

# print(Person.eat)
# p1.eat()
# p1.drink
# p1._Person__drink
# print(Person().drink)
# _Person__drink
# print(p1)
# p1.b = 333
# print(p1.b)

class Foo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        print(item)

    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        pass


obj = Foo("武沛齐", 19)

print(obj["age"])
obj['x2'] = 123
print(obj['x2'])
del obj['x3']

# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __add__(self, other):
#         return "{}-{}".format(self.name, other.name)
#
#
# v1 = Foo("alex")
# v2 = Foo("sb")
#
# # 对象+值，内部会去执行 对象.__add__方法，并将+后面的值当做参数传递过去。
# v3 = v1 + v2
# print(v3)