count = 0
number = "5" * 500
while "555" in number or "333" in number:
    if "333" in number:
        number = number.replace("333", "5", 1)
        count += 3
    else:
        number = number.replace("555", "3", 1)
print(count)
