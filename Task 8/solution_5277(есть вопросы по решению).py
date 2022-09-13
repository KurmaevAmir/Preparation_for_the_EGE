from itertools import product

abc = ["А", "И", "К", "Л", "М", "Ь"]
abc_sorted = abc.copy()
abc_sorted.sort()
abc_sorted = "".join(abc_sorted)
options_list = ["".join(i) for i in product(abc_sorted, repeat=6)]
for n, option in enumerate(options_list):
    if option[0] == "К" and option[-1] == "Ь":
        cond = True
        for letter in abc:
            if option.count(letter) != 1:
                cond = False
                break
        if cond and abs(n - int(str(n)[::-1])) == 26655:
            print(n + 1)
            break
