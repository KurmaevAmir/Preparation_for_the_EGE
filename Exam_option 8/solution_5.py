for i in range(1, 50):
    i_bin = bin(i)[2:]
    i_bin_duplicate = i_bin
    i_bin_duplicate += i_bin_duplicate[-1]
    if i_bin.count("1") % 2 == 0:
        i_bin_duplicate += "0"
    else:
        i_bin_duplicate += "1"
    if i_bin_duplicate.count("1") % 2 == 0:
        i_bin_duplicate += "0"
    else:
        i_bin_duplicate += "1"
    if int(i_bin_duplicate, 2) > 105:
        print(int(i_bin_duplicate, 2))
        break
