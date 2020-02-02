import requests
from bs4 import BeautifulSoup
#Урок-пример
#вынимает  ссылку из сайта новостей и текст в первом блоке



url = "https://www.rbc.ru/"


r = requests.get(url)
soup = BeautifulSoup(r.text , 'lxml')


pages = soup.find('a', class_ = 'main__feed__link js-yandex-counter')# находим нужный блок по элементу "а" и классу main... 

link = pages.get('href') #берем с помощью get из обьекта 'pages' элемент 'href' 
ttext = pages.text  # берем текст из обьекта pages

print(ttext, link)
