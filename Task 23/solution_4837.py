massive = [0] * 12
massive[2] = 1
for i in range(3, 12):
    a = massive[i - 1]
    if (i - 4) >= 2:
        a += massive[i - 4]
    if (i // 2) % 2 != 0:
        if (i // 2 + 1) + i // 2 == i and i // 2 >= 2:
            a += massive[i // 2]
        elif (i // 2 - 1) + (i // 2 + 1) == i and i // 2 - 1 >= 2:
            a += massive[i // 2 - 1]
    massive[i] = a
print(massive[11])
massive = [0] * 27
massive[11] = 1
for i in range(12, 27):
    if i == 21:
        massive[i] = 0
    else:
        a = massive[i - 1]
        if (i - 4) >= 11:
            a += massive[i - 4]
        if (i // 2) % 2 != 0:
            if (i // 2 + 1) + i // 2 == i and i // 2 >= 11:
                a += massive[i // 2]
            elif (i // 2 - 1) + (i // 2 + 1) == i and i // 2 - 1 >= 11:
                a += massive[i // 2 - 1]
        massive[i] = a
print(massive[26])
