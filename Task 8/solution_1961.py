from itertools import permutations

symbols = "ТРАТАТА"
options = list(permutations(symbols, 7))
options_list = ["".join(i) for i in set(options)]
count = 0
for word in options_list:
    if word.count("Т") <= 3 and word.count("А") <= 3:
        count += 1
print(count)
