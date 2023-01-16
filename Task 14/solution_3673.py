n = 26 ** 2 + 169 - 11
abc = {10: "A",
       11: "B",
       12: "C",
       0: "0",
       1: "1",
       2: "2",
       3: "3",
       4: "4",
       5: "5",
       6: "6",
       7: "7",
       8: "8",
       9: "9"}
remainder_list = []
while n // 13 > 0:
    remainder_list.append(abc[n % 13])
    n //= 13
remainder_list.append(abc[n])
print(remainder_list.count("C") + remainder_list.count("2"))
