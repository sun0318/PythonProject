class Record:
    date = None
    id = None
    money = 0
    province = None

    def __init__(self, date, id, money, province):
        self.date = date            # 日期
        self.id = id                # 订单号
        self.money = money          # 销售额
        self.province = province    # 省份

    def __str__(self):
        return f"{self.date, self.id, self.money, self.province}"
