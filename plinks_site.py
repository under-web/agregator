import requests
from bs4 import BeautifulSoup
import re
#вынимает все ссылки из сайта новостей


url = "https://www.rbc.ru/"


r = requests.get(url)
soup = BeautifulSoup(r.text , 'lxml')


pages = soup.find_all('a', href=re.compile('www')) #находит ссылки с атрибутом "www" в атрибутах с тегом href

for a in pages:
 links = a.get('href') # цикл построчно взять элемент href
 print(links)


