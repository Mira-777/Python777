from parsers import Parser


def main():
    pars = Parser("https://flors.ru/catalog/komnatnye-rastenija", "flors.txt")
    pars = Parser("https://flors.ru/catalog/komnatnye-rastenija?start=64/", "flors2.txt")
    pars = Parser("https://flors.ru/catalog/komnatnye-rastenija?start=96/", "flors3.txt")



    pars.run()



if __name__ == '__main__':
    main()








