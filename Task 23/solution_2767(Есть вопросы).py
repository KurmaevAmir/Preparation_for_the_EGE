massive = [0] * 26
massive[22] = 1
for i in range(21, 3, -1):
    a = massive[i + 1]
    if i + 3 <= 22:
        a += massive[i + 3]
    massive[i] = a
    if i % 4 == 3:
        massive[3] += a
    if i % 4 == 2:
        massive[2] += a
massive[3] += massive[4]
massive[3] += massive[6]
massive[2] += massive[3]
massive[2] += massive[5]
print(massive[2])
