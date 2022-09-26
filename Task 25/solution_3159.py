import math

for i in range(500000, 1000000 + 1):
    n_max = 0
    count = 1
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0 and abs(i // j - j) <= 90:
            count += 1
            if n_max < i // j:
                n_max = i // j
        if count > 3:
            print(i, n_max)
            break
