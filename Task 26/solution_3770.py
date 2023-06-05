with open("Files/3770", "r") as f:
    n = int(f.readline().strip())
    mass = []
    for i in range(n):
        mass.append(int(f.readline().strip()))
    total_list = []
    mass.sort()
    for i in range(n - 1):
        if mass[i] % 2 == 0:
            for j in range(i + 1, n):
                if mass[j] % 2 == 0:
                    if (mass[i] + mass[j]) // 2 in mass:
                        total_list.append((mass[i] + mass[j]) // 2)
    print(len(total_list), min(total_list))
