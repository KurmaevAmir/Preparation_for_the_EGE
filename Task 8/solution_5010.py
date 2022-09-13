from itertools import permutations, product

abc = "ПРЕПАРАТ"
options_list = set("".join(i) for i in permutations(abc, 8))
vowels = ["".join(i) for i in product("ЕАА", repeat=2)]
consonants = ["".join(i) for i in product("ПРПРТ", repeat=2)]
abc_options = set(vowels + consonants)
count = 0
for option in options_list:
    for abc_option in abc_options:
        if abc_option in option:
            count += 1
            break
print(count)
