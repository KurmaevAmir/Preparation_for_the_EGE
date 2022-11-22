for i in range(11, 60):
    n_bin = bin(i)[2:]
    n_bin += n_bin[-2] + n_bin[1]
    if int(n_bin, 2) > 210:
        print(i)
        break
