with open("Input_files_28131/28131_A.txt", "r") as f:
    n = int(f.readline().strip())
    input_mass = []
    for i in range(n):
        input_mass.append(int(f.readline().strip()))
    total_list = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            if input_mass[i] > input_mass[j] and (input_mass[i] + input_mass[j]) % 120 == 0:
                total_list.append([input_mass[i], input_mass[j], input_mass[i] + input_mass[j]])
total_list.sort(key=lambda x: x[2])
print(total_list[-1][:2])
