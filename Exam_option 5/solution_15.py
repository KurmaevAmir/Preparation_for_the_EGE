min_function = float("inf")
for a1 in range(-200, 200):
    for a2 in range(-200, 200):
        cond = True
        for x in range(1000):
            if not((117 <= x <= 158) <= (((129 <= x <= 180) and (not(a1 < x < a2))) <= (not(117 <= x <= 158)))):
                cond = False
                break
        if cond:
            min_function = min(min_function, abs(a2 - a1))
print(min_function + 1)
