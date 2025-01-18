import requests
import re
import os
if __name__ == '__main__':
    if not os.path.exists('./imgs'):
        os.mkdir('./imgs')
    # url = "https://kyfw.12306.cn/otn/leftTicket/query"
    url = "https://www.163.com/dy/article/DF8283SH0517A1KR.html"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }

    reg = '<p class="f_center"><img src="(.*?)"/><br/></p>'
    response = requests.get(url=url,headers=headers).text
    lists = re.findall(reg,response,re.S)
    for num,url1 in enumerate(lists):
        cont = requests.get(url=url1, headers=headers).content
        with open('./imgs/'+str(num)+'.jpeg','wb') as fp:
            fp.write(cont)

    print("write over!!!")
