def function(n, m):
    if n % m == 0:
        return True
    return False


for a in range(1, 1000):
    cond = True
    for x in range(1000):
        if not((function(x, 6) <= (not())))