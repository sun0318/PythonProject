# import requests
# res = requests.get(url="http://www.weather.com.cn/data/ks/101010100.html")
# res.encoding = "utf-8"
# weather_dict = res.json()
#
# # 获取的天气信息是个字典类型，内容如下：
# print(weather_dict)

"""
{
    'weatherinfo': {
        'city': '北京', 
        'cityid': '101010100', 
        'temp': '18', 
        'WD': '东南风', 
        'WS': '1级', 
        'SD': '17%', 
        'WSE': '1', 
        'time': '17:05', 
        'isRadar': '1', 
        'Radar': 'JC_RADAR_AZ9010_JB', 
        'njd': '暂无实况', 
        'qy': '1011', 
        'rain': '0'
    }
}
"""

import requests


def write_file(**kwargs):
    """将天气信息拼接起来，并写入到文件
    格式要求：
        1. 每个城市的天气占一行
        2. 每行的格式为：city-北京,cityid-101010100,temp-18...
    """
    # 补充代码
    data_list = list()
    for key ,value in kwargs.items():
        data = "{}-{}".format(key,value)
        data_list.append(data)
    print(data_list)

def get_weather(code):
    """ 获取天气信息 """
    url = "http://www.weather.com.cn/data/ks/{}.html".format(code)
    res = requests.get(url=url)
    res.encoding = "utf-8"
    weather_dict = res.json()
    return weather_dict


city_list = [
    {'code': "101020100", 'title': "上海"},
    {'code': "101010100", 'title': "北京"},
]
for city in city_list:
    code = city['code']
    result = get_weather(code)
    write_file(**result['weatherinfo'])

# 补充代码
