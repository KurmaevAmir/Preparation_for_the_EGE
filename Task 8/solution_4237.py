from itertools import permutations

abc = "ДЕЙКСТРА"
white_list = ["Д", "К", "С", "Т", "Р"]
options = list(permutations(abc, 6))
options_list = ["".join(i) for i in options]
count = 0
for word in options_list:
    position = word.find("Й")
    if word.count("Й") == 1 and position != 5:
        if word[position + 1] in white_list:
            count += 1
print(count)
