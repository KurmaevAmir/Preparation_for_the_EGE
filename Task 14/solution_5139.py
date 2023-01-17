n = 81 ** 79 + 75 ** 2022 - 12 ** 35
remainders_list = []
while n // 5 > 0:
    remainders_list.append(n % 5)
    n //= 5
remainders_list.append(n)
options_list = []
number_list = remainders_list[::-1]
for i in range(len(number_list) - 2):
    if number_list[i] == 4 and number_list[i + 1] in [1, 2, 3]:
        options_list.append(number_list[i + 1])
print(len(options_list))
