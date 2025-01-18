import json

from record_define import Record


class FileReader:

    def read_data(self) -> list[Record]:
        pass


class TextFileReader:

    def __init__(self, path):
        self.path = path

    # 复写父类方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list(Record) = []
        for line in f.readlines():
            line = line.strip()
            split_list = line.split(",")
            date = split_list[0]
            id = split_list[1]
            money = int(split_list[2])
            province = split_list[3]
            record = Record(date, id, money, province)
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader:

    def __init__(self, path):
        self.path = path

    # 复写父类方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = json.loads(line)
            date = line["date"]
            id = line["order_id"]
            money = int(line["money"])
            province = line["province"]
            record = Record(date, id, money, province)
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    textReader = TextFileReader("2011年1月销售数据.txt")
    json_file = JsonFileReader("2011年2月销售数据JSON.txt")
    record_data1 = textReader.read_data()
    record_data2 = json_file.read_data()
    # for i in record_data1:
    #     print(i)

    for j in record_data2:
        print(j)
