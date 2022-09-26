import math

for i in range(113000000, 114000000 + 1, 2):
    count = 2
    l = []
    for j in range(2, int(math.sqrt(i)) + 1, 2):
        if i % j == 0:
            count += 1
            l.append(j)
            if i // j != j and j % 2 == 0:
                count += 1
                l.append(i // j)
        if count > 3:
            break
    if count == 3:
        l.append(i)
        l.sort()
        print(i, l[-2])
