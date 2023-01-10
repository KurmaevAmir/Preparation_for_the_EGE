number = "1" + "0" * 33
while "1" in number or "100" in number:
    if "100" in number:
        number = number.replace("100", "0001", 1)
    else:
        number = number.replace("1", "00", 1)
print(number.count("0"))
