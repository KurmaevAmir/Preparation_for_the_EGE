with open("Input_files_28131/28131_B.txt", "r") as f:
    n = int(f.readline().strip())
    input_mass = []
    for i in range(n):
        input_mass.append(int(f.readline().strip()))
    m = 120
    massive = [0] * m
    a, b, c = 0, 0, 0
    for i in range(n):
        remainder = input_mass[i] % m
        d = (m - remainder) % m
        if massive[d] != 0 and massive[d] > input_mass[i]:
            if massive[d] + input_mass[i] > a:
                a = massive[d] + input_mass[i]
                b = massive[d]
                c = input_mass[i]
        massive[remainder] = max(massive[remainder], input_mass[i])
print(b, c)
