# str1 = " 123456789   "
# print("str1长度=", len(str1))
# str1.strip()
# print("去除空格后str1长度=", len(str1))

# my_str = "12345"
# new_str = my_str[::-1]  # 从头（最后）开始，到尾结束，步长-1（倒序）
# print(new_str)		# 结果："54321"
#
# my_list = [1, 2, 3, 4, 5]
# new_list = my_list[3:1:-1]  # 从下标3开始，到下标1（不含）结束，步长-1（倒序）
# print(new_list)		# 结果：[4, 3]
#
# my_tuple = (1, 2, 3, 4, 5)
# new_tuple = my_tuple[:1:-2]  # 从头（最后）开始，到下标1(不含)结束，步长-2（倒序）
# print(new_tuple)		# 结果：(5, 3)

# str2 = "万过薪月，员序程马黑来，nohtyP学"
# new_str2 = str2[-10:4:-1]
# print(new_str2)

# 去除重复值，利用集合特性（不能有重复值）做去重处理
# my_list1 = [1, 2, 3, 4, 5, 1, 4]
# print(list(set(my_list1)))

import pandas as pd
import numpy as np

data = np.random.randint(0,100,size=(3,3))
index = pd.Index(data=list("ABC"))
column = pd.Index(data = list("abc"))

score = pd.DataFrame(data,index,column)
score = score.T
score.to_excel("test.xlsx")
print(score)

