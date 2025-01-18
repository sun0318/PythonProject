global i
i = 10

class test(object):
    def fun1(str1):
        """
        函数说明卸载函数体内
        :param str1:
        :return:
        """
        print(f"这是一个{str1}字")
        #  全局变量定义在函数里
        i = 30
        return i  # 函数有默认的返回值None

i = i + 1
print(i)
str2 = "孙"
# x = fun1(str2)
i = i + 1
print(i)

