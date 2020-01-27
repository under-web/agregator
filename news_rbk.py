import requests
from bs4 import BeautifulSoup
#Пишем новостной парсер

url = "https://rt.rbc.ru/"
url2 = "https://svpressa.ru/society/article/255256/"
url3 = "https://lenta.ru/news/2020/01/27/million/"
url4 = "https://ria.ru/location_Russia/"
url5 = "https://www.vesti.ru/news/"

r = requests.get(url)
r2 = requests.get(url2)
r3 = requests.get(url3)
r4 = requests.get(url4)
r5 = requests.get(url5)

soup = BeautifulSoup(r.text, 'lxml')
soup2 = BeautifulSoup(r2.text, 'lxml')
soup3 = BeautifulSoup(r3.text, 'lxml')
soup4 = BeautifulSoup(r4.text, 'lxml')
soup5 = BeautifulSoup(r5.text, 'lxml')

#https://rt.rbc.ru/
print("-------------------------Agregator_news 1.1-----------------------------------")
print()
print()
print()
print()

print(soup.find('span', class_= "main__big__title").text, "(РБК)") #взял через плагин "show html"
print(soup2.find('h1', class_= "b-text__title").text, "(Свободная пресса)")
print(soup3.find('h1', class_= "b-topic__title").text, "(Лента.ру)")
print(soup4.find('a', class_= "list-item__title color-font-hover-only").text, "(Риа новости)")
print(soup5.find('h3', class_="b-item__title").text, "(Вести)")
print()
print()
print()
print()
print("-------------------------------------------------------------------------")
