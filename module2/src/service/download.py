import requests
import time
import os
from datetime import datetime
# 下载专区
def download(id_dict):
    while True:
        search_id = input("请输入要下载的id(q/Q 退出):\n").strip()
        if search_id.upper() == "Q":
            print("已退出！")
            return
        url = id_dict.get(search_id)
        if not url:
            print("id输入有误，请重新输入")
            continue
        download_film(id_dict,search_id)

def download_film(id_dict,search_id):

    res = requests.get(
        url=id_dict[search_id]["website"]
    )

    # 视频总大小（字节）
    file_size = int(res.headers['Content-Length'])

    download_size = 0
    current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M")
    film_name = "{}-{}.mp4".format(search_id,current_datetime)
    # print(os.path.dirname(__file__))
    file_path = os.path.join(os.path.dirname(__file__),"..","..","files",film_name)
    print(file_path)
    with open(file_path, mode='wb') as file_object:
        # 分块读取下载的视频文件（最多一次读128字节），并逐一写入到文件中。 len(chunk)表示实际读取到每块的视频文件大小。
        for chunk in res.iter_content(128):
            download_size += len(chunk)
            file_object.write(chunk)
            file_object.flush()
            # message = "视频总大小为：{}字节，已下载{}字节。".format(file_size, download_size)
            # print(message)
        file_object.close()
    res.close()

    print("正在下载中...")
    for i in range(101):
        text = "\r{}%".format(i)
        print(text, end="")
        time.sleep(0.2)

    print("\n下载完成")