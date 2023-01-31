for a in range(1, 1000):
    cond = True
    for x in range(1, 1000):
        if cond:
            for y in range(1, 1000):
                if not((- 5 * y + 3 * x < a) or  (x > 15) or (y > 30)):
                    cond = False
                    break
        else:
            break
    if cond:
        print(a)
        break
