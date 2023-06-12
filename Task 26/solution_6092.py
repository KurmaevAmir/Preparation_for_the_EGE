with open("Files/6092", "r") as f:
    n, k = [int(i) for i in f.readline().strip().split()]
    input_mass = []
    for i in range(n):
        input_mass.append(int(f.readline().strip()))
    input_mass.sort(reverse=True)
    total_list = []
    while bool(input_mass):
        block = [input_mass[0]]
        input_mass[0] = 0
        for i in range(1, len(input_mass)):
            if block[-1] - input_mass[i] >= k:
                block.append(input_mass[i])
                input_mass[i] = 0
        input_mass = [i for i in input_mass if i != 0]
        total_list.append(block)
    print(len(total_list), max([len(i) for i in total_list]))
