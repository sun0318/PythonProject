# file1 = open("wt_file.txt",mode="r",encoding="UTF-8")
# data_content = file1.read()
# print(data_content)
# file1.close()
# file2 = open("wt_file.txt",mode="w",encoding="UTF-8")
# file2.write("萨克雷大嫁风尚骄傲拉开距离佛挡杀佛节点上"+data_content)
#
# file2.close()

#
# with open("wt_file.txt",mode="rb") as file1:
#     data_content = file1.read(1)
#     data_content = data_content.decode("utf-8")
#     print(data_content)

file1 = open("wt_file.txt",mode="x+",encoding="UTF-8")
file1.write("777777777777")
file1.flush()
file1.close()


