n = 3 * 5 ** 1984 - 7 * 25 ** 777 - 11 * 125 * 666 - 404
remainders_list = []
while n // 5 > 0:
    remainders_list.append(n % 5)
    n //= 5
remainders_list.append(n)
print(remainders_list.count(2))
