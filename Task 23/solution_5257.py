def function(n, k, m):
    if n > k:
        return 0
    if n == k:
        return 1
    else:
        if n % 6 == 0:
            m += 1
            if m <= 3:
                return function(n + 2, k, m) + function(n * 2, k, m) + function(n * 3, k, m)
            else:
                return 0
        else:
            return function(n + 2, k, m) + function(n * 2, k, m) + function(n * 3, k, m)


print(function(1, 300, 0))
