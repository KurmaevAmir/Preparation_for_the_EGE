massive = [0] * 17
massive[1] = 1
for i in range(2, 17):
    a = massive[i - 2]
    if i % 2 == 0:
        a += massive[i // 2]
    massive[i] = a
print(massive[16])
massive = [0] * 35
massive[16] = 1
for i in range(17, 35):
    a = massive[i - 2]
    if i % 2 == 0:
        a += massive[i // 2]
    massive[i] = a
print(massive[34])
