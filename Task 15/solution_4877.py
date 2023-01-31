a_max = -float('inf')
for a1 in range(1000):
    for a2 in range(a1 + 1, 1000):
        cond = True
        for x in range(1000):
            if not(((a1 <= x <= a2) <= (44 <= x <= 49)) or (28 <= x <= 53)):
                cond = False
                break
        if cond:
            a_max = max(a_max, abs(a2 - a1))
print(a_max)
