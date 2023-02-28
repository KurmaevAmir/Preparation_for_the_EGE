number = "9" * 84
while "33333" in number or "999" in number:
    if "33333" in number:
        number = number.replace("33333", "99", 1)
    else:
        number = number.replace("999", "3", 1)
print(number)
