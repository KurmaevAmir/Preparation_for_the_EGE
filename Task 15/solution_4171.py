def function(n, m):
    return n // m


for a in range(1, 1000):
    cond = True
    for x in range(1, 1000):
        if not((function(x, 50) > 3) or (not(function(x, 13) > 3)) or (function(x, a) > 6)):
            cond = False
            break
    if cond:
        print(a)
        break
