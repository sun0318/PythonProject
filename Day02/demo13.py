my_dict = {
    "name": "Ask",
    "age": 20,
    "gender": "male",
    "hobby": {"hot": "music", "normal": "drawing"}
}
# 取值方法1
x = my_dict.get("nam",1)
print(x)

my_set = {"1","2"}
my_set.update("1","3")
print(my_set)