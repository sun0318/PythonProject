
import requests
if __name__ == "__main__":
    url = "http://www.natcm.gov.cn/e/search/result/index.php"
    # 反爬策略
    headers ={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    param = {
        "page":1,
        "searchid":1710
    }
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    print(page_text)
    # fileName = "request.html"
    # with open(fileName,'w',encoding="UTF-8") as fp:
    #     fp.write(page_text)
    # print(fileName,'保存成功！！！')