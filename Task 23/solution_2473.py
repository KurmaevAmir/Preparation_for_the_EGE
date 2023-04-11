massive = [0] * 14
massive[2] = 1
for i in range(3, 14):
    if i == 6:
        massive[i] = 0
    else:
        a = massive[i - 1]
        if i - 2 >= 2:
            a += massive[i - 2]
        if i - 4 >= 2:
            a += massive[i - 4]
        massive[i] = a
print(massive[13])
