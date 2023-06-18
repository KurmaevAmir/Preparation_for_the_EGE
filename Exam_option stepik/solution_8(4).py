from itertools import product

words_list = ["".join([abc for abc in word]) for word in list(product("ШКОЛА", repeat=3))]
count = 0
for word in words_list:
    if word.count("К") == 1:
        count += 1
print(count)
