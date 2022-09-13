from itertools import product

abc = ["О", "С", "Е", "Н", "Ь"]
abc.sort(reverse=True)
abc = "".join(abc)
options = list(product(abc, repeat=4))
options_list = ["".join(i) for i in options]
print(options_list[99])
