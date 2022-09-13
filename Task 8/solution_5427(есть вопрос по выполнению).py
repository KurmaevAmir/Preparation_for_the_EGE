from itertools import product

abc = ["К", "Е", "Г", "Э"]
numbers = ["0", "2", "3"]
abc.sort()
numbers.sort()
symbols = abc + numbers
options_list = list(set(["".join(i) for i in product(symbols, repeat=4)]))
options_list.sort()
symbols_duplicate = [i * 2 for i in symbols]
count = 0
for option in options_list:
    if option[0] in numbers:
        cond = True
        for symbol in symbols_duplicate:
            if symbol in option:
                cond = False
                break
        if cond:
            count += 1
print(count)
