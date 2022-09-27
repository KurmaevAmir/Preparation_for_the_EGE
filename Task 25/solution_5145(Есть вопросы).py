import math

start = 75000000
k = 0
count = 0
while count != 5:
    count_number = 0
    for j in range(2, int(math.sqrt(start + k)) + 1, 2):
        if (start + k) % j == 0:
            count_number += 1
            if (start + k) // j != j and (start + k) % 2 == 0:
                count_number += 1
    if count_number % 2 != 0:
        count += 1
        print(k, count_number)
    k += 2
