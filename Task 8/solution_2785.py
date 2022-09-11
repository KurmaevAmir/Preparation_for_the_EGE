from itertools import product

directions = "urdl"
options = list(product(directions, repeat=4))
options_list = ["".join(i) for i in options]
count = 0
for command in options_list:
    if command[0] != "u" and command[0] != command[2] and command[1] != command[3]:
        count += 1
print(count)
