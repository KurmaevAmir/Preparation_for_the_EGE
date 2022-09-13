from itertools import product

symbols = "1234567890ABCDEF"
options = list(product(symbols, repeat=15))
options_list = ["".join(i) for i in options]
print(len(options_list))
