for n in range(4, 100):
    number = "2" + n * "5"
    while "25" in number or "355" in number or "555" in number:
        number = number.replace("25", "5", 1)
        number = number.replace("355", "52", 1)
        number = number.replace("555", "3", 1)
    if number.count("3") == 2:
        print(n)
        break
# 18
