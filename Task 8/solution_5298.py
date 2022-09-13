from itertools import product

abc = ["У", "Ж", "Е", "М", "А", "Й"]
abc.sort()
abc = "".join(abc)
options_list = ["".join(i) for i in product(abc, repeat=5)]
count = 0
double_abc = [i * 2 for i in abc]
for n, option in enumerate(options_list):
    if n % 2 == 0:
        cond = True
        for litters in double_abc:
            if litters in option:
                cond = False
                break
        if cond:
            count += 1
print(count)
