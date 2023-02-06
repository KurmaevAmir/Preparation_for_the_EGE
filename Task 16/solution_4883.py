def function(n):
    if n == 0:
        return 1
    elif n > 0:
        return 7 * (n - 1) + function(n - 1)


def check_number(number):
    if number < 10:
        if number in [2, 3, 5, 7]:
            return True
        return False
    elif number % 2 == 0 or number % 10 == 5:
        return False
    for i in range(3, number):
        if number % i == 0:
            return False
    return True


count = 0
for i in range(2, 201):
    if check_number(function(i)):
        count += 1
print(count)
