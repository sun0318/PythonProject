import re

text = "abc\naabcdef\nghiabc"
# 未使用re.M时匹配^abc
result1 = re.findall(r'^abc', text)
print(result1)
# 使用re.M时匹配^abc
result2 = re.findall(r'^abc', text, re.M)
print(result2)

# 未使用re.M时匹配def$
result3 = re.findall(r'def$', text)
print(result3)
# 使用re.M时匹配def$
result4 = re.findall(r'def$', text, re.M)
print(result4)