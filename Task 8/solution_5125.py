from itertools import product

abc = "ОГЭИНФ"
options_list = ["".join(i) for i in product(abc, repeat=6)]
count = 0
for option in options_list:
    if option[0] in ["Э", "О"] and option[-2:] == "НФ" and "ИГ" in option and "ОГЭ" not in option:
        count += 1
print(count)
