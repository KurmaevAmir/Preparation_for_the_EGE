def function(n):
    if n <= 1:
        return n
    elif n > 1 and n % 3 == 0:
        return n + function(n // 3 - 1)
    elif n > 1 and n % 3 != 0:
        return False


for i in range(1000):
    answer_function = function(i)
    if answer_function is not False:
        if answer_function > 1000:
            print(i)
            break
