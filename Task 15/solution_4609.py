n_min = float('inf')
for a1 in range(1000):
    for a2 in range(a1 + 1, 1000):
        cond = True
        for x in range(1000):
            if not(((80 <= x <= 103) <= (5 <= x <= 15)) or ((not(a1 <= x <= a2)) <= (35 <= x <= 50))):
                cond = False
                break
        if cond:
            n_min = min(n_min, abs(a2 - a1))
print(n_min)
