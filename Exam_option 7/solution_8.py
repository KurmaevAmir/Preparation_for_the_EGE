from itertools import product

abc = "АКЛМНЯ"
count = 0
for word in list(product(abc, repeat=5)):
    count += 1
    if "".join(word[:2]) == "КМ":
        print(count)
        break
