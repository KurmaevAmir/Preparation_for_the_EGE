number = "5" * 200
while "555" in number or "333" in number:
    if "555" in number:
        number = number.replace("555", "3", 1)
    else:
        number = number.replace("333", "5", 1)
print(sum([int(i) for i in number]))
