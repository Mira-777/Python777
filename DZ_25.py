import re

s = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@name.ru"

lst = re.findall('\S+@\S+\W', s)


print(lst)