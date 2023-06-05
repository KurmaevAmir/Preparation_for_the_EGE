with open("Files/2641", "r") as f:
    n, k = [int(i) for i in f.readline().strip().split()]
    mass = []
    for i in range(n):
        number = int(f.readline().strip())
        mass.append(number)
    mass.sort(reverse=True)
    print(int(sum(mass[k:2 * k]) // k))
    print(int(sum(mass[:k]) // k))
