n = 7 ** 2103 - 6 * 7 ** 1270 + 3 * 7 ** 57 - 98
remainders_list = []
while n // 7 > 0:
    remainders_list.append(n % 7)
    n //= 7
remainders_list.append(n)
print(sum(remainders_list))
