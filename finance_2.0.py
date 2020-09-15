import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36 '
    }
    r = requests.get(url, headers=headers, timeout=5)
    if r.status_code == 200:
        print('Ок!')

    if r.status_code == 404:
        print('Страница не существует!')
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    shares = soup.find('div', class_='top bold inlineblock').text  # ищем акции
    all_sum = shares[1:4]  # делаем хитрый срез =) потомучто в shares мусор который не дает привести к int()
    capital = int(all_sum) * 75  # приводим к целочисленному значению и производим умножение

    print('Tatneft' + '\n', shares + '\n', 'Cумма в акциях ~ ', capital)

    diapason = soup.find('div', class_='bottomText').text
    print(diapason)


def main():
    url = 'https://ru.investing.com/equities/tatneft_rts'
    html = get_html(url)
    get_page_data(html)
    input()


if __name__ == '__main__':
    main()
