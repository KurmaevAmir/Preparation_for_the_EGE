def change_base(number, base):
    number_with_standart_base = 0
    for i in range(len(number)):
        number_with_standart_base += int(abc_for_change[number[i]]) * base ** (len(number) - 1 - i)
    return number_with_standart_base


abc = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
       6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B",
       12: "C", 13: "D", 14: "E", 15: "F"}
abc_for_change = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
                  "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                  "A": 10, "B": 11, "C": 12, "D": 13, "E": 14,
                  "F": 15, "D": 16}
for x in range(15):
    n1 = change_base(f'131{abc[x]}1', 15)
    n2 = change_base(f'13{abc[x]}3', 17)
    if (n1 + n2) % 11 == 0:
        total_number = (n1 + n2) // 11
print(total_number)
