massive = [0] * 13
massive[3] = 1
for i in range(4, 13):
    a = massive[i - 1]
    if i % 2 == 0 and i // 2 >= 3:
        a += massive[i // 2]
    if i % 3 == 0 and i // 3 >= 3:
        a += massive[i // 3]
    massive[i] = a
print(massive[12])
massive = [0] * 47
massive[12] = 1
for i in range(13, 47):
    if i == 25:
        massive[i] = 0
    else:
        a = massive[i - 1]
        if i % 2 == 0 and i // 2 >= 12:
            a += massive[i // 2]
        if i % 3 == 0 and i // 3 >= 12:
            a += massive[i // 3]
        massive[i] = a
print(massive[46])
