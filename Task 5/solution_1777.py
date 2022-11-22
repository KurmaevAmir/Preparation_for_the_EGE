for i in range(100):
    n_bin = bin(i)[2::]
    n_bin += n_bin[-1]
    if n_bin.count("1") % 2 == 0:
        n_bin += "011"
    else:
        n_bin += "111"
    n = int(n_bin, 2)
    if n > 80:
        print(n)
        break
