import requests
import os
res = requests.get(
    url="https://gimg3.baidu.com/search/src=http%3A%2F%2Fgips0.baidu.com%2Fit%2Fu%3D2278820839%2C141979975%26fm%3D3030%26app%3D3030%26f%3DJPEG%3Fw%3D121%26h%3D74%26s%3D68C7E916B7C06CE056D190F603005031&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=f242,150&n=0&g=0n&q=100&fmt=auto?sec=1707152400&t=dad4fb33a014f91450de105a1acb7218",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
)
with open("image.csv", mode="rt" ,encoding="utf-8") as f:
    # 忽略第一行
    f.readline()
    for line in f:
        split_info = line.split(",")
        name = split_info[1].strip()
        image_url = split_info[2].strip()
        res = requests.get(
            url=image_url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
        )
        if not os.path.exists("images"):
            os.makedirs("images")
        with open("images/{}.jpg".format(name), mode="wb") as image_file:
            image_file.write(res.content)
            image_file.flush()


