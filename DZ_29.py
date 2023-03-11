f = open('text4.txt', 'w')
f.write('''Замена строки в текстовом файле;
изменить строку в списке;
записать список в файл''')
f.close()

# Обмен местам двух строк в файле
pos1 = int(input('pos1 = '))
pos2 = int(input('pos2 = '))

if pos2<=pos1: exit()
f = open('text4.txt', 'r')
L = f.readlines()
s = L[len(L)-1]
length = len(s)
f_nl = True

if (length>0)and((s[length-1] != '\n')):
    L[len(L)-1] += '\n' # добавить в последнюю строку '\n'
    f_nl = False

f.close()

if (pos1<0)or(pos1>=len(L))or(pos2<0)or(pos2>=len(L)):
    exit()

s = L[pos1]
L[pos1] = L[pos2]
L[pos2] = s

f = open('text4.txt', 'w')


if f_nl == False:

    L[len(L)-1] = L[len(L)-1][:-1]

for item in L:
    f.write(item)


f.close()
print(L)
