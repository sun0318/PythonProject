import datetime

from PythonProject.myblog.entity.User import User
import PythonProject.myblog.dao.accountDao as accountdao
def loginService():
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username == None or password == None:
        print("用户名为空!")
        return None
    result = accountdao.login(username,password)
    return result


def registerService():
    """ 注册 """
    # username, nickname, mobile, password, email, ctime
    username = input("请输入用户名:")
    nickname = input("请输入昵称:")
    mobile = input("请输入手机号:")
    password = input("请输入密码:")
    email = input("请输入邮箱:")
    ctime = datetime.datetime.now()
    user = User(username, nickname, mobile, password, email, ctime)
    result = accountdao.register(user)
    return result


if __name__ == "__main__":
    print(registerService())
