factorial = [0] * 2024
factorial[1] = 1
for n in range(2, 2024):
    factorial[n] = n * factorial[n - 1]
print(factorial[2023] / factorial[2020])
