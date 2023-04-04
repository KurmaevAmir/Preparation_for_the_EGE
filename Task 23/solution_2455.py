mass = [0] * 23
mass[1] = 1
mass[2] = 1
mass[3] = 2
for i in range(4, 23):
    if i % 3 == 0:
        mass[i] = mass[i - 1] + mass[i // 3]
    else:
        mass[i] = mass[i - 1]
print(mass[22])
mass = [0] * 71
mass[22] = 1
for i in range(23, 71):
    if i % 3 == 0 and i // 3 >= 22:
        mass[i] = mass[i - 1] + mass[i // 3]
    else:
        mass[i] = mass[i - 1]
print(mass[70])
