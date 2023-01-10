number = (13 * "1") + (13 * "2") + (13 * "3")
while "11" in number:
    number = number.replace("11", "2", 1)
    number = number.replace("22", "3", 1)
    number = number.replace("33", "1", 1)
print(number)
