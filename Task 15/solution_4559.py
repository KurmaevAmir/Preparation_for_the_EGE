n_max = -float("inf")
for a1 in range(1000):
    for a2 in range(a1 + 1, 1000):
        cond = True
        for x in range(1000):
            if ((a1 <= x <= a2) and (not(((11 > x or x > 28) <= (35 <= x <= 55))))):
                cond = False
                break
        if cond:
            n_max = max(n_max, abs(a2 - a1))
print(n_max)
