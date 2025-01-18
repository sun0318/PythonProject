import requests
import json
if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    param = {
        "type": "11",
        "interval_id": "100:90",
        "action":"",
        "start":"1",
        "limit": "20"
    }
    response = requests.get(url=url,params=param,headers=headers)
    print(response.content)
    # data_json = response.json()
    # fp = open("douban.json","w",encoding="utf-8")
    # json.dump(data_json,fp=fp,ensure_ascii=False)
    # print("over!!!")