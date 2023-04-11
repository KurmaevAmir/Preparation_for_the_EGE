massive = [0] * 16
massive[1] = 1
for i in range(2, 16):
    a = massive[i - 1]
    if i % 2 == 0 and i // 2 >= 1:
        a += massive[i // 2]
    if (i - 1) % 2 == 0 and (i - 1) // 2 >= 1:
        a += massive[(i - 1) // 2]
    if i % 10 == 0 and i // 10 >= 1:
        a += massive[i // 10]
    massive[i] = a
print(massive[15])
