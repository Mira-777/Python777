
import re
p = input("ведите пароль от 8 до 16 символов: ")
x = True
i = 0
while x:
    if len(p) < 8:
        print("Пароль меньше 8 символов")
        break
    elif len(p) > 16:
        print("Пароль больше 16 символов")
        break
    elif not re.search("[a-z]", p):
        i = i + 1
        print(i)
        break
    elif not re.search("[0-9]", p):
        i = i + 1
        print(i)
        break
    elif not re.search("[A-Z]", p):
        i = i + 1
        print(i)
        break
    elif not re.search("[-@_]", p):
        i = i + 1
        print(i)
        break
    elif not re.search("\s", p):
        i = i + 1
        print(i)
        break
    elif x == "True":
        print(i)
    else:
        print("Надежный пароль")
        x = False
        break

if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
    print("Пароль надёжный")
    print(i)
#elif i == 1:
    #print("ok")
else:
    print("Пароль не надёжный")
