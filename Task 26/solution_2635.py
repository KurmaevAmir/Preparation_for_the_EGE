with open("Files/2635", "r") as f:
    s, n = [int(i) for i in f.readline().strip().split()]
    mass = []
    for i in range(n):
        mass.append(int(f.readline().strip()))
    mass.sort()
    archived = 0
    count = 0
    for i in range(n):
        if archived + mass[i] > s:
            break
        archived += mass[i]
        count += 1
    print(count)
    difference = s - archived
    for i in range(count, n):
        if mass[i] - mass[count - 1] <= difference:
            max_number = mass[i]
    print(max_number)
