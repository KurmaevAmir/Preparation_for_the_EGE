for x in range(10, 0, -1):
    base1 = int(f'123{x}4')
    base2 = int(f'124{x}3')
    n1 = 1 * base1 ** 2 + 2 * base1 ** 1 + 3 * base1 ** 0
    n2 = 1 * base2 ** 2 + 1 * base2 ** 1 + 1 * base2 ** 0
    if (n1 + n2) % 100 == 0:
        print((n1 + n2) // 100)
        break
