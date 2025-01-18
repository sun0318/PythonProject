import requests
import json
if __name__ == '__main__':
    # url = "https://kyfw.12306.cn/otn/leftTicket/query"
    url = "https://kyfw.12306.cn/lcquery/query"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    param = {
        # "leftTicketDTO.train_date": "2024-08-06",
        # "leftTicketDTO.from_station": "CSQ",
        # "leftTicketDTO.to_station": "SZQ",
        # "purpose_codes": "ADULT"
        "train_date": "2024-08-26",
        "from_station_telecode": "CSQ",
        "to_station_telecode": "SZQ",
        "result_index": "0",
        "can_query": "Y",
        "isShowWZ": "Y",
        "sort_type": "2",
        "purpose_codes": "00",
        "is_loop_transfer": "S",
        "channel": "E",
        "_json_att":""
    }
    response = requests.get(url=url,params=param,headers=headers)
    print(response.text)
    data_json = response.json()
    # fp = open("tickets.txt","w",encoding="utf-8")
    # json.dump(data_json,fp=fp,ensure_ascii=False)
    first_list = data_json['data']['middleList'][0]['fullList'][0]
    for key,value in first_list.items():
        print(key,':',value)

