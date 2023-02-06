def function(n):
    if n > 18:
        return n
    elif n <= 18:
        return 3 * function(n + 1) + n + 8


print(function(9))
