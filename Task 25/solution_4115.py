import math

count = 1
for i in range(150000, 300000):
    s = 0
    if count == 8:
        break
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            s += j
            if i // j != j:
                s += i // j
    if s % 13 == 10:
        count += 1
        print(i, s)
