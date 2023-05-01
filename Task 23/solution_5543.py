def function(n, k, m):
    if n > k:
        return 0
    if n == k:
        return 1
    else:
        if n % 2 != 0:
            m += 1
            if m != 2:
                return function(n + 2, k, m) + function(n * 3, k, m) + function(n * 4, k, m)
            else:
                return 0
        else:
            m = 0
            return function(n + 2, k, m) + function(n * 3, k, m) + function(n * 4, k, m)


print(function(1, 600, 0))
