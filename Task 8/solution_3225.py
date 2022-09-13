from itertools import product

abc = "КАЛИЙ"
options = list(product(abc, repeat=6))
options_list = ["".join(i) for i in options]
count = 0
for word in options_list:
    position = word.find("Й")
    if position == -1:
        count += 1
    elif word[0] != "Й" and word[-1] != "Й" and word.count("Й") <= 1 and \
            word[position - 1] != "И" and word[position + 1] != "И":
        count += 1
print(count)
