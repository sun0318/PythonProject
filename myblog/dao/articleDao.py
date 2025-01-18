from PythonProject.myblog.utils.db import Connect
from datetime import datetime
def publish_article(title,text,user_id):
    # id,title,text,read_count,comment_count,up_count,down_count,user_id,ctime
    sql = "insert into article(title,text,user_id,ctime) values (%s,%s,%s,%s)"
    with Connect() as conn:
        result = conn.exec(sql,title,text,user_id,datetime.now())
        conn.conn.commit()
        return result

def view_article(limit,offset):
    sql = "select id,title from article order by id desc limit  %s offset %s"
    with Connect() as conn:
        result = conn.fetch_all(sql,limit,offset)
        return result

def total_article_count():
    sql = "select count(1) as total_count from article"
    with Connect() as conn:
        result = conn.fetch_one(sql)
        if not result:
            return 0
        else:
            return result["total_count"]

def view_one_article(id):
    sql = "select title,text from article where id = %s"
    with Connect() as conn:
        result = conn.fetch_one(sql,id)
        return result

def update_view_count(id):
    sql = "update article set read_count=read_count+1 where id=%s"
    with Connect() as conn:
        result = conn.exec(sql, id)
        conn.conn.commit()
        return result

def add_comment(content,user_id,article_id,ctime):
    with Connect() as conn:
        try:
            sql = "insert into comment(content,user_id,article_id,ctime) values (%s,%s,%s,%s)"
            conn.exec(sql, content,user_id,article_id,ctime)

            upsql = "update article set comment_count=comment_count+1 where id=%s"
            conn.exec(upsql,article_id)
            conn.conn.commit()
            return True
        except Exception as e:
            conn.conn.rollback()
            raise e

def up(user_id,article_id):
    with Connect() as conn:
        try:
            sql = "insert into up_down(user_id,article_id,choice,ctime) values(%s,%s,1,%s)"
            conn.exec(sql,user_id,article_id,datetime.now())

            upsql = "update article set up_count = up_count+1 where id = %s"
            conn.exec(upsql,article_id)
            conn.conn.commit()
        except Exception as e:
            conn.conn.rollback()
            raise e

def down(user_id,article_id):
    with Connect() as conn:
        try:
            sql = "insert into up_down(user_id,article_id,choice,ctime) values(%s,%s,0,%s)"
            conn.exec(sql,user_id,article_id,datetime.now())

            upsql = "update article set down_count = down_count+1 where id = %s"
            conn.exec(upsql,article_id)
            conn.conn.commit()
        except Exception as e:
            conn.conn.rollback()
            raise e

def selectchoice(user_id,article_id):
    with Connect() as conn:
        sql = "select choice from up_down where user_id = %s and article_id = %s"
        result = conn.fetch_one(sql,user_id,article_id)
        if result:
            return result["choice"]

def up_to_down(user_id,article_id):
    with Connect() as conn:
        sql = "update up_down set choice = '0' where user_id=%s and article_id=%s"
        conn.exec(sql, user_id, article_id)

        upsql = "update article set up_count=up_count-1 , down_count = down_count+1 where user_id=%s and id=%s"
        conn.exec(upsql,user_id,article_id)
        conn.conn.commit()
        return True

def down_to_up(user_id,article_id):
    with Connect() as conn:
        sql = "update up_down set choice = '1' where user_id=%s and article_id=%s"
        conn.exec(sql,user_id,article_id)

        upsql = "update article set up_count=up_count+1 , down_count = down_count-1 where user_id=%s and id=%s"
        conn.exec(upsql, user_id, article_id)
        conn.conn.commit()
        return True

if __name__ == "__main__":
    # publish_article("标题","内容","1")
    add_comment("pinglun","1","1",datetime.now())