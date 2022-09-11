from itertools import product

symbols = "АНДРЕЙ"
options = list(product(symbols, repeat=7))
options_list = [''.join(i) for i in options]
count = 0
for name in options_list:
    if name.count("Й") == 1 and name.count("А") == 1 and name[0] != "Й":
        count += 1
print(count)
