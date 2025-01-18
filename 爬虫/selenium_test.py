from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

# 创建Service对象，指定ChromeDriver的路径（这里假设在当前目录下名为chromedriver.exe）
service = Service(executable_path='./chromedriver.exe')

# 创建Chrome浏览器实例，传入Service对象
chrome_options = webdriver.ChromeOptions()
bro = webdriver.Chrome(service=service, options=chrome_options)
bro.get("https://www.baidu.com/")
text = bro.page_source
print(text)
sleep(5)
bro.close()