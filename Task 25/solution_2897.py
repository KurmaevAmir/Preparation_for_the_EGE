total_list = []
for i in range(2358827, 2358891 + 1):
    if i % 2 != 0 or i % 10 != 5:
        for j in range(3, i):
            if i % j == 0:
                break
        else:
            total_list.append(i)
for n, i in enumerate(total_list):
    print(n + 1, i)
