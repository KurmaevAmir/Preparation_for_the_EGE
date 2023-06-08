with open("Files/5231", "r") as f:
    n = int(f.readline().strip())
    mass = []
    for i in range(n):
        mass.append([int(i) for i in f.readline().strip().split()])
    mass.sort()
    count = 0
    total_list = []
    for i in range(n - 1):
        if mass[i][0] == mass[i + 1][0] and mass[i][1] % 2 == 0:
            count += 1
        elif mass[i][0] != mass[i + 1][0] and count != 0:
            if mass[i][1] % 2 == 0:
                count += 1
            total_list.append((count, mass[i][0]))
            count = 0
    print(*[i for i in total_list if i[0] == max(total_list)[0]][0])
