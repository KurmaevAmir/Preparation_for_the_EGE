def function(n, m):
    if n % m == 0:
        return True
    return False


for a in range(1, 1000):
    cond = True
    for x in range(1, 1000):
        if not((function(x, 6) <= (not(function(x, 14)))) or (x + a >= 70) and function(a, 20)):
            cond = False
            break
    if cond:
        print(a)
        break