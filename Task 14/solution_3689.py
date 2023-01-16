def prime_number_test(number):
    if number < 10:
        if number in [2, 3, 5, 7]:
            return True
        return False
    elif number % 2 == 0 or number % 10 == 5:
        return False
    for j in range(3, number):
        if number % j == 0:
            return False
    return True


a = 437
total_list = []
for i in range(2, 11):
    n = a
    remainder_list = []
    while n // i > 0:
        remainder_list.append(n % i)
        n //= i
    remainder_list.append(n)
    if prime_number_test(sum(remainder_list)):
        total_list.append(i)
print(sum(total_list))
