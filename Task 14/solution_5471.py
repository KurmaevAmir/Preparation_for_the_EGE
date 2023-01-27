n = 7 * 729 ** 543 - 6 * 81 ** 765 - 5 * 9 ** 987 - 20
remainder_list = []
while n // 9 > 0:
    remainder_list.append(str(n % 9))
    n //= 9
remainder_list.append(str(n))
print(remainder_list.count("8"))
