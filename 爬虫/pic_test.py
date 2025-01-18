import os
import requests
import re
if __name__ == "__main__":
    url = "https://www.biedoul.com/t/57OX5Zu%2B5aSn5YWo.html"
    # 反爬策略
    headers ={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    param = {
        "page":1,
        "searchid":1710
    }
    if not os.path.exists('./images'):
        os.mkdir('./images')
    response = requests.get(url=url,headers=headers)
    page_text = response.text
    result_list = re.findall('<br /><img src="(.*?)" alt=.*?>',page_text,re.S)
    for i in result_list:
        file_name = i.split('/')[-1]
        img_path = "./images/"+file_name
        img_res = requests.get(i, headers=headers).content
        with open(img_path,"wb",) as fp:
            fp.write(img_res)
            print(file_name + '下载成功!!')

    # print(result_list)
    # fileName = "request.html"
    # with open(fileName,'w',encoding="UTF-8") as fp:
    #     fp.write(page_text)
    # print(fileName,'保存成功！！！')