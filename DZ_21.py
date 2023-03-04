
a = str(input('Введите строку - '))

b = list(a)

for i in range(len(b)):

   if b[i] == '(':

       x = i

   if b[i] == ')':

       y = i

for z in range(x+1,y):

   b[z]=str(b[z])

   g = b[z].replace(',',' ')

   print(g,end = "")