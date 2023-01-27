n = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
remainders_list = []
while n // 5 > 0:
    remainders_list.append(n % 5)
    n //= 5
remainders_list.append(n)
print(sum(remainders_list))
