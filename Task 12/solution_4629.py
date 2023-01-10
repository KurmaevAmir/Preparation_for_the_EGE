for i in range(201, 250):
    number = "8" * i
    while "555" in number or "888" in number:
        number = number.replace("555", "8", 1)
        number = number.replace("888", "55", 1)
    if number.count("8") == number.count("5"):
        print(i)
        break
