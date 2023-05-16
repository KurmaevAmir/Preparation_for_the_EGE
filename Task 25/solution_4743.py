import math

count = 0
for i in range(10000000, 20000000):
    divisors_list = []
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            divisors_list.append(j)
            if i // j != j:
                divisors_list.append(i // j)
    if len(divisors_list) >= 2:
        divisors_list.sort(reverse=True)
        s = divisors_list[0] + divisors_list[1]
        if s < 100000 and s % 31 == 0:
            print(i, s)
            count += 1
        if count == 5:
            break
