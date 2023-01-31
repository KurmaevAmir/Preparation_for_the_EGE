n_min = float("inf")
for a1 in range(1000):
    for a2 in range(a1, 1000):
        cond = True
        for x in range(1000):
            if not((54 <= x <= 75) <= ( ((25 <= x <= 120) == (54 <= x <= 75)) or ((not(25 <= x <= 120)) <= (a1 <= x <= a2)) )):
                cond = False
                break
        if cond:
            n_min = min(n_min, abs(a2 - a1))
print(n_min)
