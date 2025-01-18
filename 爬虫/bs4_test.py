from bs4 import BeautifulSoup
import lxml
import requests

url ="https://career.cic.tsinghua.edu.cn/xsglxt/b/jyxt/anony/queryDzxzphxxlist"
headers ={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
a = """[{"name":"sEcho","value":1},{"name":"iColumns","value":9},{"name":"sColumns","value":""},{"name":"iDisplayStart","value":0},{"name":"iDisplayLength","value":-1},{"name":"mDataProp_0","value":"function"},{"name":"mDataProp_1","value":"zphqsrq"},{"name":"mDataProp_2","value":"zphzzrq"},{"name":"mDataProp_3","value":"zphdd"},{"name":"mDataProp_4","value":"kfbmrq"},{"name":"mDataProp_5","value":"bmjzrq"},{"name":"mDataProp_6","value":"zws"},{"name":"mDataProp_7","value":"sqrs"},{"name":"mDataProp_8","value":"function"}]"""
param = {'aoData': a
         }
response = requests.post(url=url,data=param,headers=headers)
res_json = response.json()
print(res_json)

s_lists = []
for s_li in res_json['aaData']:
    s_lists.append(s_li['zphid'])

print(s_lists)
for zphid in s_lists:
    inside_url = f"https://career.cic.tsinghua.edu.cn/xsglxt/f/jyxt/anony/viewDzxzph/{zphid}"
    response2 = requests.post(url=inside_url,headers=headers)
    soup = BeautifulSoup(response2.text, "lxml")
    a = soup.find('div', class_='modal-body').find('table').find_all('tr')[7].find('td').text
    print(a)
