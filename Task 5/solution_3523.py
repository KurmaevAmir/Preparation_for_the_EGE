for i in range(13, 100):
    n = int(str(i) + str(i)[-1])
    n_bin = bin(n)[2:]
    if n_bin.count("1") % 2 != 0:
        n_bin += "1"
    else:
        n_bin += "0"
    if int(n_bin, 2) > 413:
        print(i)
        break
