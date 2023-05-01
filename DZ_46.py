import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    res = requests.get(url)
    return res.text

def write_csv(data):
    with open("muzik.csv", 'a') as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\r")

        writer.writerow((data['name'], data['url'], data['price']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find_all("div", class_="col-lg-4 col-md-4 col-sm-4")
    #print(len(p1))
    for el in p1:
        try:
            name = el.find("div", class_="item_title").text
        except ValueError:
            name = ""

        try:
            url = el.find('div', class_="item_title").find("a")["href"]
        except ValueError:
            url = ""

        try:
            price = el.find('div', class_="item_price").text
        except ValueError:
            price = ""

        data = {
            'name': name,
            'url': url,
            'price': price
        }


        write_csv(data)


def main():
    url = "https://www.golovastik.ru/shop/muzykal-nye-igrushki/muzykal-nye-instrumenty"
    get_data(get_html(url))

if __name__=='__main__':
    main()