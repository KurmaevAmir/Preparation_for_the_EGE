def function(n, m):
    if n % m == 0:
        return True
    return False


min_function = float('inf')
for a1 in range(1, 1000):
    for a2 in range(a1 + 1, 1001):
        cond = True
        for x in range(1, 1000):
            if not((x >= a1 and x <= a2) or ((x >= 10 and x <= 40) <= (not(function(x, 6))))):
                cond = False
                break
        if cond is False:
            continue
        else:
            min_function = min(min_function, a2 - a1)
print(min_function)
