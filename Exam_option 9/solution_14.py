number = 9 ** 8 + 3 ** 5 - 2
print(number)
remainder_list = []
while number // 3 > 0:
    remainder_list.append(str(number % 3))
    number //= 3
remainder_list.append(str(number))
print(remainder_list.count("2"))
