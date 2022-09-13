from itertools import permutations

abc = "МАРИНА"
options = list(permutations(abc, 6))
options_list = set("".join(i) for i in options)
count = 0
for word in options_list:
    if word[0] not in ["А", "И"]:
        count += 1
print(count)
