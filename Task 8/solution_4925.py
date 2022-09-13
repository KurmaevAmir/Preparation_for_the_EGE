from itertools import product

count = 0
numbers = "0123456"
black_list = ["3", "5"]
options_list = ["".join(i) for i in product(numbers, repeat=7)]
for option in options_list[options_list.index("1000000"):]:
    if option[0] not in black_list and ("22" not in option or "44" not in option):
        count += 1
print(count)
