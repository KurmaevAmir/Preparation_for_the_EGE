n = 36 ** 15 + 6 ** 38 - 11
remainder_list = []
while n // 6 > 0:
    remainder_list.append(str(n % 6))
    n //= 6
remainder_list.append(str(n))
print(remainder_list.count("0"))
