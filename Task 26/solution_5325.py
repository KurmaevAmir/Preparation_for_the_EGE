with open("Files/5325", "r") as f:
    n = int(f.readline().strip())
    mass = []
    for i in range(n):
        mass.append(int(f.readline().strip()))
    mass.sort(reverse=True)
    total_list = [mass[0]]
    for i in range(1, n):
        if total_list[-1] - mass[i] >= 3:
            total_list.append(mass[i])
    for i in range(len(total_list), n):
        if total_list[-2] - mass[i] >= 3:
            min_number = mass[i]
            break
    print(len(total_list), min_number)
