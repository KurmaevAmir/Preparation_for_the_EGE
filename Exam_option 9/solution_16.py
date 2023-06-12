def function(n):
    if n <= 2:
        return n + 1
    else:
        return function(n - 1) * function(n - 2)


print(function(4))
