with open("Files/4741", "r") as f:
    n, k = [int(i) for i in f.readline().strip().split()]
    mass = []
    count = 0
    max_count = 0
    max_time = 0
    start_time = k
    end_time = k + 24 * 3600000
    for i in range(n):
        numbers = [int(i) for i in f.readline().strip().split()]
        if numbers[1] == 0:
            numbers[1] = end_time
        if numbers[0] >= end_time or numbers[1] <= start_time:
            continue
        mass.append([(max(start_time, numbers[0]), 1), (min(numbers[1], end_time, - 1))])
    mass.sort()
    a = 0
    b = 0
    c = 0
    t0 = 0
    for t, d in mass:
        b += d
        if b > a:
            a, c = b, 0
        if b - d == a:
            c += t - t0
        t0 = t
    print(a, c)
