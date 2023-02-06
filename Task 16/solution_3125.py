def function_f(n):
    if n > 1:
        return 2 * function_f(n - 1) + function_g(n - 1) - 2
    elif n == 1:
        return 1


def function_g(n):
    if n > 1:
        return function_f(n - 1) + 2 * function_g(n - 1)
    elif n == 1:
        return 1


print(function_f(14) + function_g(14))
