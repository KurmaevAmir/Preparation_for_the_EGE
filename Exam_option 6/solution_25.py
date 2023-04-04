abc = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
       6: "6", 7: "7", 8: "8", 9: "9", 10: "A",
       0: "0"}
for i in range(2031, 14313):
    number = i
    remainder_list = []
    while i // 11 > 0:
        remainder_list.append(abc[i % 11])
        i //= 11
    remainder_list.append(abc[i])
    if remainder_list.count("2") == 0:
        max_number = number
print(max_number)
