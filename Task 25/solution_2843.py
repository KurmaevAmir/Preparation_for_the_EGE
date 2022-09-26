import math

for i in range(4234679, 10157812 + 1):
    count = 0
    l = []
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            count += 1
            l.append(j)
            if i // j != j:
                count += 1
                l.append(i // j)
        if count > 3:
            break
    if count == 3:
        l.sort()
        print(i, l[-1])
