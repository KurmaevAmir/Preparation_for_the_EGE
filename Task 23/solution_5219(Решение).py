def function(n, k, m):
    if n > k:
        return 0
    if n == k:
        return 1
    else:
        if m < 5:
            return function(n + 1, k, m) + function(n * 3, k, m + 1) + function(n * 4, k, m + 1)
        else:
            return 0


print(function(3, 300, 0))
