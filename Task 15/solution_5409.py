def function(n, m):
    if n % m == 0:
        return True
    return False


count = 0
for a in range(1, 10000):
    cond = True
    for x in range(1, 1000):
        if not(function(a, 25) and ((function(x, 24) and function(x, 75)) <= function(x, a))):
            cond = False
            break
    if cond:
        count += 1
print(count)
