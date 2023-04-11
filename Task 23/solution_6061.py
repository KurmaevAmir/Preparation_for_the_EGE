massive = [0] * 62
massive[1] = 1
for i in range(2, 62):
    if "7" in str(i):
        massive[i] = 0
    else:
        a = massive[i - 1]
        if i - 7 >= 1:
            a += massive[i - 7]
        massive[i] = a
print(massive[61])
