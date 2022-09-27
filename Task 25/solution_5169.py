import math


def check_number(n):
    if n < 10:
        if n in [2, 3, 5, 7]:
            return True
        return False
    elif n % 2 == 0 or n % 10 == 5:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


total_list = [(2, 1)]
for i in range(2, 15):
    z = math.factorial(i)
    count = 0
    for j in range(2, int(math.sqrt(z)) + 1):
        if check_number(j):
            if z % j == 0:
                count += 1
                if z // j != j and check_number(z // j):
                    count += 1
    if count % 2 != 0:
        total_list.append((i, count))
for i in total_list:
    print(i[0], i[1])
