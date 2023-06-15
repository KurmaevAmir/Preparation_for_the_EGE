with open("Input_files_27990/27990_B.txt", "r") as f:
    n = int(f.readline().strip())
    input_mass = []
    for i in range(n):
        input_mass.append(int(f.readline().strip()))
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (input_mass[i] * input_mass[j]) % 62 == 0:
                count += 1
print(count)
