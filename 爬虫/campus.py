import requests
# import xml
if __name__ == '__main__':
    # url = "https://kyfw.12306.cn/otn/leftTicket/query"
    url = "https://career.csu.edu.cn/"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    param = {
        # "leftTicketDTO.train_date": "2024-08-06",
        # "leftTicketDTO.from_station": "CSQ",
        # "leftTicketDTO.to_station": "SZQ",
        # "purpose_codes": "ADULT"
        "year":"2024",
        "month":"8"
    }
    response = requests.get(url=url,params=param,headers=headers)
    print(response.text)
    data_xml = response.text
    fp = open("center_south.txt","w",encoding="utf-8")
    fp.write(data_xml)
    print("over!!!")