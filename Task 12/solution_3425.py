number = "5" + "6" * 152 + "5"
while "63" in number or "664" in number or "6665" in number:
    if "63" in number:
        number = number.replace("63", "4", 1)
    elif "664" in number:
        number = number.replace("664", "65", 1)
    elif "6665" in number:
        number = number.replace("6665", "663", 1)
print(number)
