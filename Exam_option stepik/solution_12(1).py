for i in range(4, 100):
    number = "2" + "5" * i
    while "25" in number or "355" in number or "555" in number:
        number = number.replace("25", "5", 1)
        number = number.replace("355", "52", 1)
        number = number.replace("555", "3", 1)
    if sum([int(j) for j in number]) == 17:
        print(i)
        break
# 29
