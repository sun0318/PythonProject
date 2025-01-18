"""
博客功能：
注册、登录
发表文章
评论文章、点赞、踩
"""

import src.accountService as account
import src.articleService as article

userInfo = dict()


class Handler(object):
    def run(self):
        title = "欢迎登录博客系统".center(50, "=")
        print(title)
        while True:
            menu = input("1.注册  2.登录  3.发布博客  4.查看博客列表\n")
            if menu.upper() == "Q":
                return
            if menu == "1":
                result = account.registerService()
                if result:
                    print("注册成功！")
            elif menu == "2":
                while True:
                    result = account.loginService()
                    if result:
                        userInfo["id"] = result["id"]
                        userInfo["nickname"] = result["nickname"]
                        print("登录成功！")
                        break
                    else:
                        print("用户不存在")
            elif menu == "3":
                article.publish_article(userInfo["id"])
            elif menu == "4":
                article.view_article(userInfo["id"])


handler = Handler()
handler.run()
