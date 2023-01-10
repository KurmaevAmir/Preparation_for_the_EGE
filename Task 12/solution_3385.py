number = "7" * 120
while "8887" in number or "77" in number:
    if "8887" in number:
        number = number.replace("8887", "8", 1)
    else:
        number = number.replace("77", "8", 1)
print(number)
