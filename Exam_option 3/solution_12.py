for i in range(101, 120):
    number = "3" * i
    while "111" in number or "333" in number:
        if "111" in number:
            number = number.replace("111", "3", 1)
        else:
            number = number.replace("333", "1", 1)
    print(i, number) # 107
