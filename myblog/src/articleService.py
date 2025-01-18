import datetime

import PythonProject.myblog.dao.articleDao as articledao


def publish_article(user_id):
    # id,title,text,read_count,comment_count,up_count,down_count,user_id,ctime
    """
    发布文章
    :param title:
    :param text:
    :param user_id:
    :return:
    """
    title = input("请输入文章标题：")
    text = input("请输入文章内容：")
    articledao.publish_article(title, text, user_id)


def view_article(userid, offset=0):
    limit = 10
    pagenum = 1
    results = articledao.view_article(limit, offset)
    print("文章列表：")
    for result in results:
        print("    {id}. {title}".format(**result))
    while True:
        pageid = input("请输入要查看的文章id，输入P+页码表示翻页：")
        if pageid.upper() == "Q":
            break
        elif pageid.upper().startswith("P"):
            pagenum = int(pageid[1:])
            total_count = articledao.total_article_count()
            page_size, modnum = divmod(total_count, limit)
            if modnum > 0:
                page_size = page_size + 1
            if page_size == 0:
                print("没有数据")
                continue
            if page_size >= pagenum > 0:
                offset = (pagenum - 1) * limit
                print(pagenum, offset)
                results = articledao.view_article(limit, offset)
                print("文章列表：")
                for result in results:
                    print("    {id}. {title}".format(**result))
            else:
                continue
        else:
            if not pageid.isdecimal():
                print("输入有误！")
                continue
            else:
                result = articledao.view_one_article(pageid)
                print("{title}: {text}".format(**result))
            article_detail(userid, pageid)



def article_detail(user_id, article_id):
    def add_comment(user_id, article_id):
        content = input("评论：")
        articledao.add_comment(content, user_id, article_id, datetime.datetime.now())
        print("评论成功！")

    def up(user_id, article_id):
        choice = articledao.selectchoice(user_id, article_id)
        if not choice:
            articledao.up(user_id, article_id)
            print("成功点赞！")
            return

        if choice == 1:
            print("已点赞过了！")
            return
        elif choice == 0:
            articledao.down_to_up(user_id, article_id)

    def down(user_id, article_id):
        choice = articledao.selectchoice(user_id, article_id)
        if not choice:
            articledao.up(user_id, article_id)
            print("成功拉踩！")
            return

        if choice == 0:
            print("已点踩过了！")
            return
        elif choice == 1:
            articledao.up_to_down(user_id, article_id)
        print("成功拉踩!")

    action = input("1：评论    2：点赞    3：踩\n")
    if user_id == "" or user_id == None:
        print("请先登录后再评论 点赞 踩! ")
        return
    if action == "1":
        add_comment(user_id, article_id)
    elif action == "2":
        up(user_id, article_id)
    elif action == "3":
        down(user_id, article_id)


if __name__ == "__main__":
    view_article("1")
    # print("1".isdecimal())
