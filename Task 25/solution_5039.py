def change_base(n):
    remainder_list = []
    while n // 7 > 0:
        remainder_list.append(n % 7)
        n //= 7
    remainder_list.append(n)
    remainder_list.reverse()
    total_list = [str(i) for i in remainder_list]
    return int(''.join(total_list))


i = 0
j = 0
number = int(f'1{i}586{j}6')
while True:
    number = int(f'1{i}586{j}6')
    cond = True
    for j in range(10):
        number = int(f'1{i}586{j}6')
        if number > 2 * 10 ** 9:
            cond = False
            break
        number_basicSeven = change_base(number)
        for position in range(len(str(number)) // 2 + 1):
            if str(number_basicSeven)[position] != str(number_basicSeven)[(- 1 - position)]:
                break
        else:
            print(number, sum([int(i) for i in str(number_basicSeven)]))
    if cond is False:
        break
    i += 1
