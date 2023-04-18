massive = [0] * 901
massive[2] = 1
for i in range(3, 901):
    a = massive[i - 2]
    if str(i)[-1] == "2" and int(str(i)[:-1]) >= 2:
        a += massive[int(str(i)[:-1])]
    massive[i] = a
print(massive[900])
