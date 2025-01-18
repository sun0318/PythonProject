from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

# 创建Service对象，指定ChromeDriver的路径（这里假设在当前目录下名为chromedriver.exe）
service = Service(executable_path='./chromedriver.exe')

# 创建Chrome浏览器实例，传入Service对象
chrome_options = webdriver.ChromeOptions()
bro = webdriver.Chrome(service=service, options=chrome_options)
bro.get("https://www.luffycity.com/")

bro.find_element(by='class name',value='signin').click()
bro.find_element(by="class name",value="username").find_element(by="xpath",value="./input").send_keys("18273137409")
bro.find_element(by="class name",value="password").find_element(by="xpath",value="./input").send_keys("ask12345")
sleep(1)
bro.find_element(by="class name",value="popup-content").find_element(by="class name",value="signin").find_element(by="xpath",value="./button").click()

sleep(9)
# bro.save_screenshot('a.png')
# print(t)
bro.quit()

