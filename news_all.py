import requests
from bs4 import BeautifulSoup
#Пишем новостной парсер

url = "https://rt.rbc.ru/"
url2 = "https://svpressa.ru/society/article/255256/"
url3 = "https://lenta.ru/news/2020/01/27/million/"
url4 = "https://ria.ru/location_Russia/"
url5 = "https://www.vesti.ru/news/"
url6 = "https://www.tatpressa.ru/"
url7 = "https://www.tatar-inform.ru/"
url8 = "https://ria.ru/location_Tatarstan/"
url9 = "http://bugulma-tatarstan.ru/"
#нужно написать функцию
r = requests.get(url)
r2 = requests.get(url2)
r3 = requests.get(url3)
r4 = requests.get(url4)
r5 = requests.get(url5)
r6 = requests.get(url6)
r7 = requests.get(url7)
r8 = requests.get(url8)
r9 = requests.get(url9)

soup = BeautifulSoup(r.text, 'lxml')
soup2 = BeautifulSoup(r2.text, 'lxml')
soup3 = BeautifulSoup(r3.text, 'lxml')
soup4 = BeautifulSoup(r4.text, 'lxml')
soup5 = BeautifulSoup(r5.text, 'lxml')
soup6 = BeautifulSoup(r6.text, 'lxml')
soup7 = BeautifulSoup(r7.text, 'lxml')
soup8 = BeautifulSoup(r8.text, 'lxml')
soup9 = BeautifulSoup(r9.text, 'lxml')

print("Agregator_news v1.3")
print()
print()
print()

print("------------------------Новости России------------------------------")
print()
print()
print()
print()

print(soup.find('span', class_= "main__big__title").text, "(РБК)") #взял через плагин "show html"
print(soup2.find('h1', class_= "b-text__title").text, "(Свободная пресса)")
print(soup3.find('h1', class_= "b-topic__title").text, "(Лента.ру)")
print(soup4.find('a', class_= "list-item__title color-font-hover-only").text, "(Риа новости)")
print(soup5.find('h3', class_= "b-item__title").text, "(Вести)")
print()
print("------------------------Новости татарстана----------------------------")
print()
print()
print(soup6.find('a', class_= "title").text, "(tatpressa)")
print(soup7.find('div', class_= "content").text, "(tatar-inform)")
print(soup8.find('a', class_= "list-item__title color-font-hover-only").text, "(РИА тат)")

print(soup9.find('a' , class_= "widget-topic__head").text, "(bugulma-tatarstan)")
print()
print()
print("-------------------------------------------------------------------------")
