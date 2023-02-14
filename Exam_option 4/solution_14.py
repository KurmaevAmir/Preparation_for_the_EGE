number = 9 ** 11 * 3 ** 20 - 3 ** 9 - 27
remainder_list = []
while number // 3 > 0:
    remainder_list.append(str(number % 3))
    number //= 3
remainder_list.append(str(number))
print(remainder_list.count("2"))
