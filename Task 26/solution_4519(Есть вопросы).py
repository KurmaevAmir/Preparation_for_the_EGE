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
    difference = m - sum_coasts
    for i in range(len(abc_list), n):
        if mass[i][0] - mass[len(abc_list) - 1][0] <= difference:
            max_number = mass[i][0]
    print(abc_list.count("B"))
