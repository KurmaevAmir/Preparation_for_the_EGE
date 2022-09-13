from itertools import product

directions = "urdl"
options = list(product(directions, repeat=5))
options_list = ["".join(i) for i in options]
count = 0
for symbol in options_list:
    if symbol[0] != "u" and (symbol[0] != symbol[2] or symbol[1] != symbol[3]):
        count += 1
print(count)
