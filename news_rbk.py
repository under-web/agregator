import requests
from bs4 import BeautifulSoup

url = "https://rt.rbc.ru/"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')
#https://rt.rbc.ru/

pages = soup.find('span', class_="main__big__title") #взял через плагин "show html"
print(pages)
