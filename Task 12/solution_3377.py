number = 72 * "8"
while "222" in number or "888" in number:
    if "222" in number:
        number = number.replace("222", "8", 1)
    else:
        number = number.replace("888", "2", 1)
print(number)
