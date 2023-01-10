number = 70 * "3"
while "333" in number or "77777" in number:
    if "333" in number:
        number = number.replace("333", "77", 1)
    else:
        number = number.replace("77777", "7", 1)
print(sum([int(i) for i in number]))
