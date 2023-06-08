with open("Files/3763", "r") as f:
    n = int(f.readline().strip())
    mass = []
    for i in range(n):
        mass.append(int(f.readline().strip()))
    mass.sort()
    total_list = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            count = 0
            average = (mass[i] + mass[j]) // 2
            for k in range(n):
                if average > mass[k]:
                    count += 1
                else:
                    break
            if count % 100 == 0 and count != 0:
                total_list.append(count)
    print(len(total_list), max(total_list))
