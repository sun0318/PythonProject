import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import urllib.request


def download_video():
    url = url_entry.get()

    try:
        # 发送GET请求获取网页内容
        response = requests.get(url)

        # 检查请求是否成功
        if response.status_code == 200:
            # 使用BeautifulSoup解析网页内容
            soup = BeautifulSoup(response.text, 'html.parser')

            # 找到视频链接
            video_link = soup.find('video')['src']

            # 提取视频文件名
            video_name = video_link.split('/')[-1]

            # 下载视频文件
            urllib.request.urlretrieve(video_link, video_name)

            messagebox.showinfo("Success", "视频下载成功！")
        else:
            messagebox.showerror("Error", "无法获取网页内容！")

    except Exception as e:
        messagebox.showerror("Error", f"下载视频失败：{e}")


# 创建主窗口
root = tk.Tk()
root.title("视频下载器")

# 创建标签和输入框
url_label = tk.Label(root, text="输入网址：")
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = tk.Entry(root, width=40)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# 创建下载按钮
download_button = tk.Button(root, text="下载视频", command=download_video)
download_button.grid(row=1, column=0, columnspan=2, pady=10)

# 运行主循环
root.mainloop()
