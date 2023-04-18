massive = [0] * 11
massive[4] = {1: 0, 2: 1, 3: 0}
for i in range(5, 11):
    massive[i] = {1: 0, 2: 0, 3: 0}
    if i - 1 >= 4:
        massive[i][1] = massive[i - 1][2] + massive[i - 1][3]
    if i - 3 >= 4:
        massive[i][2] = massive[i - 3][1] + massive[i - 3][2] + massive[i - 3][3]
    if i % 2 == 0 and i // 2 >= 4:
        massive[i][3] = massive[i // 2][1] + massive[i // 2][2] + massive[i // 2][3]
print(massive[10])
massive = [0] * 94
massive[10] = {1: 0, 2: 1, 3: 0}
for i in range(11, 94):
    if i == 28:
        massive[i] = {1: 0, 2: 0, 3: 0}
    else:
        massive[i] = {1: 0, 2: 0, 3: 0}
        if i - 1 >= 10:
            massive[i][1] = massive[i - 1][2] + massive[i - 1][3]
        if i - 3 >= 10:
            massive[i][2] = massive[i - 3][1] + massive[i - 3][2] + massive[i - 3][3]
        if i % 2 == 0 and i // 2 >= 10:
            massive[i][3] = massive[i // 2][1] + massive[i // 2][2] + massive[i // 2][3]
print(massive[93])
#14200552
