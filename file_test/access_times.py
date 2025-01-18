with open("access.log", mode="rt", encoding="utf-8") as f:
    ip_dict = dict()
    for line in f:
        split_data = line.split("- -")
        ip = split_data[0].strip()
        # if ip == "223.73.89.192":
        #     i = i + 1
        value = ip_dict.get(ip,0)
        if value >= 0:
            value = value + 1
        ip_dict[ip] = value
print(ip_dict)

