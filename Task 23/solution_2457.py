massive = [0] * 7
massive[2] = 1
for i in range(3, 7):
    a = massive[i - 1]
    if (i - 4) >= 2:
        a += massive[i - 4]
    if i % 4 == 0 and i // 4 >= 2:
        a += massive[i // 4]
    massive[i] = a
print(massive[6])
massive = [0] * 25
massive[6] = 1
for i in range(7, 25):
    a = massive[i - 1]
    if i == 8:
        a = 0
    if (i - 4) >= 6:
        a += massive[i - 4]
    if i % 4 == 0 and i // 4 >= 6:
        a += massive[i // 4]
    massive[i] = a
print(massive[24])
