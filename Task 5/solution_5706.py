for i in range(13, 100):
    n = i
    i = bin(i)[2::]
    if i.count("1") % 2 == 0:
        i += "0"
        i = i.replace(i[:2], "10", 1)
    else:
        i += "1"
        i = i.replace(i[:2], "11", 1)
    if int(i, 2) > 40:
        print(n)
        break
