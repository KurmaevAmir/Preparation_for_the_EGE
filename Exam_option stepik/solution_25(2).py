import math

for i in range(194455, 194500 + 1):
    divisors_list = []
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            divisors_list.append(j)
            if i // j != j:
                divisors_list.append(i // j)
    if len(divisors_list) == 4:
        divisors_list.sort()
        print(divisors_list[-2], divisors_list[-1])
