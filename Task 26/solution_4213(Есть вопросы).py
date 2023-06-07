with open("Files/4213", "r") as f:
    s, n = [int(i) for i in f.readline().strip().split()]
    mass_input = []
    for i in range(n):
        mass_input.append(int(f.readline().strip()))
    mass_input_set = set(mass_input)
    mass = []
    for number in mass_input_set:
        if mass_input.count(number) >= 2 and number not in mass:
            mass.append((number, mass_input.count(number)))
    mass.sort()
    print(mass)
    total_list = []
    total_count_list = []
    for i in range(len(mass)):
        if sum(total_list) + mass[i][0] > s:
            break
        elif sum(total_list) + (mass[i][0] * mass[i][1]) <= s:
            for j in range(mass[i][1]):
                total_list.append(mass[i][0])
            total_count_list.append(mass[i][1])
        else:
            count = mass[i][1]
            while sum(total_list) + (mass[i][0] * count) > s:
                count -= 1
            if count >= 2:
                for j in range(count):
                    total_list.append(mass[i][0])
            total_count_list.append(count)
    sum_total = sum(total_list)
    difference = s - sum_total
    k = len(total_count_list)
    for j in range(-count, 0, 2):
        for i in range(k, len(mass)):
            if 2 * mass[i][0] - 2 * total_list[j] <= difference:
                sum_total -= 2 * total_list[j]
                sum_total += 2 * mass[i][0]
                difference = s - sum_total
                k += 1
                total_list[j] = mass[i][0]
                total_list[j + 1] = mass[i][0]
    print(max(total_list), max(total_count_list))
