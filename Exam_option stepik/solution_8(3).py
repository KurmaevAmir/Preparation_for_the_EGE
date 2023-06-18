from itertools import permutations

abc = sorted("КАПКАН")
words_list = list(permutations(abc, 6))
words_list = ["".join([abc for abc in massive]) for massive in words_list]
words_list = set(words_list)
count = 0
for word in words_list:
    cond = True
    for pos in range(len(word) - 1):
        if word[pos] == word[pos + 1]:
            cond = False
            break
    if cond:
        count += 1
print(count)
