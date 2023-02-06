def function(n, m):
    if n % m == 0:
        return True
    return False


min_a = float('inf')
for a1 in range(10000):
    for a2 in range(a1, 10000):
        cond = True
        for x in range(1, 1000):
            if not((20 <= x <= 80) <= (function(x, 17) <= (a1 <= x <= a2))):
                cond = False
                break
        if cond:
            min_a = min(min_a, abs(a2 - a1))
print(min_a)
