for a in range(1, 1000):
    cond = True
    for x in range(1, 1000):
        if not((x & 41 == 0) <= ((x & 119 != 0) <= (x & a != 0))):
            cond = False
            break
    if cond:
        print(a)
        break
