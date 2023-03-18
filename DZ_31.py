import os

path = os.listdir()
for el in path:
    if os.path.isfile(el):
        print(el, '- file -', os.path.getsize(el), "bytes")
    else:
        print(el, '- dir')


