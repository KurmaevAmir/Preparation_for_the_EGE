from itertools import product

total_list = []
word = "POLYGON"
vowels = ["O", "Y"]
for i in list(product(word, repeat=5)):
    if i[2] in vowels:
        if i[:2] == i[3:]:
            total_list.append(i)
total_list = set(total_list)
print(len(total_list))
