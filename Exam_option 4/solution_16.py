def function(n):
    if n == 1 or n == 2:
        return 3
    elif n > 2:
        return 5 * function(n - 1) - 4 * function(n - 2)


print(function(15))
