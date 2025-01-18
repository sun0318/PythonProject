# a = lambda x,y : x+y
# b = lambda x :3 if 1>x else 4
#
# print(a(1,1))
# print(b(9))

def c():
    print("c")
    v1 = yield 1
    # print(v1)
    print("d")
    v2 = yield 2

d = c()
n1 = d.send(None)
print(n1)

n2 = d.send(22)
print(n2)

# c1 = next(d)
# d1 = next(d)
#
# for item in d:
#     # print(item)
#     pass

# import random
# def get_count(max_count):
#     count = 0
#     while count < max_count:
#         c1 = yield random.randint(1000,9000)
#         count +=1
#
# data_list = get_count(1000)
#
# # print(next(data_list))
# # print(next(data_list))
# data_list.send(None)


