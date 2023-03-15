numbers = "5" * 400
count = 0
while "555" in numbers or "333" in numbers:
    if "555" in numbers:
        numbers = numbers.replace("555", "3", 1)
        count += 1
    elif "333" in numbers:
        numbers = numbers.replace("333", "5", 1)
        count += 1
print(count)
