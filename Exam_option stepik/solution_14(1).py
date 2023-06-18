x_15 = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
        10: "A", 11: "B", 12: "C", 13: "D", 14: "E"}
for x in range(15):
    number1 = int(f"97968{x_15[x]}15", 15)
    number2 = int(f"7{x_15[x]}233", 15)
    if (number1 + number2) % 14 == 0:
        print((number1 + number2) // 14)
        break
