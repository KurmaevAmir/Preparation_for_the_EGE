def function(n):
    if n < 3:
        return 3 * n
    elif n > 2 and n % 2 == 0:
        return function(n - 2) * function(n - 1) - n
    elif n > 2 and n % 2 != 0:
        return function(n - 1) - function(n - 2) + 2 * n

print(str(function(30))[-2:])
