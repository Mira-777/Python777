import requests
from bs4 import BeautifulSoup

class Parser:
    html = ""
    res = []
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        flors = self.html.find_all("div", class_="product_wrap")
        for item in flors:
            title = item.find("h4", class_="item_name product_title").text
            href = item.find('a').get("href")
            price = item.find("span", class_= "PricesalesPrice").text
            self.res.append({
                'title': title,
                'href': href,
                'price': price
            })

        #print(self.res)

    def save(self):
        with open(self.path, 'w') as f:
            i = 1
            for item in self.res:
                f.write(f"Цветок № {i}\n\nНазвание: {item['title']}\nСсылка: {item['href']}\nЦена: {item['price']}"
                        f"\n\n{'*' * 20}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()


