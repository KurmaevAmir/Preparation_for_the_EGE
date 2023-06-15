def function(file):
    with open(f"Input_files_28133/{file}", "r") as f:
        n = int(f.readline().strip())
        input_mass = []
        for i in range(n):
            input_mass.append(int(f.readline().strip()))
        m = 120
        total_list = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                if input_mass[i] > input_mass[j] and (input_mass[i] + input_mass[j]) % m == 0:
                    total_list.append([input_mass[i], input_mass[j], (input_mass[i] + input_mass[j])])
        total_list.sort(key=lambda x: x[2])
    if bool(total_list):
        return total_list[-1][:2]
    else:
        return "00"


print(*function("28133_A.txt"))
print(*function("28133_B.txt"))
