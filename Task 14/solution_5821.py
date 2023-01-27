for x in range(10, 0, -1):
    base1 = int(f'132{x}4')
    n1 = 1 * base1 ** 1 + 3 * base1 ** 0
    n2 = 1 * 13 ** 4 + 3 * 13 ** 3 + 4 * 13 ** 2 + x * 13 ** 1 + 2 * 13 ** 0
    if (n1 - n2) % 30 == 0:
        print(abs(n1 - n2) // 30)
