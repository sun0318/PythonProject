import json
# JSON可以直接和Python的字典或列表进行无缝转换。
data = [{"name": "老王", "age": 16}, {"name": "张三", "age": 20}]

# 列表转json ，ensure_ascii不使用ASCII码输出，中文正常输出
data = json.dumps(data, ensure_ascii=False)
print(data)

data = {"name": "张三", "age": 20}

# ensure_ascii不使用ASCII码输出，中文正常输出
data = json.dumps(data, ensure_ascii=False)
print(data)

# json定义，两层的冒号区分开来
data1 = '[{"name": "老王", "age": 16}, {"name": "张三", "age": 20}]'
data2 = '{"name": "张三", "age": 20}'
# loads方法 json转字符串
# l1 = json.loads(data1)
# l2 = json.loads(data2)
# print(type(l1))
# print(l1)
# print(type(l2))
# print(l2)

# dump(列表或字典数据,文件变量)将数据写到文件中
# data = [{"name": "老王", "age": 16}, {"name": "张三", "age": 20}]
# f = open("jsonData.txt", "a", encoding="UTF-8")
# json.dump(data, f, ensure_ascii=False)

# load(文件名，字符串名) json转字符串
f = open("jsonData.txt", "r", encoding="UTF-8")
aaa = json.load(f)
print("aaa",aaa)


# with open('jsonData.txt', 'r', encoding="UTF-8") as json_file:
#     data = json.load(json_file)
#
# print(data)