massive = [0] * 11
massive[1] = 1
massive[2] = 2
for i in range(3, 11):
    if i % 2 == 0:
        massive[i] = massive[i // 2] + massive[i - 1]
    else:
        massive[i] = massive[i - 1]
print(massive[10])
massive = [0] * 21
massive[10] = 2
for i in range(11, 21):
    if i % 2 == 0 and i // 2 >= 20:
        massive[i] = massive[i // 2] + massive[i - 1]
    else:
        massive[i] = massive[i - 1]
print(massive[20])

