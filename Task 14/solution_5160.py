i = 0
total_list = set()
n = f'3 * 16 ** 2018 - 2 * 8 ** 1028 - 3 * 4 ** 1100 - 4 ** {i} - 2022'
while eval(n) > 0:
    number = eval(n)
    remainders_list = []
    while number // 4 > 0:
        remainders_list.append(number % 4)
        number //= 4
    remainders_list.append(number)
    total_list.add(sum(remainders_list))
    i += 1
    n = f'3 * 16 ** 2018 - 2 * 8 ** 1028 - 3 * 4 ** 1100 - 4 ** {i} - 2022'
print(len(total_list))
