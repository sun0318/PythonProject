# import re
# import requests
# from bs4 import BeautifulSoup
#
# res = requests.get(
#     url="https://tieba.baidu.com/p/8862768593?da_from=ZGFfbGluZT1EVCZkYV9wYWdlPTEmZGFfbG9jYXRlPXAwMDY0JmRhX2xvY19wYXJhbT0xJmRhX3Rhc2s9dGJkYSZkYV9vYmpfaWQ9Mzc1NTImZGFfb2JqX2dvb2RfaWQ9NTgwMjgmZGFfdGltZT0xNzA4MTc0NzQ3&da_sign=f1ec0cb2c10e07774c4d1e6bea33b7b5&tieba_from=tieba_da",
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
#     }
# )
# bs_object = BeautifulSoup(res.text, "html.parser")
# # print(bs_object.text)
# comment_object_list = bs_object.find_all("div", attrs={"class": "reply-content"})
# for comment_object in comment_object_list:
#     text = comment_object.text
#     print(text)
#     # 请继续补充代码，提取text中的邮箱地址

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 发送 HTTP 请求获取网页内容
url="https://tieba.baidu.com/p/8862768593?da_from=ZGFfbGluZT1EVCZkYV9wYWdlPTEmZGFfbG9jYXRlPXAwMDY0JmRhX2xvY19wYXJhbT0xJmRhX3Rhc2s9dGJkYSZkYV9vYmpfaWQ9Mzc1NTImZGFfb2JqX2dvb2RfaWQ9NTgwMjgmZGFfdGltZT0xNzA4MTc0NzQ3&da_sign=f1ec0cb2c10e07774c4d1e6bea33b7b5&tieba_from=tieba_da"
response = requests.get(url)

# 使用 Beautiful Soup 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 提取评论内容
comments = []
comment_elements = soup.find_all('div', class_='d_post_content j_d_post_content')  # 假设评论的 HTML 结构是 <div class="comment">
print(comment_elements)
for comment_element in comment_elements:
    comment_text = comment_element.text  # 假设评论文本的标签是 <p class="comment-text">
    comments.append(comment_text)

# 将评论数据存储到 DataFrame 中
comments_df = pd.DataFrame({'comment': comments})

# 打印前几条评论
print(comments_df.head())
