# class test:
#     def func(self,content):
#         print(content)
#
# test1 = test()
# test1.func("测试")
"""
# 需求
1. while循环提示 户输 : 户名、密码、邮箱(正则满足邮箱格式)
2. 为每个用户创建一个个对象，并添加到user_list中。
3. 当列表中的添加 3个对象后，跳出循环并以此循环打印所有用户的姓名和邮箱
"""


# import re
# import hashlib
# class person():
#     def __init__(self, user,pwd,email):
#         self.user = user
#         self.pwd = pwd
#         self.email = email
#
#     def encrypt(self,pwd):
#         origin_bytes = pwd.encode('utf-8')
#         md5_object = hashlib.md5()
#         md5_object.update(origin_bytes)
#         return md5_object.hexdigest()
#
#     def run(self):
#         user_list = []
#         while True:
#             if len(user_list) == 1:
#                 break
#             user = input("请输入用户名:")
#             pwd = input("请输入密码:")
#             email = input("请输入邮箱:")
#             if not re.match("^\d+@[0-9a-z]+\.[a-z]+$", email):
#                 print("邮箱格式有误")
#                 continue
#             new_person = person(user, pwd, email)
#             pwd = new_person.encrypt(pwd)
#             new_person.pwd = pwd
#             user_list.append(new_person)
#
#         for users in user_list:
#             print(users.user, users.pwd, users.email)
#
#     if __name__ == "__main__":
#         run()


class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = []

    def login(self):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        name = input("请输入用户名:")
        pwd = input("请输入密码:")
        flag = False
        for person in self.user_list:
            if person.name == name and person.pwd == pwd:
                flag = True
                break
        if flag:
            print("登录成功")
        else:
            print("登录失败")

    def register(self):
        """
        用户注册，没注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        name = input("请输入用户名:")
        pwd = input("请输入密码:")
        new_user = user(name, pwd)
        self.user_list.append(new_user)
        print("注册成功")

    def run(self):
        """
        主程序
        :return:
        """
        method_dict = {
            "1": {"title": "用户注册", "method": self.register},
            "2": {"title": "用户登录", "method": self.login},
        }
        message = ";".join(["{}.{}".format(k, v["title"]) for k, v in method_dict.items()])
        while True:
            print(message)
            choice = input("请选择功能")
            if choice.upper() == "Q":
                print("已退出")
                break
            info = method_dict.get(choice)
            if not info:
                print("选择有误，请重新选择！")
                continue
            info["method"]()


class user():
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


if __name__ == '__main__':
    obj = Account()
    obj.run()
