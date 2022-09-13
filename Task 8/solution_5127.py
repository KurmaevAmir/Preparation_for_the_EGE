from itertools import product

numbers = "01234567"
options_list = ["".join(i) for i in product(numbers, repeat=5)]
count = 0
for option in options_list[options_list.index("70000"):]:
    cond1 = False
    cond2 = False
    if int(option) % 2 == 0:
        if "56" in option:
            cond2 = True
        if "65" in option:
            cond1 = True
        if cond1 and cond2:
            continue
        elif cond1 or cond2:
            count += 1
print(count)
