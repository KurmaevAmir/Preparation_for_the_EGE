from itertools import product

product_list = [[j for j in i] for i in list(product("АГИЛМОРТ", repeat=4))]
count = 1
for word in product_list:
    if word == ["Т", "Т", "И", "М"]:
        print(count)
        break
    count += 1
