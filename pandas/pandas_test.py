import pandas as pd
import pymysql

# fpath = "pandas_test.xlsx"
# excel_data = pd.read_excel(fpath)
# print(excel_data)

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database= "py_sql",
    autocommit=True
)

mysql_result = pd.read_sql("select * from orders", con=conn)
print(mysql_result)
