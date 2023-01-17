number = 16 ** 44 * 16 ** 30 - (32 ** 5 * (8 ** 40 - 8 ** 32) * (16 ** 17 - 32 ** 4))
number_hex = hex(number)[2:]
number_hex = number_hex.replace("f", "0")
len_number_hex = len(number_hex)
number_changed = 0
number_hex_list = [i for i in number_hex]
for i in range(3):
    del number_hex_list[-1]
number_hex_list_changed = []
cond = True
for symbol in number_hex_list:
    if cond and symbol == "0":
        continue
    else:
        cond = False
        number_hex_list_changed.append(symbol)
print(number_hex_list_changed.count("0"))
