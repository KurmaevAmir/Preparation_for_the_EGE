for n in range(105, 200):
    n_bin = bin(n)[2:]
    for i in range(3):
        if n_bin.count("1") == n_bin.count("0"):
            n_bin += n_bin[-1]
        elif n_bin.count("1") > n_bin.count("0"):
            n_bin += "0"
        else:
            n_bin += "1"
    number = int(n_bin, 2)
    if number % 4 == 0:
        print(n)
        break
