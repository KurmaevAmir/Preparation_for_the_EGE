def function(n, m):
    if n % m == 0:
        return True
    return False


max_a = 0
for a in range(1, 1000):
    cond = True
    for x in range(1, 1000):
        if not(function(190, a) and (((not(function(x, a))) and function(x, 15)) <= (not(function(x, 75))))):
            cond = False
            break
    if cond:
        max_a = a
print(max_a)
