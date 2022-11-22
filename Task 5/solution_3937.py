for i in range(1, 50):
    n_bin_list = [int(j) for j in bin(i)[2:]]
    n_bin_sum = sum(n_bin_list)
    n_bin = "".join([str(j) for j in n_bin_list]) + str(n_bin_sum % 2)
    if n_bin.count("0") < n_bin.count("1"):
        n_bin += "0"
    else:
        n_bin += "1"
    if int(n_bin, 2) > 80:
        print(int(n_bin, 2))
        break
