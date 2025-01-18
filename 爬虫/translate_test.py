import requests
import json
if __name__ == "__main__":
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }

    url = "https://fanyi.baidu.com/sug"
    word = input("要查询的单词:")
    param = {
        "kw" : word
    }

    response = requests.post(url=url,data=param,headers=headers)
    jsonText = response.json()
    fileName = word + ".txt"
    fp = open(fileName,"w",encoding="utf-8")
    # print(jsonText)
    json.dump(jsonText,fp=fp,ensure_ascii=False)