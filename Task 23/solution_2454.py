massive = [0] * 9
massive[2] = 1
for i in range(3, 9):
    a = massive[i - 1]
    if (i - 2) >= 2:
        a += massive[i - 2]
    if i % 3 == 0 and i // 3 >= 2:
        a += massive[i // 3]
    massive[i] = a
print(massive[8])
massive = [0] * 11
massive[8] = 1
for i in range(9, 11):
    a = massive[i - 1]
    if (i - 2) >= 8:
        a += massive[i - 2]
    if i % 3 == 0 and i // 3 >= 8:
        a += massive[i // 3]
    massive[i] = a
print(massive[10])
massive = [0] * 13
massive[10] = 1
for i in range(11, 13):
    a = massive[i - 1]
    if (i - 2) >= 10:
        a += massive[i - 2]
    if i % 3 == 0 and i // 3 >= 10:
        a += massive[i // 3]
    massive[i] = a
print(massive[12])
