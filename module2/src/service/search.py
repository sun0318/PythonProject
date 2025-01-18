import re
# 搜索专区
def search(id_dict):
    while True:
        search_id = input("请输入要搜索的id或内容(q/Q 退出):\n").strip()
        if search_id.upper() == "Q":
            print("已退出！")
            return
        if search_id.isdecimal():
            for key, value in id_dict.items():
                if key == search_id:
                    print(id_dict[key]["content"])
        else:
            for key, value in id_dict.items():
                if re.search(search_id,id_dict[key]["content"]):
                    print(id_dict[key]["content"])