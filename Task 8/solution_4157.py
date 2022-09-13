from itertools import product

count = 0
numbers = "01234"
options_list = ["".join(i) for i in product(numbers, repeat=6)]
n1 = options_list.index("300000")
n2 = options_list.index("400000")
print((abs(n1 - n2) - 1) / 2)
