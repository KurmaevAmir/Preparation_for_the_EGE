from itertools import product

abc = "ДЕКОР"
count = 1
for word in list(product(abc, repeat=4)):
    if word[0] == "К":
        print(count)
        break
    count += 1
