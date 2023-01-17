n = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
abc = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4",
       5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
       10: "a", 11: "b", 12: "c", 13: "d", 14: "e"}
remainders_list = []
while n // 15 > 0:
    remainders_list.append(abc[n % 15])
    n //= 15
remainders_list.append(abc[n])
count = 0
for i in range(15):
    if remainders_list.count(abc[i]) > 0:
        count += 1
print(count)
