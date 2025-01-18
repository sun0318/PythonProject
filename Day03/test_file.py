import sys
import io
from urllib import request

def simulate_login():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

    # 登录后才能访问的网站
    url = 'https://blog.csdn.net/m0_37952030/article/details/78304088'

    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    # cookie_str = r"VTP_CODE=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VyRGV0YWlscyI6eyJVc2VybmFtZSI6IjEiLCJQYXNzd29yZCI6IiIsIkF1dGhvcml0aWVzIjoiIn0sIkNsaWVudERldGFpbHMiOnsiQ2xpZW50SWQiOiJaSzNZcEZ1Q1hHOUlZcGtZN0lodGhiYm1tbHhPRVNMTWl3dnZPZzU1Wk1JPSIsIkF1dGhvcml6ZWRHcmFudFR5cGVzIjoiIn0sImV4cCI6MTYzMjM0MjcxOSwiaXNzIjoidnRwIn0.OX-u7geGpdCTmV9g35peJ77fUXxaGxSZsYBJ0s20cxg"
    #
    # # 登录后才能访问的网页
    # url = 'http://10.7.185.55:9000/#/plat'

    req = request.Request(url)
    # 设置cookie
    # req.add_header('cookie', cookie_str)
    # 设置请求头
    req.add_header('User-Agent',
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML"
                   ", like Gecko) Chrome/89.0.4389.90 Safari/537.36")

    resp = request.urlopen(req)

    print(resp.read().decode('utf-8'))

if __name__=='__main__':
    simulate_login()