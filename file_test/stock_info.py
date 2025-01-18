# 方法一
# with open("stockinfo", mode="rt", encoding="utf-8") as f:
#     for line in f:
#         line_data = line.split(",")
#         if line_data[2].strip() == "当前价":
#             continue
#         current_price = float(line_data[2].strip())
#         if current_price > 20:
#             print(line_data)

# 方法二
with open("stockinfo", mode="rt", encoding="utf-8") as f:
    # 跳过第一行（读一行什么也不操作，让下标跳到第二行）
    f.readline()
    for line in f:
        line_data = line.split(",")
        current_price = float(line_data[2].strip())
        if current_price > 20:
            print(line_data)