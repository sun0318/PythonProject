import requests
import time
import re
# dict :{
#   id_num :
#       {
#           content:
#           website:
#       }
# }

id_dict = dict()
with open("files/video.csv",mode="rt",encoding="utf-8") as f:
    text = f.readlines()
    for i,line in enumerate(text,1):
        id_num = line.split(",")[0]
        content = re.findall(r'\d+,(.*?),https',line)
        website = re.findall(r"https://\S+",line)
        id_key = dict()
        id_key["content"] = content[0]
        id_key["website"] = website[0]
        id_dict[id_num] = id_key

for i,(key,value) in enumerate(id_dict.items(),1):
    if 20> i > 10 :
        print(i,key)







