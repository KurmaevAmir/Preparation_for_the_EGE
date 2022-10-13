import math

start = 75000000
k = 0
count = 0
while count != 5:
    number = start + k
    if number % 2 == 0:
        count_number = 1
    else:
        count_number = 0
    for j in range(2, int(math.sqrt(number)) + 1):
        if number % j == 0:
            if j % 2 == 0:
                count_number += 1
            if number // j != j and (number // j) % 2 == 0:
                count_number += 1
    if count_number % 2 != 0:
        count += 1
        print(k, count_number)
    k += 1
