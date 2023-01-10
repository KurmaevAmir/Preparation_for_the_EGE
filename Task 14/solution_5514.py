for i in range(43, -1, -1):
    number = 1 * 44 ** 3 + i * 44 ** 2 + 2 * 44 + 3
    number2 = 3 * 44 ** 3 + 2 * 44 ** 2 + i * 44 + 1
    if (number + number2) % 42 == 0:
        print((number + number2) // 42)
        break
