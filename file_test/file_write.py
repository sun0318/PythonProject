import requests

res = requests.get(
    url="https://gimg3.baidu.com/search/src=http%3A%2F%2Fgips0.baidu.com%2Fit%2Fu%3D2278820839%2C141979975%26fm%3D3030%26app%3D3030%26f%3DJPEG%3Fw%3D121%26h%3D74%26s%3D68C7E916B7C06CE056D190F603005031&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=f242,150&n=0&g=0n&q=100&fmt=auto?sec=1707152400&t=dad4fb33a014f91450de105a1acb7218",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
)

# 视频的文件内容

with open("test.jpg",mode="wb") as f:
    f.write(res.content)