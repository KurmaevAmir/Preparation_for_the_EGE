massive = [0] * 112
massive[108] = 1
for i in range(107, 41, -1):
    a = massive[i + 3]
    if i * 2 <= 108:
        a += massive[i * 2]
    massive[i] = a
print(massive[42])
massive[44] = 0
massive[43] = 0
massive[42] = 1
for i in range(41, 11, -1):
    a = massive[i + 3]
    if i * 2 <= 42:
        a += massive[i * 2]
    massive[i] = a
print(massive[12])
# 30
