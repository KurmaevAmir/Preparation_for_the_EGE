from itertools import product

abc = ["П", "Я", "Т", "Ь", "Д", "Н", "Е", "Й"]
abc.sort()
position_word = 0
count = 0
for word in product(abc, repeat=4):
    count += 1
    if "Я" not in word and "Е" not in word:
        cond = True
        for letter in word:
            if word.count(letter) >= 2:
                cond = False
                break
        if cond:
            position_word = count
print(position_word) # 3428
