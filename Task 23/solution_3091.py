massive = [0] * 47
massive[30] = 1
for i in range(31, 47):
    a = massive[i - 1]
    if i - 4 >= 30:
        a += massive[i - 4]
    if i - 5 >= 30:
        a += massive[i - 5]
    massive[i] = a
print(massive[46])
