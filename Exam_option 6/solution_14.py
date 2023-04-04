number = 9 ** 22 + 3 ** 66 - 12
remainder_list = []
while number // 3 > 0:
    remainder_list.append(number % 3)
    number //= 3
remainder_list.append(number)
print(remainder_list.count(2))
