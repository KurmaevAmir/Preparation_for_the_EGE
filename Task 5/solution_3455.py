total_list = []
for i in range(1, 10000):
    bin_n = bin(i)[2:]
    if bin_n.count("0") < bin_n.count("1"):
        bin_n += "0"
    else:
        bin_n += "1"
    bin_n_list = [j for j in bin_n]
    if len(bin_n) % 2 == 0:
        del bin_n_list[len(bin_n) // 2 - 1]
        del bin_n_list[len(bin_n) // 2 - 1]
    else:
        for j in range(3):
            del bin_n_list[len(bin_n) // 2 - 1]
    if bin_n_list == []:
        continue
    bin_n = int("".join(bin_n_list), 2)
    if bin_n not in total_list and bin_n >= 50 and bin_n <= 100:
        total_list.append(bin_n)
    elif bin_n > 500:
        break
print(len(total_list))
