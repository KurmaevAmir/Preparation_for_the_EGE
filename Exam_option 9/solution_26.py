with open("Files/26.txt", "r") as f:
    n = int(f.readline().strip())
    mass = []
    total_list = []
    for i in range(n):
        mass.append(int(f.readline().strip()))
    mass.sort(reverse=True)
    while bool(mass):
        block = [mass[0]]
        mass[0] = 0
        for i in range(1, len(mass)):
            if block[-1] - mass[i] >= 7:
                block.append(mass[i])
                mass[i] = 0
        mass = [int(i) for i in mass if i != 0]
        total_list.append(block)
print(len(total_list), max([len(i) for i in total_list]))
