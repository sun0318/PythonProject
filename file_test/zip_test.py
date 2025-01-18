import shutil

import requests
import os

# 1.下载文件
file_url = 'https://files.cnblogs.com/files/wupeiqi/HtmlStore.zip'
res = requests.get(url=file_url)

# 2.将下载的文件保存到当前执行脚本同级目录下 /files/package/ 目录下（且文件名为HtmlStore.zip）
abs_path = os.path.abspath(__file__)
base_path = os.path.dirname( os.path.dirname(abs_path))
path = os.path.join(base_path,"files","package")
is_dir = os.path.isdir(path)
if not is_dir:
    os.makedirs(path)
file_name = file_url.split("/")[-1]
with open("{}/HtmlStore.zip".format(path), mode="wb") as f:
    f.write(res.content)
# 3.在将下载下来的文件解压到 /files/html/ 目录下

path2 = os.path.join(base_path,"files","html")
is_dir2 = os.path.isdir(path2)
if not is_dir2:
    os.makedirs(path2)

shutil.unpack_archive(filename=r'{}/HtmlStore.zip'.format(path), extract_dir=r"{}".format(path2), format='zip')