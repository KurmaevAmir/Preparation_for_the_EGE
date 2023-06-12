from itertools import product

count = 1
abc = "ПАРУС"
abc = sorted(abc)
for word in list(product(abc, repeat=4)):
    if "А" not in word:
        print(count)
        break
    count += 1
