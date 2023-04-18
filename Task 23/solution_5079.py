massive = [0] * 16
massive[2] = {1: 1, 2: 0, 3: 0}
for i in range(3, 16):
    if i == 12:
        massive[i] = {1: 0, 2: 0, 3: 0}
    else:
        massive[i] = {1: 0, 2: 0, 3: 0}
        if i - 1 >= 2:
            massive[i][1] = massive[i - 1][1] + massive[i - 1][2] + massive[i - 1][3]
        if i - 2 >= 2:
            massive[i][2] = massive[i - 2][1] + massive[i - 2][2] + massive[i - 2][3]
        if i % 3 == 0 and i // 3 >= 2:
            massive[i][3] = massive[i // 3][1] + massive[i // 3][2]
print(massive[15])
massive = [0] * 31
massive[15] = {1: 1, 2: 0, 3: 0}
for i in range(16, 31):
    if i == 20:
        massive[i] = {1: 0, 2: 0, 3: 0}
    else:
        massive[i] = {1: 0, 2: 0, 3: 0}
        if i - 1 >= 15:
            massive[i][1] = massive[i - 1][1] + massive[i - 1][2] + massive[i - 1][3]
        if i - 2 >= 15:
            massive[i][2] = massive[i - 2][1] + massive[i - 2][2] + massive[i - 2][3]
        if i % 3 == 0 and i // 3 >= 15:
            massive[i][3] = massive[i // 3][1] + massive[i // 3][2]
print(massive[30])
massive = [0] * 39
massive[30] = {1: 1, 2: 0, 3: 0}
for i in range(31, 39):
    massive[i] = {1: 0, 2: 0, 3: 0}
    if i - 1 >= 30:
        massive[i][1] = massive[i - 1][1] + massive[i - 1][2] + massive[i - 1][3]
    if i - 2 >= 30:
        massive[i][2] = massive[i - 2][1] + massive[i - 2][2] + massive[i - 2][3]
    if i % 2 == 0 and i // 2 >= 30:
        massive[i][3] = massive[i // 2][1] + massive[i // 2][2]
print(massive[38])
# 1 234 550
