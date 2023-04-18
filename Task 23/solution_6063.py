massive = [0] * 50
massive[1] = 1
for i in range(2, 50):
    if str(i).count("5") != 0:
        massive[i] = 0
    else:
        a = massive[i - 1]
        if i - 3 >= 1:
            a += massive[i - 3]
        if i % 3 == 0 and i // 3 >= 1:
            a += massive[i // 3]
        massive[i] = a
print(massive[49])
