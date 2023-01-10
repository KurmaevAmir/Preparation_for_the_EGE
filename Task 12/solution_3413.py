number = 194 * "3"
while "9999" in number or "333" in number:
    if "9999" in number:
        number = number.replace("9999", "3", 1)
    else:
        number = number.replace("333", "99", 1)
print(number)
