for a in range(1, 1000):
    cond = True
    for x in range(1, 1000):
        if cond:
            for y in range(1, 1000):
                if not((75 != 2 * x + 3 * y) or (a > x * 3) or (a > 2 * y)):
                    cond = False
                    break
        else:
            break
    if cond:
        print(a)
        break
