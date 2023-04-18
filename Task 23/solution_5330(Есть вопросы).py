massive = [0] * 30
massive[28] = 1
for i in range(27, 0, -1):
    a = massive[i + 2]
    if i * 2 <= 28:
        a += massive[i * 2]
    massive[i] = a
print(massive[1])
