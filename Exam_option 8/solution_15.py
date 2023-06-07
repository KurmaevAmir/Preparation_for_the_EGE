for a in range(0, 1000):
    cond = True
    for x in range(1, 100):
        if cond:
            for y in range(1, 100):
                if cond:
                    for z in range(1, 100):
                        if not((150 != y + 2 * x + 2 * z) or (a < x) or (a < y) or (a < z)):
                            cond = False
                            break
                else:
                    break
        else:
            break
    if cond:
        print(a)
