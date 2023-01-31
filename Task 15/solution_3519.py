for a in range(1, 1000):
    cond = True
    for x in range(1, 1000):
        if not((((x & 13 != 0) or (x & a == 0)) <= (x & 13 != 0)) or (x & a != 0) or (x & 39 == 0)):
            cond = False
            break
    if cond:
        print(a)
        break
