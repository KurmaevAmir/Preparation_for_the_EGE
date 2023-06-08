with open("Files/4859", "r") as f:
    n = int(f.readline().strip())
    mass = []
    for i in range(n):
        mass.append([int(i) for i in f.readline().strip().split()])
    mass.sort()
    number = 1
    total_list = []
    for i in range(n - 1):
        if mass[i][0] == mass[i + 1][0] and mass[i][1] + 1 == mass[i + 1][1]:
            number += 1
        elif number != 0:
            total_list.append((mass[i - 1][0], number))
            number = 1
    total_list.sort(key=lambda x: x[1])
    print(*total_list[-1])
