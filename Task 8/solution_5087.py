from itertools import product

abc = ["С", "Т", "Е", "К", "Л", "О"]
abc.sort()
abc = "".join(abc)
options_list = ["".join(i) for i in product(abc, repeat=5)]
for n, option in enumerate(options_list):
    if option[0] == "С" and "ОО" in option:
        print(n + 1)
        break
