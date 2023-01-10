for i in range(90, 150):
    number = i * "1"
    while "111" in number:
        number = number.replace("111", "2", 1)
        number = number.replace("2222", "333", 1)
        number = number.replace("33", "1", 1)
    print(i, number.count("1")) # 110
