def function(n, m):
    if n % m == 0:
        return True
    return False


count = 0
for a in range(1, 10000):
    cond = True
    for x in range(1, 1000):
        if not((160 <= x <= 180) <= (function(x, 35) <= function(x, a))):
            cond = False
            break
    if cond:
        count += 1
print(count)
