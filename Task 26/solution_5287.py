with open("Files/5287", "r") as f:
    n = int(f.readline().strip())
    input_mass = []
    for i in range(n):
        a, b, c = [int(i) for i in f.readline().strip().split()]
        input_mass.append([a, b, c])
    input_mass.sort()
    input_mass.append([0, 0, 0])
    total_list = []
    cond = False
    count_h = 0
    count_other = 0
    for i in range(n):
        if input_mass[i][0] == input_mass[i + 1][0] and \
                input_mass[i][2] == input_mass[i + 1][2] == 1 and \
                input_mass[i + 1][1] - input_mass[i][1] - 1 == 100:
            cond = True
            count_other += 1
        elif input_mass[i][0] != input_mass[i + 1][0]:
            if input_mass[i][2] == 0:
                count_h += 1
            else:
                count_other += 1
            if cond and count_h >= 500:
                total_list.append([input_mass[i][0], count_other])
            cond = False
            count_h = 0
            count_other = 0
        elif input_mass[i][2] == 0:
            count_h += 1
        elif input_mass[i][2] == 1:
            count_other += 1
    print(*total_list[-1])
