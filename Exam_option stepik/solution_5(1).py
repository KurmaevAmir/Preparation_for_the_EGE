for i in range(1, 50):
    i_bin = bin(i)[2:]
    if i % 3 == 0:
        i_bin += i_bin[-3:]
    else:
        i_bin += bin(i % 3 * 3)[2:]
    if int(i_bin, 2) >= 76:
        print(i)
        break
