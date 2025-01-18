# 遇到文字做修改的方式不可取(rt+)，不可取

# 方法一，小文件可以全读出来，修改内容后再写
# data_read = ""
# with open("ha.conf", mode="r", encoding="utf-8") as fr:
#     data_read = fr.read()
#     data_read = data_read.replace("luffycity","pythonav")
#
# with open("ha.conf", mode="w", encoding="utf-8") as fw:
#     fw.write(data_read)
#     fw.flush()

# 方法二，大文件同时操作两个文件，一边读，一边写
with open("ha.conf", mode="r", encoding="utf-8") as fr,open("newha.conf", mode="w", encoding="utf-8") as fw:
    for line in fr:
        new_line = line.replace("luffycity","pythonav")
        fw.write(new_line)

# 重命名
import shutil

shutil.move("newha.conf","ha.conf")