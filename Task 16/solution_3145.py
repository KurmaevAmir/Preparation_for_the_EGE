def function(n, m):
    if m == 0:
        d = 0
    else:
        d = n + function(n, m - 1)
    return d


total_list = []
for i in range(300):
    for j in range(300):
        if function(i, j) == 30:
            total_list.append(i)
set(total_list)
print(len(total_list))
