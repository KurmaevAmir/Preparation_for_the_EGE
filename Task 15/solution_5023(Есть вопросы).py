for a in range(1000000, 10000000):
    cond = True
    for x in range(1, 1000):
        if cond:
            for y in range(1, 1000):
                if not((680 * y + 256 * x < a) or (5 * x + 3 * y > 11112)):
                    cond = False
                    break
        else:
            break
    if cond:
        print(a)
        break
