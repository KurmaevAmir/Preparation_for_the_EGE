from itertools import product

abc = "ОНИКС"
options1 = list(product(abc, repeat=4))
options2 = list(product(abc, repeat=5))
options3 = list(product(abc, repeat=6))
options_total = set(options1 + options2 + options3)
options_list = ["".join(i) for i in options_total]
count = 0
for word in options_list:
    if word.count("С") == 3 and word.count("О") == 1:
        count += 1
print(count)
