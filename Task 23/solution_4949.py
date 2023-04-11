massive = [0] * 13
massive[1] = {1: 1, 2: 0, 3: 0}
for i in range(2, 13):
    massive[i] = {1: 0, 2: 0, 3: 0}
    if i - 1 >= 1:
        massive[i][1] = massive[i - 1][1] + massive[i - 1][2] + massive[i - 1][3]
    if i - 2 >= 1:
        massive[i][2] = massive[i - 2][1] + massive[i - 2][3]
    if i % 2 == 0 and i // 2 >= 1:
        massive[i][3] = massive[i // 2][1] + massive[i // 2][2] + massive[i // 2][3]
print(massive[12])
