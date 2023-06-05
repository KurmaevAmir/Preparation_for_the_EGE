with open("Files/2707", "r") as f:
    n = int(f.readline().strip())
    mass = []
    for i in range(n):
        mass.append(int(f.readline().strip()))
    mass.sort()
    max_volume = sum(mass) * 0.9
    compressed_volume = sum(mass) * 0.8
    max_volume1 = max_volume
    compressed_volume1 = compressed_volume
    total_list1 = []
    for number in mass:
        if compressed_volume1 - number * 0.8 <= max_volume1 - number:
            total_list1.append(number)
            compressed_volume1 -= number * 0.8
            max_volume1 -= number
        else:
            break
    print(len(total_list1))
    difference = max_volume1 - compressed_volume1
    for i in range(len(total_list1), len(mass)):
        if (mass[i] - mass[len(total_list1) - 1]) * 0.8 <= difference + mass[i] * 0.8:
            max_number = mass[i]
    print(max_number)
