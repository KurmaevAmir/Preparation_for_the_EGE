import math

for i in range(177399, 177453 + 1):
    count = 2
    l = []
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            count += 1
            l.append(j)
            if i // j != j:
                count += 1
                l.append(i // j)
        if count > 6:
            break
    if count == 6:
        l.sort()
        print(l[-1], i)
