number = 400 * '5'
count = 0
while "555" in number or "333" in number:
    if "555" in number:
        number = number.replace("555", "3", 1)
    else:
        number = number.replace("333", "5", 1)
        count += 3
print(count)
