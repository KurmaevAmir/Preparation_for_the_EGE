number = (64 ** 25 + 4 ** 10) - (16 ** 20 + 32 ** 3)
remainder_list = []
while number // 4 > 0:
    remainder_list.append(number % 4)
    number //= 4
remainder_list.append(number)
for i in range(0, len(remainder_list) - 1):
    if remainder_list[i] == 2:
        print(i)
        break
