for i in range(14, 100):
    i_bin = bin(i)[2:]
    if i % 2 == 0:
        i_bin += "10"
    else:
        i_bin = "1" + i_bin + "01"
    if int(i_bin, 2) > 516:
        print(i)
        break
