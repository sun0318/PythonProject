def func(i = []):
    print(id(i))
    i.append(1)
    return i

i1= func()
# print(i1) # [1]

i2 = func([2])
# print(i2) # [2,1]

i3 = func()
# print(i3) # [1,1]

print(i1)# [1,1]
print(i2)# [2,1]
print(i3)# [1,1]

# def func(a1, a2=[1, 2]):
#     a2.append(a1)
#     return a2

# v1 = func(10)
# print(v1)
# v2 = func(20)
# print(v2)
# v3 = func(30, [11, 22])
# print(v3)
# v4 = func(40)
# print(v4)
#
# # print(v1) # [1,2,10]
# # print(v2) # [1,2,10,20]
# # print(v3) # [11,22,30]
# # print(v4) # [1,2,10,20,40]