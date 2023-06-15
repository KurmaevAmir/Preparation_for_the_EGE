with open("Input_files_28133/28133_B.txt", "r") as f:
    n = int(f.readline().strip())
    input_mass = []
    for i in range(n):
        input_mass.append(int(f.readline().strip()))
    m = 120
    massive = [0] * m
    sum_numbers, number1, number2 = 0, 0, 0
    for i in range(n):
        remainder = input_mass[i] % m
        d = (m - remainder) % m
        if massive[d] != 0 and massive[d] > input_mass[i]:
            if massive[d] + input_mass[i] > sum_numbers:
                sum_numbers = massive[d] + input_mass[i]
                number1 = massive[d]
                number2 = input_mass[i]
        massive[remainder] = max(massive[remainder], input_mass[i])
print(number1, number2)
