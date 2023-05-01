massive = [0] * 16
massive[2] = 1
for i in range(3, 16):
    if i == 11:
        massive[i] = 0
    else:
        a = massive[i - 1]
        if i % 2 == 0 and i // 2 >= 2:
            a += massive[i // 2]
        if i % 3 == 0 and i // 3 >= 2:
            a += massive[i // 3]
        massive[i] = a
print(massive[15])
massive = [0] * 26
massive[15] = 1
for i in range(16, 26):
    a = massive[i - 1]
    if i % 2 == 0 and i // 2 >= 15:
        a += massive[i // 2]
    if i % 3 == 0 and i // 3 >= 15:
        a += massive[i // 3]
    massive[i] = a
print(massive[25])
