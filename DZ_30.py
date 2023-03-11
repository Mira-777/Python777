f = open('text5.txt', 'w')
f.write('''Замена строки в текстовом файле;
изменить строку в списке;
записать список в файл''')
f.close()
# Перестановка строк файла в обратном порядке
f = open('text5.txt', 'r')
L = f.readlines()

s = L[len(L)-1]
length = len(s)
f_nl = True

if (length>0)and((s[length-1] != '\n')):
    L[len(L)-1] += '\n'
    f_nl = False
f.close()
L2=[]
i=0
while i<len(L):
    s = L[len(L)-i-1]
    L2 = L2 + [s]
    i = i+1
if f_nl == False:
    L2[len(L)-1] = L2[len(L)-1][:-1]
f = open('text5.txt', 'w')
for item in L2:
    f.write(item)

f.close()
print(L2)
