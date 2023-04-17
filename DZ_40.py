class Integer:



    @staticmethod
    def verify_dlina(dlina):
        if not isinstance(dlina, int):
            raise TypeError(f"Длина {dlina} должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verity_dlina(value)
        instance.__dict__[self.name] = value


class Triangle:
    def __init__(self, a, b, c):
        print('Треугольник со сторонами', (a, b, c))
        self.a = a
        self.b = b
        self.c = c

        flag = ''
        if a + b <= c:
            flag = 'c'
        elif a + c <= b:
            flag = 'b'
        elif b + c <= a:
            flag = 'a'
        else:
            print("существует")

        if flag != '':
            print("Не существует")


p1 = Triangle(2, 5, 6)
print(p1.__dict__)
p2 = Triangle(3, 2, 8)
print(p2.__dict__)
p3 = Triangle(7, 3, 6)
print(p3.__dict__)











