sum_of_final_answers = 0
for x in range(158):
    n1 = 2 * 158 ** 4 + 7 * 158 ** 3 + 3 * 158 ** 2 + x * 158 ** 1 + 2 * 158 ** 0
    n2 = 1 * 158 ** 4 + x * 158 ** 3 + 3 * 158 ** 2 + 9 * 158 ** 1 + 0
    if (n1 + n2) % 73 == 0:
        sum_of_final_answers += (n1 + n2) // 73
print(sum_of_final_answers)
