"""
str1 = ["Ask","ss","333"]
str2 = ["Ask","ss","333"]
str3 = ["Ask","ss","333"]
# aaa = hash(str1)
# for i,data in enumerate(str1,1):
#     print(i,data)
result = zip(str3,str2,str1)
for item in result:
    print(item)
"""

"""
"""
# number_list = (i for i in range(10))
# print(number_list.send(None))
# print(number_list.send(3))
# print(number_list.send(4))

# def test(listdata):
#     listdata.append(1)
#
# a= [1,2,3]
# b= [1,2,3]
# # test(a)
# print(a)
# print(id(a),id(b))

# def func(*args,**kwargs):
#     # args[0].append(1)
#     print(args,kwargs)
#
# def func1(**kwargs):
#     print(kwargs)
# city = [1,2,3]
# def father():
#     global city
#     city = [2,3,4,5]
#     x = 10
#     def son():
#         nonlocal x
#         x = x+20
#         print(x)
#     son()

# father()
# a = {"k":1}
# b = [1,2]
# func(*b,**a)
# print(b)
# func1(a=1)
# father()
# print(city)

# def outter(origin):
#     def inner():
#         print("begin")
#         res = origin()
#         print("end")
#         return res
#     return inner
#
# @outter
# def func():
#     print("test")
#     pass
#
# func()

# def func():
#     name = '武沛齐'
#     def inner():
#         print(name)
#         return '路飞'
#     return inner
#
# v11 = func()
# data = v11()
# print(data)
#
#
# v2 = func()()
# print(v2)

# from concurrent.futures.thread import ThreadPoolExecutor
#
# import requests
#
#
# def download_video(url):
#     res = requests.get(
#         url=url,
#         headers={
#             "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
#         }
#     )
#     return res.content
#
#
# def outer(file_name):
#     def write_file(response):
#         content = response.result()
#         with open(file_name, mode='wb') as file_object:
#             file_object.write(content)
#
#     return write_file
#
#
# POOL = ThreadPoolExecutor(10)
#
# video_dict = [
#     ("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
#     ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
#     ("罗斯mvp.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
# ]
# for item in video_dict:
#     future = POOL.submit(download_video, url=item[1])
#     future.add_done_callback(outer(item[0]))
#
# POOL.shutdown()

# from concurrent.futures.thread import ThreadPoolExecutor
# import time
#
# def cal_time():
#     return time.time()
#
# def call_back(arg):
#     result = arg.result()
#     print(result)
#
# POOL = ThreadPoolExecutor(10)
#
# for i in range(3):
#     future = POOL.submit(cal_time)
#     future.add_done_callback(call_back)

# data_list = [ lambda x:x+100,  lambda x:x+110, lambda x:x+120 ]
#
# print( data_list[0] )
# b = lambda x:x+1
# a= all([1,2,3,0])
# print(a)
# print(b(2))

# import os
# a =os.walk("D:\PycharmProjects\PythonProject")
# print(os.walk.__doc__)
# # for path,folder_list,file_list in a:
# #
# #     print(folder_list)

import re

text = "逗2B最逗3B欢乐"
data = re.finditer("\dB", text)
for item in data:
    print(item.group())