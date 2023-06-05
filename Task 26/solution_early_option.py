with open("Files/early_option.txt", "r") as f:
    k = int(f.readline().strip())
    n = int(f.readline().strip())
    mass = []
    for i in range(n):
        a, b = [int(i) for i in f.readline().strip().split()]
        mass.append((a, b))
    mass.sort(key=lambda x: x[0])
    massive = [0] * k
    a = 0
    last_number = 0
    for i in range(n):
        for j in range(k):
            if mass[i][0] > massive[j]:
                massive[j] = mass[i][1]
                a += 1
                last_number = j + 1
                break
    print(a, last_number)
