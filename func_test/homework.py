# 1.  请定义一个函数，用于计算一个字符串中字符`a`出现的次数并通过return返回。
#
#     *   参数，字符串。
#     *   返回值，字符串中 a 出现的次数。
# def count_a(str1):
#     return str1.count("a")
#
# print(count_a(input("请输入字符串：")))
# 2.  写函数，判断用户传入的一个值（字符串或列表或元组任意）长度是否大于5，并返回真假。

# def fun1(params):
#     print(params)
#     if len(params) > 5:
#         return True
#     else:
#         return False
#
# params1 = "8792329"
# params2 = [1,3,2,3]
# params3 = (1,2,5,35,2)
# print(fun1(params1))
# 3.  写函数，接收两个数字参数，返回比较大的那个数字（等于时返回两个中的任意一个都可以）。
# def fun2(x,y):
#     if x > y:
#         return x
#     else:
#         return y
# print(fun2(5,5))
# 4.  写函数，函数接收四个参数分别是：姓名，性别，年龄，学历，然后将这四个值通过"\*"拼接起来并追加到一个student\_msg.txt文件中。
# import os
# def fun3(*params):
#     params_str = "*".join(params)
#     abs_path = os.path.abspath(__file__)
#     base_path = os.path.dirname(os.path.dirname(abs_path))
#     path2 = os.path.join(base_path, "student")
#     is_dir2 = os.path.isdir(path2)
#     if not is_dir2:
#         os.makedirs(path2)
#     file_name = os.path.join(path2,"_msg.txt")
#     with open(file_name, mode="a", encoding="utf-8") as f:
#         f.write(params_str)
#
# fun3("Ask","男","19","本科")
# 5.  补充代码，实现如下功能：
#
#     *   【位置1】读取文件中的每一行数据，将包含特定关键的数据筛选出来，并以列表的形式返回。
#     *   【位置1】文件不存在，则返回None
#     *   【位置2】文件不存在，输出 "文件不存在"，否则循环输出匹配成功的每一行数据。
#
#     ```python
# import os
# def select_content(file_path,key):
#     # 补充代码【位置1】
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(base_dir, 'files', file_path)
#     print(file_path)
#     if not os.path.exists(file_path):
#         return None
#     data = list()
#     with open(file_path,mode="rt",encoding="utf-8") as f:
#         for line in f:
#             if key in line:
#                 data.append(line)
#     return data
# # 补充代码【位置2】
# #     ```
# result = select_content("stock.txt","股票")
# if result == None:
#     print("文件不存在")
# else:
#     print(result)

# 脱敏处理
# def change_string(origin):
#     result = origin
#     # 补充代码，将字符串origin中中的敏感词替换为 **，最后将替换好的值返回。
#     data_list = ["苍老师", "波多老师", "大桥"]
#     for word in data_list:
#         if word in origin:
#             result = result.replace(word,"**")
#     return result
#
# text = input("请输入内容：")
# result = change_string(text)
# print(result)

# import hashlib
#
# def encrypt(origin):
#     origin_bytes = origin.encode('utf-8')
#     md5_object = hashlib.md5()
#     md5_object.update(origin_bytes)
#     return md5_object.hexdigest()


# p1 = encrypt('admin')
# print(p1) # 21232f297a57a5a743894a0e4a801fc3
#
# p2 = encrypt('123123')
# print(p2) # "4297f44b13955235245b2497399d7a93"
#
# p3 = encrypt('123456')
# print(p3) # "e10adc3949ba59abbe56e057f20f883e"

# from openpyxl import load_workbook
# wb = load_workbook("files/user.xlsx")
# sheet = wb.worksheets[0]
# # print(sheet["A1"].value)
# row_num = 2
# # print(sheet.cell(row_num,2).value)
# name = input("请输入用户名:")
# password = input("请输入密码:")
# # 获取 A 列和 B 列的数据范围
# a_column = sheet['B'][1:]  # 从第二行开始获取 A 列的数据
# b_column = sheet['C'][1:]  # 从第二行开始获取 B 列的数据

# 循环读取数据
# for a_cell, b_cell in zip(a_column, b_column):
#     en_password = encrypt(password)
#     name2 = str(a_cell.value)
#     en_password2 = str(b_cell.value)
#     if(name == name2.strip() and en_password == en_password2.strip()):
#         print("登录成功")
#         break
# else:
#     print("用户名或密码错误")

# from openpyxl import load_workbook
# wb = load_workbook("files/user.xlsx")
# sheet = wb.worksheets[0]
# for i,rows in enumerate(sheet.rows,3):
#     print(rows[1].value,rows[2].value)

import os
abs_path = os.path.abspath(__file__)
print(abs_path)