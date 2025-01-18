import requests
if __name__ == "__main__":

    # 反爬策略
    headers ={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    for page in range(1,3):
        url = f"http://jy.hieu.edu.cn/module/getcareers?start_page=1&k=&panel_name=&type=inner&day=&panel_id=&professionals=&work_city=&is_yun_career=&count=15&start={page}"
        response = requests.get(url=url, headers=headers)
        page_text = response.json()
        data = page_text['data']
        for i in data:
            print(i['company_name'])