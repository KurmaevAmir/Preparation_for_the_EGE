from math import sqrt

massive = [0] * 28
massive[2] = 1
for i in range(3, 28):
    a = massive[i - 1]
    if i % 2 == 0 and i // 2 >= 2:
        a += massive[i // 2]
    if int(sqrt(i)) == sqrt(i) and sqrt(i) >= 2:
        a += massive[int(sqrt(i))]
    massive[i] = a
print(massive[27])
