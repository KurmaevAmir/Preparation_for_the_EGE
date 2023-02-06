def function(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return function(n // 2) - 1
    elif n > 0 and n % 2 != 0:
        return 1 + function(n - 1)


count = 0
for i in range(1000):
    if function(i) == 0:
        count += 1
print(count)
