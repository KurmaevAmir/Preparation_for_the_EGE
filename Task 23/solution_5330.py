massive = [0] * 30
massive[28] = 1
for i in range(27, 9, -1):
    a = massive[i + 2]
    if i * 2 <= 28:
        a += massive[i * 2]
    if i * 2 + 1 <= 28:
        a += massive[i * 2 + 1]
    massive[i] = a
print(massive[10])
massive = [0] * 12
massive[10] = 1
for i in range(9, 0, -1):
    a = massive[i + 2]
    if i * 2 <= 10:
        a += massive[i * 2]
    if i * 2 + 1 <= 10:
        a += massive[i * 2 + 1]
    massive[i] = a
print(massive[1])
print(9 * 4)
