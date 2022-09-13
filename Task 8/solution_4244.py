from itertools import product

abc = "ПСКАЛЬ"
options = list(product(abc, repeat=4))
options_list = ["".join(i) for i in options]
count = 0
for word in options_list:
    if word[0] != "Ь":
        if (word[1] == "Ь" and word[2] == "Ь") or (word[2] == "Ь" and word[3] == "Ь"):
            pass
        else:
            count += 1
print(count)
