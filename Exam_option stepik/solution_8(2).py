from itertools import product

count = 1
abc = sorted("БАТЫР")
words_list = list(product(abc, repeat=5))
words_list = ["".join([abc for abc in massive]) for massive in words_list]
for word in words_list:
    if word.count("Ы") == 0:
        cond = True
        for pos in range(len(word) - 1):
            if word[pos] == word[pos + 1] == "А":
                cond = False
                break
        if cond:
            print(count)
            break
    count += 1
