# from itertools import product
#
# colors = "ROYGXBP"
# options_list = []
# for i in range(3, 10):
#     options_list += ["".join(z) for z in product(colors, repeat=i)]
# print(options_list)
# count = 0
# for option in options_list:
#     cond = True
#     for l in range(len(option) - 1):
#         if option[l] == option[l + 1]:
#             cond = False
#             break
#     if cond:
#         count += 1
# print(count)

n3 = 7 * 6 ** 2
n4 = 7 * 6 ** 3
n5 = 7 * 6 ** 4
n6 = 7 * 6 ** 5
n7 = 7 * 6 ** 6
n8 = 7 * 6 ** 7
n9 = 7 * 6 ** 8
print(n3 + n4 + n5 + n6 + n7 + n8 + n9)
