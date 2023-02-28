from itertools import permutations

total_list = []
abc = "СПОРТЛОТО"
for word in list(permutations(abc, 9)):
    if word.index("Т") == 0:
        if word[word.index("Т") + 1] == "Т":
            total_list.append(word)
    elif word.index("Т") == len(word) - 1:
        if word[word.index("Т") - 1] == "Т":
            total_list.append(word)
    else:
        if word[word.index("Т") + 1] == "Т" or word[word.index("Т") - 1] == "Т":
            total_list.append(word)
total_list = set(total_list)
print(len(total_list))
