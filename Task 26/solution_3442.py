with open("Files/3442", "r") as f:
    d, e, n = [int(i) for i in f.readline().strip().split()]
    mass = []
    for i in range(n):
        mass.append(int(f.readline().strip()))
    mass.sort()
    storage_e = 0
    count_e = 0
    for i in range(n):
        if storage_e + mass[i] > e or mass[i] > 500:
            break
        storage_e += mass[i]
        count_e += 1
    difference = e - storage_e
    for i in range(count_e, n):
        if mass[i] > 500:
            break
        if mass[i] - mass[count_e - 1] <= difference:
            max_number_e = mass[i]
            pos_max_number = i
    storage_d = 0
    count_d = 0
    pos_max_count_d = 0
    for i in range(n):
        if mass[i] > 500:
            if storage_d + mass[i] > d:
                break
            storage_d += mass[i]
            count_d += 1
            pos_max_count_d = i
    difference_d = d - storage_d
    for i in range(pos_max_count_d, n):
        if (mass[i] - mass[pos_max_count_d - 1]) <= difference_d and mass[i] != 0:
            max_number_d = mass[i]
    print(count_e + count_d, max_number_d + max_number_e)
