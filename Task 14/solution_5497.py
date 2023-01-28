total_list = []
for x in range(13):
    for y in range(13):
        m = 2 * 15 ** 5 + y * 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 ** 1 + 5 * 15 ** 0
        n = 6 * 13 ** 4 + 7 * 13 ** 3 + x * 13 ** 2 + 9 * 13 ** 1 + y * 13 ** 0
        if m == n:
            total_list.append(n)
        elif m > n:
            if m % n == 0:
                total_list.append(n)
            else:
                total_list.append(n - m % n)
        else:
            total_list.append(n - m % n)
print(min(total_list))
