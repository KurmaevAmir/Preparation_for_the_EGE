massive = [0] * 17
massive[1] = 1
massive[2] = 2
for i in range(3, 17):
    a = massive[i - 2]
    if i - 2 >= 1:
        a += massive[i - 2]
    if i - 3 >= 1:
        a += massive[i - 3]
    if i % 4 == 0 and i // 4 >= 1:
        a += massive[i // 4]
    massive[i] = a
print(massive[16])
