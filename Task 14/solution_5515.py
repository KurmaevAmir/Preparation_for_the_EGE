total_list = []
a_key = {}
for a in range(55):
    n1 = 35 * 55 ** 3 + a * 55 ** 2 + 34 * 55 ** 1 + 33 * 55 ** 0
    n2 = 2 * 55 ** 3 + 33 * 55 ** 2 + a * 55 ** 1 + 34 * 55 ** 0
    if (n1 - n2) % 29 == 0:
        total_list.append(a)
        a_key[a] = n1 - n2
min_a = min(total_list)
max_a = max(total_list)
print(abs(a_key[max_a] - a_key[min_a]))
