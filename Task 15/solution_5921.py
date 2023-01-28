def check_del(n, m):
    if n % m == 0:
        return True
    return False


def check_symbol(s,d):
    if s + d > 0:
        return True
    return False


total_list = []
for a in range(1, 160):
    cond = True
    for x in range(1, 16000):
        if not((x + a >= 160) or (check_del(x, 7) <= (not(check_symbol(x, -17))))):
            cond = False
            break
    if cond:
        total_list.append(a)
print(min(total_list))
