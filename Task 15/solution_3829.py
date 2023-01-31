def function(n, m):
    if n % m == 0:
        return True
    return False


count = 0
for a in range(1, 1000):
    cond = True
    for x in range(1, 10000):
        if not(function(a, 12) and (function(530, x) <= ((not(function(a, x))) <= (not(function(170, x)))))):
            cond = False
            break
    if cond:
        count += 1
print(count)
