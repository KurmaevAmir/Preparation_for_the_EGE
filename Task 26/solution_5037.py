with open("Files/5037", "r") as f:
    n, k = [int(i) for i in f.readline().strip().split()]
    mass = []
    for i in range(n):
        mass.append([int(i) for i in f.readline().strip().split()])
    mass.sort()
    count = 0
    total_list = []
    for i in range(n - 1):
        if mass[i][0] == mass[i + 1][0] and mass[i + 1][1] - mass[i][1] - 1 == k:
            total_list.append((mass[i][0], mass[i][1] + 1))
    print(max(total_list))
