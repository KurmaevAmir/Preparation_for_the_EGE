massive = [0] * 18
massive[1] = 1
for i in range(2, 18):
    a = massive[i - 1]
    if i % 2 == 0 and i // 2 >= 1:
        a += massive[i // 2]
    if i % 4 == 0 and i // 4 >= 1:
        a += massive[i // 4]
    massive[i] = a
print(massive[17])
