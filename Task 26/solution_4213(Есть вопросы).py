with open("Files/4213", "r") as f:
    s, n = [int(i) for i in f.readline().strip().split()]
    mass_input = []
    for i in range(n):
        mass_input.append(int(f.readline().strip()))
    mass_input.sort()
    mass = []
    for number in mass_input:
        if mass_input.count(number) >= 2 and number not in mass:
            mass.append((number, mass_input.count(number)))
    total_list = []
    for i in range(len(mass)):
        if sum(total_list) + mass[i][0] > s:
            break
        elif sum(total_list) + (mass[i][0] * mass[i][1]) < s:
            for j in range(mass[i][1]):
                total_list.append(mass[i][0])
        else:
            count = mass[i][1]
            while sum(total_list) + (mass[i][0] * count) > s:
                count -= 1
            if count >= 3:
                for j in range(count):
                    total_list.append(mass[i][0])
    # difference = s - sum(total_list)
    # for i in range(len(total_list), len(mass)):
    #     for j in range(2, mass[i][0]):
    #         if mass[i][j] - mass[len(total_list) - 1][0] <= difference:
    #             max_number = (mass[i][0], mass[i][1])
    # for i in range(max_number[1]):
    #     total_list.append(max_number[0])
    # count = -float('inf')
    # for number in total_list:
    #     count = max(total_list.count(number), count)
    # print(sum(total_list), count)
