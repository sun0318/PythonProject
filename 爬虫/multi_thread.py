# 环境安装：pip install aiohttp
# 使用该模块中的ClientSession
import requests
import asyncio
import time
import aiohttp

start = time.time()
# urls = [
#     'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom',
#     'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom',
#     'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom',
#     'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom',
#
# ]
from multiprocessing.dummy import Pool

pool = Pool(2)

urls = []
for i in range(3):
    urls.append('https://www.baidu.com')
print(urls)


async def get_page(url):
    async with aiohttp.ClientSession() as session:
        # get()、post():
        # headers,params/data,proxy='http://ip:port'
        async with await session.get(url) as response:
            # text()返回字符串形式的响应数据
            # read()返回的二进制形式的响应数据
            # json()返回的就是json对象
            # 注意：获取响应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
            print(len(page_text))
            return "下载完了"

# 返回的是task内部的协程的返回值，也就是c这个协程，也就是调用了get_page这个函数的返回值“下载完了”
def callback_func(task):
    print(task.result())

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(callback_func)
    tasks.append(task)

loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.wait(tasks))

end = time.time()

print('总耗时:', end - start)

