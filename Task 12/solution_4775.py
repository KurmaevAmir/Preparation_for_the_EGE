for i in range(501, 520):
    number = i * "5"
    while "5555" in number:
        number = number.replace("5555", "8", 1)
        number = number.replace("88", "5", 1)
    print(i, len(number)) # 504
