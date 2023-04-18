massive = [0] * 50
massive[5] = 1
for i in range(6, 50):
    a = massive[i - 2]
    if (i - 5) >= 5:
        a += massive[i - 5]
    if a == 34:
        print(i)
        break
    massive[i] = a
