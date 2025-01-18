from record_define import Record
from file_Define import TextFileReader, JsonFileReader
from pyecharts.charts import Bar

textReader: list[Record] = TextFileReader("2011年1月销售数据.txt").read_data()
json_file: list[Record] = JsonFileReader("2011年2月销售数据JSON.txt").read_data()

all_record: list[Record] = textReader + json_file

data_dict = {}
for record in all_record:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money


bar = Bar()
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()))
bar.render("每日销售额.html")