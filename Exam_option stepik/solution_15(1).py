def function(n, m):
    if n % m == 0:
        return True
    return False


for a in range(1, 100):
    cond = True
    for b in range(50, 71):
        if cond:
            for x in range(1, 100):
                if not(function(x, a) or ((50 <= x <= 70) <= (not(function(x, 21))))):
                    cond = False
                    break
        else:
            break
    if cond:
        max_a = a
print(max_a)
