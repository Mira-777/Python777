s = ('''Ежевику для ежат
       Принесли два ежа
       Ежевику еле-еле
       Ежата возле ели съели''')
words = s.split()
count = 0
for word in words:
    if word[0] == "е":
        count += 1
    if word[0] == "Е":
        count += 1
print(f"Количество слов,начинающихся с"
      f"': {count}")
