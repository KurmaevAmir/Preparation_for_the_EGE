from itertools import permutations

word = "СПОРТЛОТО"
total_list = []
for i in list(permutations(word, 9)):
    for j in range(len(i) - 1):
        if i[j] == i[j - 1] and i[j] == "О":
            total_list.append(i)
print(len(set(total_list)))
