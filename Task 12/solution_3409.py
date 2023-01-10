number = 204 * "7"
while "4444" in number or "777" in number:
    if "4444" in number:
        number = number.replace("4444", "77", 1)
    else:
        number = number.replace("777", "4", 1)
print(number)
