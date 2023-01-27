def change_base(number, base):
    number_with_standart_base = 0
    for i in range(len(number)):
        number_with_standart_base += int(number[i]) * base ** (len(number) - 1 - i)
    return number_with_standart_base


for x in range(11):
    n1 = change_base(f'3364{x}', 11)
    n2 = change_base(f'{x}7946', 12)
    n3 = change_base(f'55{x}87', 14)
    if n1 + n2 == n3:
        print(n3)
