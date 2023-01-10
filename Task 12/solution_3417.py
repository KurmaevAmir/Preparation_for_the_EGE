number = "4" + "5" * 90
while "25" in number or "355" in number or "4555" in number:
    number = number.replace("25", "3", 1)
    number = number.replace("355", "4", 1)
    number = number.replace("4555", "2", 1)
print(number)
