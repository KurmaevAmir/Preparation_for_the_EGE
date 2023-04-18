massive = [0] * 64
massive[7] = 1
for i in range(8, 64):
    if i == 43:
        massive[i] = 0
    else:
        a = 0
        if i - 2 >= 7:
            a += massive[i - 2]
        if i % 2 != 0:
            if i // 2 >= 7:
                a += massive[i // 2]
            if i // 2 + 1 >= 7:
                a += massive[i // 2 + 1]
        massive[i] = a
print(massive[63])
