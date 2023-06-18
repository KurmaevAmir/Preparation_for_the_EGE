massive = [0] * 18
massive[16] = 1
for i in range(15, 10, -1):
    if i == 12:
        massive[12] = 0
    else:
        a = massive[i + 1] + massive[i + 2]
        if i * 3 <= 16:
            a += massive[i * 3]
        massive[i] = a
print(massive[11])
massive = [0] * 18
massive[11] = 1
for i in range(10, 5, -1):
    a = massive[i + 1] + massive[i + 2]
    if i * 3 <= 11:
        a += massive[i * 3]
    massive[i] = a
print(massive[6])
