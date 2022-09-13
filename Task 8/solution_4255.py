from itertools import product

numbers = "01234567"
count = 0
options_list = ["".join(i) for i in product(numbers, repeat=4)]
for option in options_list[options_list.index("1000"):]:
    if int(option) % 4 == 0:
        count += 1
print(count)
