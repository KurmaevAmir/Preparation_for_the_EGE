for a in range(200):
    cond = True
    for x in range(100):
        if cond:
            for y in range(100):
                if not((x >= 9) or (2 * x < y) or (x * y < a)):
                    cond = False
                    break
    if cond:
        print(a)
        break
