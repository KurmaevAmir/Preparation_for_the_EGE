def function(n, m):
    if m == 0:
        d = 0
    else:
        d = n + function(n, m - 1)
    return d



