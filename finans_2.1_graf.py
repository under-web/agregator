import requests
from bs4 import BeautifulSoup
from tkinter import *


def get_html(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36 '
    }
    r = requests.get(url, headers=headers, timeout=5)
    if r.status_code == 200:  # проверяем статус подключения
        print('Ок!')

    if r.status_code == 404:
        print('Страница не существует!')
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')  # создаем обьект супа с парсером lxml
    shares = soup.find('div', class_='top bold inlineblock').text  # ищем акции
    all_sum = shares[1:4]  # делаем хитрый срез =) потомучто в shares мусор который не дает привести к int()
    capital = int(all_sum) * 75  # приводим к целочисленному значению и производим умножение
    diapason = soup.find('div', class_='bottomText').text  # диапазон цен
    # print('Tatneft' + '\n', shares + '\n', 'Cумма в акциях ~ ', capital)

    return capital, diapason, shares  # возвращаем кортежем значения сумму, диапазон цен и стоимость акций


def window_graf(capital, diapason, shares):
    window = Tk()
    window.geometry('600x250')
    window.title("Мой капитал")
    lbl = Label(window, text='Примерная сумма в акциях ~' + str(capital))
    lbl.grid(column=0, row=0)
    lb2 = Label(window, text=shares)
    lb2.grid(column=0, row=1)
    lb3 = Label(window, text=diapason)
    lb3.grid(column=0, row=2)
    window.mainloop()


def main():
    url = 'https://ru.investing.com/equities/tatneft_rts'
    html = get_html(url)
    capital, diapason, shares = get_page_data(html)
    window_graf(capital, diapason, shares)


if __name__ == '__main__':
    main()
