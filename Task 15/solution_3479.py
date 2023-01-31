for a in range(1, 1000):
    cond = True
    for x in range(1, 1000):
        if cond:
            for y in range(1, 1000):
                if not(((x - 20 < a) and (10 - y < a)) or ((x + 4) * y > 45)):
                    cond = False
                    break
        else:
            break
    if cond:
        print(a)
        break
