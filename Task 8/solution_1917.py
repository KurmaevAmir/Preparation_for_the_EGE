from itertools import product

symbols = "ГЕРОЙ"
options = list(product(symbols, repeat=4))
options_list = ["".join(i) for i in options]
count = 0
for word in options_list:
    if word[0] != "Й" and (word.count("Е") >= 1 or word.count("О") >= 1):
        count += 1
print(count)
