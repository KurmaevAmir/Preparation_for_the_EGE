import math


def check_number(number):
    if number < 10:
        if number in [2, 3, 5, 7]:
            return True
        return False
    elif number % 2 == 0 or number % 10 == 5:
        return False
    for i in range(3, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


count = 1
for i in range(3144472, 3144600 + 1):
    if check_number(i):
        print(f'{count} {i}')
        count += 1
