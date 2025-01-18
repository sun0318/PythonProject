from PythonProject.myblog.utils.db import Connect
from PythonProject.myblog.entity.User import User
from datetime import datetime

def register(user):
    sql = "insert into user(username,nickname,mobile,password,email,ctime) values (%s,%s,%s,%s,%s,%s)"
    with Connect() as conn:
        result = conn.exec(sql,user.username,user.nickname,user.mobile,user.password,user.email,user.ctime)
        conn.conn.commit()
        return result

def login(username,password):
    sql = "select id,nickname from user where username=%s and password=%s"
    with Connect() as conn:
        result = conn.fetch_one(sql,username,password)
        conn.conn.commit()
        return result


if __name__ == "__main__":
    # user = User("ask","aaa","1111111","2222222","12321312",datetime.now())
    # register(user)
    print(login("ask","2222222"))