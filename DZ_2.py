dictionary_1 = {1: 10, 2: 20}
dictionary_2 = {3: 30, 4: 40}
dictionary_3 = {5: 50, 6: 60}
dictionary_4 = dictionary_1.copy()
dictionary_4.update(dictionary_2)
dictionary_4.update(dictionary_3)
print(dictionary_4)