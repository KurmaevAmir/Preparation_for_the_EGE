from itertools import permutations

abs = "ТИХОРЕЦК"
options_list = ["".join(i) for i in permutations(abs, 4)]
count = 0
for option in options_list:
    count_vowels = option.count("И") + option.count("О") + option.count("Е")
    if count_vowels == 2:
        count_quiet = 0
        for n, litter in enumerate(option):
            if litter == "ТИХО"[n]:
                count_quiet += 1
        if count_quiet == 2:
            count += 1
print(count)
