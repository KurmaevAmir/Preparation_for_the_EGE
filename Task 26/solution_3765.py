with open("Files/3765", "r") as f:
    n = int(f.readline().strip())
    mass = []
    for i in range(n):
        mass.append(int(f.readline().strip()))
    mass.sort()
    total_list = []
    median = mass[len(mass) // 2]
    for i in range(n - 1):
        cond = False
        if mass[i] % 2 == 0:
            cond = True
        for j in range(i + 1, n):
            if ((mass[j] % 2 == 0 and mass[i] % 2 == 0) or\
                    (mass[j] % 2 != 0 and mass[i] % 2 != 0))\
                    and (mass[j] + mass[i]) // 2 < median:
                total_list.append((mass[i] + mass[j]) // 2)
    print(len(total_list), max(total_list))
