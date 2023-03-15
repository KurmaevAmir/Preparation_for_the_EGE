from itertools import product

abc = "АРСЕНИЙ"
count = 0
for word in list(product(abc, repeat=4)):
    if word[0] != "Й" and ("А" in word or "Е" in word or "И" in word):
        count += 1
print(count)
