for i in range(40, 100):
    number = "1" * i
    while "111" in number:
        number = number.replace("111", "2", 1)
        number = number.replace("222", "1", 1)
    if number == "11":
        print(i)
        break
