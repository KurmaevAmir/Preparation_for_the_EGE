from itertools import product

count = 0
numbers = "01234"
options_list = ["".join(i) for i in product(numbers, repeat=6)]
for option in options_list[options_list.index("300000"):]:
    if int(option) % 2 == 0 and option[0] == "3":
        count += 1
print(count)
