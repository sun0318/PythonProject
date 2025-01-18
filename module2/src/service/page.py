# 看新闻
def news(id_dict):
    while True:
        page_id = input("请输入要搜索的页码(q/Q 退出):\n").strip()
        if page_id.upper() == "Q":
            print("已退出！")
            return
        if not page_id.isdecimal():
            page_id = 1
        page_id = int(page_id)
        begin_id = (page_id * 10) - 10
        end_id = page_id * 10 + 1
        for i, (key, value) in enumerate(id_dict.items(), 1):
            if end_id > i > begin_id:
                print(i, id_dict[key]["content"])
