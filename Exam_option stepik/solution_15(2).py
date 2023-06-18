def function(n, m):
    if n % m == 0:
        return True
    return False


for a in range(1, 100):
    cond = True
    for x in range(1, 100):
        if not((function(x, 6) <= (not(function(x, 10)))) or ((x + a) > 121)):
            cond = False
            break
    if cond:
        print(a)
        break
