from itertools import permutations

abc = "ОДЕКОЛОН"
options_list = set(["".join(i) for i in permutations(abc, 8)])
count = 0
for option in options_list:
    if "ОО" not in option:
        count += 1
print(count)
