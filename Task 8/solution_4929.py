from itertools import product

count = 0
numbers = "012345678"
white_list = ["2", "4", "6"]
options_list = ["".join(i) for i in product(numbers, repeat=7)]
for option in options_list[options_list.index("1000000"):]:
    if option[0] not in white_list and (option[-1] != option[-2] or option[-2] != option[-3]):
        count += 1
print(count)
