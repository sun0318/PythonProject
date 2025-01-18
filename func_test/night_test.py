# def func(b):
#     return b + 1
#
# a = [func for i in range(10)]
# print(a[0](1))

# b = (lambda x: x + i for i in range(10))
# c = next(b)
# d = next(b)
# e = b.send(3)
# print(d(4))
# print(e(4))
# print(next(c))

# print(b[5](1))

test = (x for x in range(10))

a = next(test)
print(a)
print(test.send(8))
print(next(test))