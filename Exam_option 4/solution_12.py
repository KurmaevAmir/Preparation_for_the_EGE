for i in range(61, 80):
    number = i * "1"
    while "111" in number:
        number = number.replace("111", "2", 1)
        number = number.replace("222", "11", 1)
    if number == "221":
        print(i)
        break
