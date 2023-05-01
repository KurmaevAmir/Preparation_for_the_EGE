def function(n, k, m):
    if n > k:
        return 0
    if n == k:
        return 1
    else:
        if n % 3 == 0 or n % 4 == 0:
            if n % 3 == 0:
                m += 1
            if n % 4 == 0:
                m += 1
            if m <= 5:
                return function(n + 1, k, m) + function(n * 3, k, m) + function(n * 4, k, m)
            else:
                return 0
        else:
            return function(n + 1, k, m) + function(n * 3, k, m) + function(n * 4, k, m)


print(function(3, 300, 0))
