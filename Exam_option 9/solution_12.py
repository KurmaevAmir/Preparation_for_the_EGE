number = "1" * 100
while "111" in number:
    number = number.replace("11", "2", 1)
    number = number.replace("22", "1", 1)
print(number)
