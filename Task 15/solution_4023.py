for a in range(1, 1000):
    cond = True
    for x in range(1, 1000):
        if not((x & 87 == 0) <= ((x & 31 != 0) <= (x & a != 0))):
            cond = False
            break
    if cond:
        print(a)
        break
