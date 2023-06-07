def function_f(n):
    if n < 50:
        return n
    else:
        return 2 * function_g(50 - n // 2)


def function_g(n):
    if n > 40:
        return 10
    else:
        return 30 + function_f(n + 600 // n)


print(function_f(80))
