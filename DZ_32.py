class Auto:
    name = "name"
    year = "year"
    engine = "engine"
    power = "power"
    color = "color"
    price = "price"

    def print_info(self):
        print("Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.name}\nГод выпуска:{self.year}\nПроизводитель: {self.engine}\n"
              f"Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def input_info(self, first_name, year, engine, power, color, price):
        self.name = first_name
        self.year = year
        self.engine = engine
        self.power = power
        self.color = color
        self.price = price

    def set_engine(self, engine):
        self.engine = engine

    def get_engine(self):
        return self.engine

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name



h1 = Auto()
h1.print_info()
h1.input_info("Х7 М50i", "2021", "BMW","530 л.с.", "white", "10790000")
h1.print_info()
h1.set_name('Rio')
print(h1.get_name())
h1.set_year(2019)
print(h1.get_year())
h1.set_engine('Kia')
print(h1.get_engine())
h1.set_power('430 л.с.')
print(h1.get_power())
h1.set_color('red')
print(h1.get_color())
h1.set_price(1200000)
print(h1.get_price())