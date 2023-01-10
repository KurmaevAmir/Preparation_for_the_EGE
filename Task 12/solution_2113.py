for i in range(50, 1, -1):
    number = "6" * i
    while "66" in number:
        number = number.replace("66", "1", 1)
        number = number.replace("11", "2", 1)
        number = number.replace("22", "6", 1)
    if number == "21":
        print(i)
        break
