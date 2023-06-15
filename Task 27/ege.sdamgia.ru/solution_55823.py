with open("Input_files_55823/27B.txt", "r") as f:
    n = int(f.readline().strip())
    k = int(f.readline().strip())
    input_mass = []
    for i in range(n):
        input_mass.append(int(f.readline().strip()))
    massive = [0] * n
    a = 0
    for i in range(n):
        if input_mass[i] > a:
            a = input_mass[i]
        massive[i] = a
    b = 0
    for i in range(k, n):
        b = max(b, input_mass[i] + massive[i - k])
print(b)
