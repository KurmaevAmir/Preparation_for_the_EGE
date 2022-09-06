from itertools import permutations

a = "СПОРТЛОТО"
b = list(permutations(a, 9))
sort_b = [''.join(i) for i in b if i[0] != "О" and i[-1] != "О"]
sort_b = set(sort_b)
print(len(sort_b))
