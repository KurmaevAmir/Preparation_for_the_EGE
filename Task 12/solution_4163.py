number = "13" + "1" * 198 + "3"
while "12" in number or "13" in number:
    number = number.replace("12", "21")
    number = number.replace("31", "23")
    number = number.replace("13", "23")
print(sum([int(i) for i in number]))
