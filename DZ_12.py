s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")
a = list(set(s1) | set(s2))
print("Искомыми буквами являются: ")
for i in a:
    print(i)