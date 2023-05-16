import math

count = 0
for i in range(520000, 1000000):
    divisors_sum = 0
    max_divisor = -float("inf")
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            divisors_sum += j
            max_divisor = max(max_divisor, j)
            if i // j != j:
                divisors_sum += i // j
                max_divisor = max(max_divisor, i // j)
    if divisors_sum != 0:
        if len(str(divisors_sum)) % 2 == 0:
            if str(divisors_sum)[:len(str(divisors_sum)) // 2] == \
                    str(divisors_sum)[len(str(divisors_sum)) // 2:len(str(divisors_sum))][::-1]:
                count += 1
                print(i, max_divisor)
        else:
            if str(divisors_sum)[:len(str(divisors_sum)) // 2] == \
                    str(divisors_sum)[len(str(divisors_sum)) // 2 + 1:len(str(divisors_sum))][::-1]:
                count += 1
                print(i, max_divisor)
    if count == 5:
        break
