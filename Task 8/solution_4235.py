from itertools import product

abc = "ЯСНОВИДЕЦ"
vowels = ["Я", "О", "И", "Е"]
options = list(product(abc, repeat=5))
options_list = ["".join(i) for i in options]
count = 0
for word in options_list:
    if word[0] not in vowels and word[-1] in vowels and word.count(word[0]) == 1 and word.count(word[-1]) == 1:
        count += 1
print(count)
