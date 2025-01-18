# with open('files/stock.txt','rt',encoding="utf-8") as f:
#     # f.seek(3)
#     for line in f:
#         print(line,end="")

test = {'a':1,'b':2}

print(test.get('c','b'))

import time
print(time.strftime("%Y=%m-%d@%H>%M>%S",time.gmtime()))

a=round((((3**2+5*(6**7))/8))**(1/2),3)
print(a)
b = 0x14a
print("二进制{0:b},十进制{0},八进制{0:o},十六进制{0:x}".format(10))

help(dict)

