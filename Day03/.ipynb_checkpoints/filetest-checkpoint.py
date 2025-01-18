# f = open("../test1", 'r', encoding="UTF-8")
#  read(读取的字符数)，不填参数则是读取所有
# print(f.read(8))
#  readline(该行的字符数) 读一行的几个字符，不填参数则是整行
# print(f.readline())

# readlines() 读多行的数据，并以数组的形式返回
# print(f.readlines())

# 每一个line临时变量，就记录了文件的一行数据
# for line in open("../test1", "r", encoding="UTF-8"):
#     print(line)

# f.close()

# 通过在with open的语句块中对文件进行操作
# 可以在操作完成后自动关闭close文件，避免遗忘掉close方法

# with open("../test1", 'r', encoding="UTF-8") as f:
#     print(f.read(10))

# 判断文件中单词个数
# with open("word.txt", "r", encoding="UTF-8") as f:

    # 方法一，直接读取全部，用count函数判断单词个数
    # line = f.read()
    # print(line.count("itheima"))
    # count = 0
    # for line in f:
    #     line = line.strip()
    #     str_list = line.split(" ")
    #     print(str_list)
    #     for word in str_list:
    #         if word == "itheima":
    #             count = count + 1
    # print("itheima出现的次数是", count)

f1 = open("bill.txt", "r", encoding="UTF-8")
# 参数：w 写入，没有文件则会创建新文件，如果有则会覆盖
# 参数：a 追加，没有文件则会创建新文件，出国游则在后面追加内容
f2 = open("bill.bak.txt", "w", encoding="UTF-8")
for line1 in f1:
    if line1.count("测试") > 0:
        continue
    else:
        f2.write(line1)
        f2.flush()
f1.close()
f2.close()