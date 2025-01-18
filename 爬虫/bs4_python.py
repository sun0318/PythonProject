from bs4 import BeautifulSoup
import lxml
with open("zph.html",'r',encoding="utf-8") as fp:
    soup = BeautifulSoup(fp,"lxml")

a = soup.find('div',class_='modal-body').find('table').find_all('tr')[8].find('td').text
print(a)