massive = [0] * 53
massive[50] = 1
for i in range(49, 0, -1):
    a = 0
    if i + 3 <= 50:
        a += massive[i + 3]
    for j in range(0, 7):
        if i * 7 + j <= 50:
            a += massive[i * 7 + j]
    massive[i] = a
print(massive)
print(massive[1])

