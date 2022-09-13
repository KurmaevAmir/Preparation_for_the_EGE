from itertools import permutations

colors = "ROYGXBP"
options_list = []
for i in range(3, 10):
    options_list += ["".join(z) for z in permutations(colors, i)]
print(len(options_list))
