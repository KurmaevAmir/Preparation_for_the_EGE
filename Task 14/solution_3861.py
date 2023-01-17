for i in range(1, 100):
    expression = 27 ** 7 - 3 ** 11 + 36 - i
    remainders_list = []
    while expression // 3 > 0:
        remainders_list.append(expression % 3)
        expression //= 3
    remainders_list.append(expression)
    if sum(remainders_list) == 22:
        print(i)
        break
