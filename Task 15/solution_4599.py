n_max = -float('inf')
for a1 in range(1000):
    for a2 in range(a1, 1000):
        cond = True
        for x in range(1000):
            if (((not(5 <= x <= 60)) or (15 <= x <= 30)) and (a1 <= x <= a2)):
                cond = False
                break
        if cond:
            n_max = max(n_max, abs(a1 - a2))
print(n_max + 1)
