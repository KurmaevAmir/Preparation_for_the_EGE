massive = [0] * 9
massive[1] = 1
for i in range(2, 9):
    a = massive[i - 1]
    if (i - 2) >= 1:
        a += massive[i - 2]
    if i % 3 == 0 and i // 3 >= 1:
        a += massive[i // 3]
    massive[i] = a
print(massive[8])
massive = [0] * 29
massive[8] = 1
for i in range(9, 29):
    if i == 10 or i == 11:
        massive[i] = 0
    else:
        a = massive[i - 1]
        if (i - 2) >= 8:
            a += massive[i - 2]
        if i % 3 == 0 and i // 3 >= 8:
            a += massive[i // 3]
        massive[i] = a
print(massive[28])
