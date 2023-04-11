massive = [0] * 52
massive[25] = 1
for i in range(26, 52):
    a = massive[i - 1]
    if str(i)[-1] == "9":
        if i - 10 >= 25:
            a += massive[i - 10]
    elif i - 11 >= 25:
        a += massive[i - 11]
    massive[i] = a
print(massive[51])
