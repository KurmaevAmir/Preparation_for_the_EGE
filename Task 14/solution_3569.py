for i in range(1, 1000):
    n1 = hex(i)[2:]
    n2 = oct(i)[2:]
    if len(n1) == 3 and len(n2) == 3:
        if n1[0] == "1" and n1[2] == "0" and n2[0] == "5" and n2[1] == "6":
            print(i)
            break
