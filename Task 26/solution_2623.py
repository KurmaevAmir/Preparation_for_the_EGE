with open("Files/2623", "r") as f:
    s, n = [int(i) for i in f.readline().strip().split()]
    mass = []
    for i in range(n):
        number = int(f.readline().strip())
        mass.append(number)
    mass.sort()
    a = 0
    count = 0
    for i in range(len(mass)):
        if a + mass[i] > s:
            break
        a += mass[i]
        count += 1
    print(count)
    b = s - a
    for i in range(count, len(mass)):
        if mass[i] - mass[count - 1] <= b:
            c = mass[i]
    print(c)
