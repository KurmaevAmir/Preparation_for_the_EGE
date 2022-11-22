n_max = -float("inf")
for i in range(1, 1000):
    bin_n = bin(i)[2:]
    if bin_n[-1] != "0":
        continue
    else:
        bin_n_list = [j for j in bin_n]
        del bin_n_list[-1]
        bin_n_list.append(bin_n_list[0])
        bin_n_list.append(bin_n_list[1])
        bin_n_list = bin_n_list[::-1]
        n = int("".join(bin_n_list), 2)
        if n == 119 and max(n_max, i) == i:
            n_max = i
print(n_max)
