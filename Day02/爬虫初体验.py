# 下载requests工具
# pip install requests

import requests

res = requests.get(
    url="https://www.baidu.com/",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
)

file = open("baidu.html",mode="wb")
file.write(res.content)