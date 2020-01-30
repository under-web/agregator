import requests
from bs4 import BeautifulSoup

#вынимает все ссылки из сайта новостей


url = "https://www.rbc.ru/" #таргет


r = requests.get(url)                  #передаем урл в реквест через метод get
soup = BeautifulSoup(r.text , 'lxml')   #создаем обьект супа  парсим библиотекой lxml


pages = soup.find_all('a')  #ищем все элементы А

for a in pages:  #цикл построчно печатать 
	links = a.get('href') # в массиве обьекта супа взять все href
	print(links)


