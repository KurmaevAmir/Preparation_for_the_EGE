massive = [0] * 28
massive[2] = 1
for i in range(3, 28):
    a = massive[i - 1]
    if i % 3 == 0 and i // 3 >= 2:
        a += massive[i // 3]
    if i % 2 != 0 and i // 2 >= 2:
        a += massive[i // 2]
    massive[i] = a
print(massive)
