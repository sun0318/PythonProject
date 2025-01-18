"""
1.  基于csv格式实现 用户的注册 & 登录认证。详细需求如下：

    *   用户注册时，新注册用户要写入文件csv文件中，输入Q或q则退出。
    *   用户登录时，逐行读取csv文件中的用户信息并进行校验。
    *   提示：文件路径须使用os模块构造的绝对路径的方式。

"""
import shutil
import os
import sys

action = input("请选择您要执行的操作：1、注册 2、登录 其他:退出")
# 用户注册时，新注册用户要写入文件csv文件中，输入Q或q则退出。
if action == "1":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir,'user_info.csv')
    f = open(file_path, mode="a",encoding="utf-8")
    while True:
        name = input("请输出要注册的用户名：(输入q/Q退出)：")
        if (name.upper() == 'Q'):
            break
        f.write("{}\n".format(name))
        f.flush()
    f.close()
# 用户登录时，逐行读取csv文件中的用户信息并进行校验。
elif action == "2":
    name = input("欢迎登录，请输入用户名：(输入q/Q退出)")
    if (name.upper() == 'Q'):
        sys.exit()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'user_info.csv')
    f = open(file_path, mode="r", encoding="utf-8")
    success_flag = False
    for line in f:
        if name == line.strip():
            success_flag = True
            break
    if success_flag:
        print("恭喜'{}',登录成功".format(name))
    else:
        print("对不起登录失败，未找到'{}'用户".format(name))
    f.close()
else:
    pass
