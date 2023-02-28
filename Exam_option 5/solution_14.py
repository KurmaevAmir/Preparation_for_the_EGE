numbers = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
           9: "9", 10: "A", 11: "B", 12: "C", 0: "0"}
for i in range(13):
    number = int(f'8{numbers[i]}121', 13) - int(f'7{numbers[i]}575', 13)
    if number % 19 == 0:
        print(number // 19)
        break
