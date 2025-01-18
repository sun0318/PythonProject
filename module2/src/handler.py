"""
有video.csv视频库文件，其中有999条短视频数据，格式如下：【 video.csv 文件已为大家提供好，在day15课件目录下。 】
项目的核心功能有：
分页看新闻（每页显示10条），提示用户输入页码，根据页码显示指定页面的数据。
  - 提示用户输入页码，根据页码显示指定页面的数据。
  - 当用户输入的页码不存在时，默认显示第1页
搜索专区
- 用户输入关键字，根据关键词筛选出所有匹配成功的短视频资讯。
- 支持的搜索两种搜索格式：
   `id=1715025`，筛选出id等于1715025的视频（video.csv的第一列）。
   `key=文本`，模糊搜索，筛选包含关键字的所有新闻（video.csv的第二列）。
下载专区
- 用户输入视频id，根据id找到对应的mp4视频下载地址，然后下载视频到项目的files目录。
   视频的文件名为：`视频id-年-月-日-时-分-秒.mp4`
   视频下载代码示例
"""

import re
from src.service import download,page,search

# 读取文件，装在字典容器里，python3.6后，字典是有序的
def read_data():
    with open("db/video.csv", mode="rt", encoding="utf-8") as f:
        id_dict = dict()
        text = f.readlines()
        for line in text:
            id_num = line.split(",")[0]
            content = re.findall(r'\d+,(.*?),https',line)
            website = re.findall(r"https://\S+",line)
            id_key = dict()
            id_key["content"] = content[0]
            id_key["website"] = website[0]
            id_dict[id_num] = id_key
    return id_dict
# 功能区

def run():
    id_dict = read_data()
    func_num = input("请选择功能区：1.分页看新闻 2.搜索专区 3.下载专区\n")
    if func_num == "1":
        page.news(id_dict)
    elif func_num == "2":
        search.search(id_dict)
    elif func_num == "3":
        download.download(id_dict)
    else:
        print("输入有误，已退出")



