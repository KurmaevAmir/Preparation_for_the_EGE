n = 5 ** 55 + 5 ** 555 * 555 - 5
remainder_list = []
while n // 5 > 0:
    remainder_list.append(str(n % 5))
    n //= 5
remainder_list.append(str(n))
print(remainder_list.count("0"))
