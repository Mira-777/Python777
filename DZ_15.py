import math
print('Площадь окружности радиуса 2: ',(lambda x = 2, y = math.pi: x ** 2 * y)())


print('Площадь прямоугольника размером 10*13: ',(lambda x, y: x * y)(10, 13))


print('Площадь трапеции для a=7, b=5, h=3: ',(lambda a = 7, b = 5, h = 3: (a + b)/2 * h)())



