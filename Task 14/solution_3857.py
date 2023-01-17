for i in range(1, 100):
    expression = 36 ** 17 - 6 ** i + 71
    remainders_list = []
    while expression // 6 > 0:
        remainders_list.append(expression % 6)
        expression //= 6
    remainders_list.append(expression)
    if sum(remainders_list) == 61:
        print(i)
