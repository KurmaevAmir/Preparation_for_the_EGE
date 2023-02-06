def function(n):
    if n == 0:
        return 3
    elif 0 < n <= 15:
        return function(n - 1)
    elif 15 < n < 100:
        return 2.5 * function(n - 3)
    elif n >= 100:
        return 3.3 * function(n - 2)


print(function(100))
# 6
