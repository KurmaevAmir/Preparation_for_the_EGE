from itertools import product

abc = ["С", "Т", "Е", "П", "У", "Х", "А"]
abc.sort()
abc = "".join(abc)
black_options = ["СС", "ТТ", "ЕЕ", "ПП", "УУ", "ХХ", "АА"]
options_list = ["".join(i) for i in product(abc, repeat=4)]
count = 0
for option in options_list[999:]:
    cond = True
    for black_option in black_options:
        if black_option in option:
            cond = False
            break
    if cond:
        count += 1
print(count)
