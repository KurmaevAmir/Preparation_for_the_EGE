number = 9 ** 81 + 27 ** 729 - 4
remainders_list = []
while number // 9 > 0:
    remainders_list.append(number % 9)
    number //= 9
remainders_list.append(number)
max_number = max(remainders_list)
print(remainders_list.count(0) + remainders_list.count(max_number))
