import string

print("1------------------------------")
print("hello you")  # 1.每行前面不要有空格,空格有语法含义，多行代码可以放一行，但是需要用分号分割;开来
print(1 + 1)  # ctrl + alt +l 进行格式化
print("你好", end="")  # print默认输出后加回车换行，end则可以自定义结束符

print("2------------------------------")
str3 = """
2.多行注释，也可以当成字符串
你好呀
"""
print("3------------------------------")
# 3 变量定义,可以不写数据类型
x = 1
y = 5
z = x + y
print(z)
player_name = "发条魔灵"
player_level = 3
isTrue = True
print(x + isTrue)
print(x < 5)
# 打印数据类型
print(type(x))
print("4------------------------------")
# 4 整型出了0是false，其他的都是true
print(bool(-1))
print(bool(0))
print("5------------------------------")
# 5 除了空字符串是false，其他都是true
print(bool(""))
print(bool("0"))
print("6------------------------------")
# 6 除了空数组返回false，其他返回true
print(bool([]))
print(bool([1, 2]))

str1 = 'hello'
str2 = "world"
print(str1 + str2 + str3)
print("7------------------------------")
# 7 格式化输出
name = "ask"
age = 27
height = 170

# 方式一
print("我的名字叫%s，我的年龄是%d岁，我的身高是%d" % (name, age, height))
# 方式二（推荐） 3.6版本解释所有
print(f"我的名字叫{name}，我的年龄是{age}岁，我的身高是{height}")
print("8------------------------------")
floatnumber = 1.3
print("精度控制：%.2f" % floatnumber)
print(f"精度控制2：{floatnumber}")
# 8 字符串索引下表从0开始，从后往前取值，用负数
str4 = "一二三四五六七八九十"
print(str4[0])
print(str4[1])
print(str4[-1])

# 切片操作：字符串[开始索引:结束索引:取值方向（1：从左往右，-1：从右往左）]顾头不顾尾，记住是不顾尾，取值规则从左往右取，所以s[5:1]取不到值，但是s[5:1:-1]可以取值，因为是从右往左取值
print(str4[0:5])
print(str4[3:-1])  # -1表示最后
print(str4[4:])  # 缺省右边默认取到最后
print(str4[:5])  # 缺省左边默认从0开始取
print("取值：" + str4[5:1])  # 取不到值
print(str4[2:8:2])  # 从第三位开始取，没两位取一次，取到第七位（顾头不顾尾，不包含第8位）
print(str4[5:1:-1])
print("9------------------------------")
# 9 字符串拼接
name = "ask锟"
age = "19"
print(name + age)  # int型不能通过加""的形式转成字符串
print("*" * 100)
print(len(name))  # 字符长度
print(len(name.encode("utf-8")))  # 字节长度
print("10------------------------------")
#  10 针对容器类型： in 判断 判断某个成员是否存在
s6 = "I love egg"
print("egg" in s6)

#  10 输入输出函数,input默认接收的是字符串，输入数字也当成字符串
# print("请输入名字:\n")
# name = input()
# age = input("请输入年龄:\n")
# print(f"姓名: {name} 年龄: {age}")

# print("请输入数字1:\n")
# num1 = input()
# num2 = input("请输入数字2:\n")
# # string类型转int类型
# print(int(num1)+int(num2))

print(100, "Hello", 999)  # 多组打印用逗号分隔，打印结果会用空格分开显示
print(100, "Hello", 999, sep=",")  # 结果显示分隔符 用sep参数控制
print("11------------------------------")
#  11 字符串函数，
#  strip()去除字符串两端的空格或换行符
str6 = " 1 2 3 "
print(str6.strip())
#  isdigit()判断是否是数字;
str7 = "1"
print(str7.isdigit())
str7.isdigit()
#  split()字符串分割 得到下标0开始的数组
str8 = "abc d"
print(str8.split(" ")[1])
#  join()用符号分隔容器中的元素元素得到一个新的字符串 a;b;c; ;d
print(";".join(str8))
#  find() 找不到返回-1
print("12345".find("5"))
#  index() 找不到报错
print("12345".index("3"))
print("12------------------------------")
#  12 使用 and 表示逻辑与，or 表示逻辑或，not 表示逻辑非。
print(1 == 1 and 1 == 2)
print(1 == 1 or 1 == 2)
print(not 1 == 2)
print("13------------------------------")
#  13 Python 也有三元运算符，但使用的是类似于 a if condition else b 的语法。
#     Python 使用 None 表示空值。
print(x if x > y else y)
str9 = None
print("14------------------------------")

#  14 条件判断 没有括号，要加冒号
if x == 2:
    print("if测试")
elif y == 2:
    print("elif测试")
else:
    print("else测试")
print("15------------------------------")
#  15 string库的一些用法
print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.ascii_uppercase)
print("16------------------------------")
#  16 for 循环 range(100);range(1,100)顾长不顾尾每次加1;range(1,100,2)每次加2
str10 = ""
for i in range(5):
    str10 += str(i)
print(str10)

str11 = ""
for i in range(1, 5, 2):
    str11 += str(i)
print("range=" + str11)

str12 = ""
for i in range(3, 8):  # 顾长不顾尾 结果：34567
    str12 += str(i)
print("range=" + str12)
print("17------------------------------")
#  17 while循环
i1 = 0
i2 = 0
while i1 < 10:
    i1 += 1
    if i1 < 2:
        continue
    i2 += 1
    if i1 == 7:
        break

print(i1)
print(i2)
