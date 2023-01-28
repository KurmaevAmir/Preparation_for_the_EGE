n_min = float('inf')
for i in range(1000):
    for j in range(i + 1, 1000):
        cond = True
        for x in range(1000):
            if not(((x >= 254 and x <= 800) and (not(x >= i and x <= j))) <= (x >= 410 and x <= 823)):
                cond = False
                break
        if cond:
            n_min = min(n_min, abs(j - i))
print(n_min)
