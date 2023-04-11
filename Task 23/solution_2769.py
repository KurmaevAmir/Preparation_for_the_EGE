massive = [0] * 32
massive[1] = 1
for i in range(2, 32):
    if i == 25:
        massive[i] = 0
    else:
        a = massive[i - 1]
        if (i - 1) % 2 == 0 and (i - 1) // 2 >= 1:
            a += massive[(i - 1) // 2]
        massive[i] = a
print(massive[31])
