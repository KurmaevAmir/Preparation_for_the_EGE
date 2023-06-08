with open("Files/4517", "r") as f:
    n, m = [int(i) for i in f.readline().strip().split()]
    mass = []
    for i in range(n):
        number, letter = [i for i in f.readline().strip().split()]
        mass.append((int(number), letter))
    mass.sort()
    basket = 0
    count = 0
    count_z = 0
    for i in range(n):
        if mass[i][0] + basket > m:
            break
        basket += mass[i][0]
        if mass[i][1] == "Z":
            count_z += 1
        count += 1
    difference = m - basket
    max_number = 0
    for i in range(count, n):
        if mass[i][0] - mass[count - 1][0] <= difference:
            max_number = mass[i][0]
    print(count_z, m - (basket - mass[count - 1][0] + max_number))
