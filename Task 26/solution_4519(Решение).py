with open("Files/4519", "r") as f:
    n, m = [int(i) for i in f.readline().strip().split()]
    mass = []
    for i in range(n):
        number, letter = [i for i in f.readline().strip().split()]
        mass.append((int(number), letter))
    mass.sort(key=lambda x: x[0])
    sum_coasts = 0
    abc_list = []
    for i in range(n):
        if sum_coasts + mass[i][0] > m:
            break
        sum_coasts += mass[i][0]
        abc_list.append(mass[i][1])
    l = len(abc_list)
    for j in range(len(abc_list) - 1, -1, -1):
        difference = m - sum_coasts
        if mass[j][1] != 'B' and difference > 0:
            k = mass[j][0]
            for i in range(l, n):
                if mass[i][0] - k <= difference and mass[i][1] == 'B':
                    sum_coasts -= k
                    sum_coasts += mass[i][0]
                    l = i + 1
                    difference = m - sum_coasts
                    abc_list[j] = mass[i][1]
                    break
print(abc_list.count("B"), m - sum_coasts)
