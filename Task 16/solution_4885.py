def function(n):
    if n <= 1:
        return 1
    elif n > 1 and n % 2 == 0:
        return 11 * n + function(n - 1)
    return 11 * function(n - 2) + n


summ_number = 0
for number in range(35, 51):
    check_number = function(number)
    if check_number % 2 == 0:
        summ_number += function(number)
print(len(str(summ_number)))
