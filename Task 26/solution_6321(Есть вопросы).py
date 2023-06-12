with open("Files/6321", "r") as f:
    n, m = [int(i) for i in f.readline().strip().split()]
    input_mass = []
    for i in range(m):
        a, b = [int(i) for i in f.readline().strip().split()]
        input_mass.append([a, b])
    input_mass.sort()

