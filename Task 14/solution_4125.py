n = 81 ** 18 - (81 ** 8 - 1) * ((8 + 1) ** 8 + 1) // 8 - 8
remainders_list = []
while n // 3 > 0:
    remainders_list.append(n % 3)
    n //= 3
remainders_list.append(n)
print(remainders_list.count(1))
