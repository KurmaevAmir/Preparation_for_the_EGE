import math

for i in range(2000000, 3000000 + 1):
    max_number = -float('inf')
    count = 0
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0 and abs(i // j - j) <= 120:
            count += 1
            if max(max_number, i // j) != max_number:
                max_number = i // j
        if count >= 3:
            print(i, max_number)
            break
