for i in range(15):
    number1 = int(f'97968{hex(i)[2:]}15', 15)
    number2 = int(f"7{hex(i)[2:]}233", 15)
    if (number1 + number2) % 14 == 0:
        print((int(f'97968{hex(i)[2:]}15', 15) + int(f"7{hex(i)[2:]}233", 15)) // 14)
        break
