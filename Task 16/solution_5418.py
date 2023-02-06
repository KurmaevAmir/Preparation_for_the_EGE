def function(n):
    if n < 2:
        return n
    elif n >= 2 and n % 2 == 0:
        return function(n // 2) + 1
    elif n >= 2 and n % 2 != 0:
        return function(3 * n + 1) + 1


count = 0
for i in range(1, 100001):
    if function(i) == 16:
        count += 1
print(count)
