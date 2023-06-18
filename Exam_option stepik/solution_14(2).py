number_in_26 = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
                10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I",
                19: "G", 20: "K", 21: "L", 22: "M", 23: "N", 24: "O", 25: "P"}
max_x = -float("inf")
for x in range(25, -1, -1):
    cond = True
    for y in range(26):
        number1 = int(f"13{number_in_26[y]}{number_in_26[x]}5", 26)
        number2 = int(f"24{number_in_26[y]}13", 26)
        if (number1 + number2) % 8 != 0:
            cond = False
            break
    if cond:
        print((int(f"13{number_in_26[2]}{number_in_26[x]}5", 26) +
               int(f"24{number_in_26[2]}13", 26)) // 8)
        break
