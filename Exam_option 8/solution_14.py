for x in range(10):
    number1 = int(f'123{x}5', 15)
    number2 = int(f'1{x}233', 15)
    if (number1 + number2) % 14 == 0:
        print((number1 + number2) // 14)
        break
