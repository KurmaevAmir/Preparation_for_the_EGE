for i in range(100, 1000):
    number1 = int(str(i)[0]) * int(str(i)[1])
    number2 = int(str(i)[1]) * int(str(i)[2])
    if number1 > number2:
        number = int(str(number2) + str(number1))
    else:
        number = int(str(number1) + str(number2))
    if number == 621:
        max_number = i
print(max_number)
