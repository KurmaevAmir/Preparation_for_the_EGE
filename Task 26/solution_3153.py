with open("Files/3153", "r") as f:
    n, m = [int(i) for i in f.readline().strip().split()]
    mass = []
    start_m = []
    for i in range(n):
        number = int(f.readline().strip())
        if 180 <= number <= 200:
            start_m.append(number)
        else:
            mass.append(number)
    mass.sort()
    loaded = []
    m -= sum(start_m)
    for i in range(len(mass)):
        if sum(loaded) + mass[i] > m:
            break
        loaded.append(mass[i])
    difference = m - sum(loaded)
    for i in range(len(loaded), len(mass)):
        if mass[i] - mass[len(loaded) - 1] <= difference:
            max_loaded = mass[i]
    print(len(loaded) + len(start_m), sum(start_m) + max_loaded + sum(loaded) - loaded[-1])
