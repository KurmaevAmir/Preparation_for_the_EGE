n_max = -float("inf")
for i in range(1, 70):
    bin_n = bin(i)[2:]
    for j in range(3):
        zeros = bin_n.count("0")
        ones = bin_n.count("1")
        if zeros == ones:
            bin_n += bin_n[-1]
        elif zeros > ones:
            bin_n += "1"
        else:
            bin_n += "0"
    n = int(bin_n, 2)
    if n % 4 == 0 and max(n_max, i) != n_max:
        n_max = i
print(n_max)
