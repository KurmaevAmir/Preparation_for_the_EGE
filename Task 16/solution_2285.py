def function(n):
    if n <= 15:
        return 2 * n * n + 4 * n + 3
    elif n > 15 and n % 3 == 0:
        return function(n - 1) + n * n + 3
    elif n > 15 and n % 3 != 0:
        return function(n - 2) + n - 6


count = 0
for i in range(1, 1000):
    number = str(function(i))
    cond = True
    for j in range(len(number)):
        if int(number[j]) % 2 == 0:
            cond = False
            break
    if cond:
        count += 1
print(count)
