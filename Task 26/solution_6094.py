with open("Files/6094", "r") as f:
    n, k, m = [int(i) for i in f.readline().strip().split()]
    input_mass = []
    for i in range(n):
        number, letter = [i for i in f.readline().strip().split()]
        input_mass.append((int(number), letter))
    input_mass.sort(reverse=True)
    massive1 = []
    while True:
        if input_mass[0][0] == 0:
            break
        a = [input_mass[0]] # Текущий блок
        input_mass.pop(0)
        input_mass.append((0, 0))
        i = 0
        while i < len(input_mass):
            if input_mass[i][0] == 0:
                break
            if input_mass[i][1] != a[-1][1]:
                if a[-1][0] - input_mass[i][0] >= k:
                    a.append(input_mass[i])
                    input_mass.pop(i)
                    input_mass.append((0, 0))
                    i -= 1
            i += 1
            if len(a) == m:
                break
        massive1.append(a)
    count = 0
    for i in massive1:
        if len(i) == m:
            count += 1
    print(len(massive1), count)
