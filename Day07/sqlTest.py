from pymysql import Connection
from file_Define import TextFileReader, JsonFileReader
from record_define import Record
from datetime import datetime

#  获取连接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)

# print(conn.get_server_info())
textRecord: list[Record] = TextFileReader("2011年1月销售数据.txt").read_data()
jsonRecord: list[Record] = JsonFileReader("2011年2月销售数据JSON.txt").read_data()
all_record: list[Record] = textRecord + jsonRecord
cursor = conn.cursor()
conn.select_db("py_sql")
for record in all_record:
    order_date = record.date
    order_id = record.id
    money = record.money
    province = record.province
    sql = f"INSERT INTO orders(order_date,order_id,money,province) " \
          f"VALUES ('{order_date}','{order_id}',{money},'{province}')"
    # print(sql)
    cursor.execute(sql)

# results: tuple = cursor.fetchall()
# for line in results:
#     print(line)
# 关闭数据库连接
conn.close()
