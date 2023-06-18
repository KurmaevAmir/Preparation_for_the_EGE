for i in range(1, 100):
    i_bin = bin(i)[2:]
    if i % 2 == 0:
        i_bin = "1" + i_bin + "00"
    else:
        i_bin += bin(sum([int(i) for i in i_bin]))[2:]
    if int(i_bin, 2) > 190:
        print(i)
        break
