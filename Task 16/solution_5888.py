help_list = [0] * 4965
help_list[0] = -1
help_list[1] = 0
help_list[2] = 1
help_list[3] = 2
for i in range(4, 4965):
    if i % 2 == 0:
        help_list[i] = help_list[i - 2] + i // 2 - help_list[i - 4]
    else:
        help_list[i] = help_list[i - 1] * i + help_list[i - 2]
print(help_list[4952] + 2 * help_list[4958] + help_list[4964])
print(help_list[:6])
