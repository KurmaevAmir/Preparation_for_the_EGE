from itertools import product

abc = ["А", "Б", "Г", "О", "Щ"]
abc.sort(reverse=True)
options = list(product("".join(abc), repeat=6))
options_list = ["".join(i) for i in options]
print(options_list.index("ОБЩАГА") + 1)
