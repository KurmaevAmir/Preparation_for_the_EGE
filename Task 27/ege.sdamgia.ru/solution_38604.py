# with open("Input_files_38604/27_A.txt", "r") as f:
#     n = int(f.readline().strip())
#     input_mass = []
#     for i in range(n):
#         input_mass.append(int(f.readline().strip()))
#     min_len = float('inf')
#     max_sum = 0
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             i_sum = sum(input_mass[i:j])
#             if i_sum % 43 == 0:
#                 if i_sum > max_sum:
#                     max_sum = i_sum
#                     min_len = len(input_mass[i:j])
#                 elif i_sum == max_sum and len(input_mass[i:j]) < min_len:
#                     min_len = input_mass[i:j]
# print(min_len)


def function(file):
    with open(file, "r") as f:
        input_mass = []
        n = int(f.readline().strip())
        for i in range(n):
            input_mass.append(int(f.readline().strip()))
        r_list = [None] * 43
        l_list = [None] * 43
        max_sum = 0
        min_len = 0
        s = 0
        l = 0
        for i in range(n):
            s += input_mass[i]
            l += 1
            if s % 43 == 0:
                max_sum = s
                min_len = l
            else:
                difference = s % 43
                if r_list[difference] is None:
                    r_list[difference] = s
                    l_list[difference] = l
                else:
                    new_s = s - r_list[difference]
                    new_l = l - l_list[difference]
                    if new_s > max_sum:
                        max_sum = new_s
                        min_len = new_l
                    elif new_s == max_sum and new_l < min_len:
                        min_len = new_l
    return min_len


print(function("Input_files_38604/27_A.txt"))
print(function("Input_files_38604/27_B.txt"))
