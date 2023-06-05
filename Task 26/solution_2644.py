with open("Files/2644", "r") as f:
    n = int(f.readline().strip())
    mass = []
    for i in range(n):
        mass.append(int(f.readline().strip()))
    mass.sort()
    average_list = mass.copy()
    average_list = list(set(average_list))
    median = mass[n // 2]
    average = sum(average_list) // len(average_list)
    max_number = max(average, median)
    min_number = min(average, median)
    count = 0
    for elem in mass:
        if min_number <= elem <= max_number:
            count += 1
    print(count)
