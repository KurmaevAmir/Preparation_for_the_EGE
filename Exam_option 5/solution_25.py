import math


def check_number(n):
    if n < 10:
        if n in [2, 3, 5, 7]:
            return True
        return False
    elif n % 2 == 0 or n % 5 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


for i in range(100000, 500001):
    divisors_list = []
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            if check_number(j):
                divisors_list.append(j)
            if i // j != j:
                if check_number(i // j):
                    divisors_list.append(i // j)
    divisors_list.sort()
    if len(divisors_list) > 3:
        difference = divisors_list[1] - divisors_list[0]
        cond = True
        for j in range(len(divisors_list) - 1):
            if divisors_list[j + 1] - divisors_list[j] != difference:
                cond = False
                break
        if cond:
            print(i, len(divisors_list) * difference)
