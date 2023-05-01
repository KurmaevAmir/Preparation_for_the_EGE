for i in range(4, 100):
    number = "3" + "5" * i
    while "25" in number or "355" in number or "555" in number:
        number = number.replace("25", "32", 1)
        number = number.replace("355", "25", 1)
        number = number.replace("555", "3", 1)
    sum_number = sum([int(i) for i in str(number)])
    if sum_number == 17:
        print(i)
        break
