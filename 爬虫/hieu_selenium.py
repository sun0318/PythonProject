from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

# 创建Service对象，指定ChromeDriver的路径（这里假设在当前目录下名为chromedriver.exe）
service = Service(executable_path='./chromedriver.exe')

# 创建Chrome浏览器实例，传入Service对象
# chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
bro = webdriver.Chrome(service=service, options=chrome_options)
bro.get("http://jy.hieu.edu.cn/module/jobfairs")
# a = bro.find_element(by="xpath",value='//*[@id="data_html"]/li[1]/div/div[2]/p[1]/a')
# 一定要等加载完后，才能获取元素
sleep(3)
b = bro.find_element(by="xpath",value='//*[@id="data_html"]').find_elements(by ="class name" ,value="item-link")

print(len(b))
sleep(1)
# 在xpath中途获取元素时，要用*好
for i in range(10):
    bro.find_element(by="xpath",value='/html/body/div[3]/div/div/div[2]/div/div[4]/div/div[1]/ul/*[@class="paginationjs-next J-paginationjs-next"]').click()
    b=bro.find_element(by="xpath",value='//*[@id="data_html"]').find_elements(by="class name",value="item-link")
    for c in b:
        print(c.text)
    sleep(2)
bro.close()