from itertools import product

abc = "CONST"
abc_options = ["CC", "OO", "NN", "SS", "TT"]
options_list = ["".join(i) for i in product(abc, repeat=16)]
count = 0

for option in options_list:
    cond = True
    position = option.find("S")
    if position != -1:
        if option[0] != "S" and option[-1] != "S" and option[position - 1] != option[position + 1]:
            for i in abc_options:
                if i in option:
                    cond = False
                    break
            if cond:
                count += 1
    elif position == -1:
        for i in abc_options:
            if i in option:
                cond = False
                break
        if cond:
            count += 1
print(count)
