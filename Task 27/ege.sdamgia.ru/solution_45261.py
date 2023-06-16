# def function(file):
#     with open(file, "r") as f:
#         n = int(f.readline().strip())
#         input_mass = []
#         for i in range(n):
#             input_mass.append(int(f.readline().strip()))
#         min_cost = float('inf')
#         for i in range(n):
#             s = 0
#             for j in range(n):
#                 s += min(abs(i - j), n - abs(i - j)) * input_mass[j]
#             if s < min_cost:
#                 min_cost = s
#     return min_cost * 3
#
#
# print(function("Input_files_45261/107_27_A.txt"))

def function(file):
    with open(file, "r") as f:
        n = int(f.readline().strip())
        input_mass = []
        for i in range(n):
            input_mass.append(int(f.readline().strip()))
        massive = [0] * n
        s = 0
        r_sum = 0
        l_sum = 0
        for i in range(1, n // 2):
            s += input_mass[i] * i + input_mass[n - i] * i
            r_sum += input_mass[i]
            l_sum += input_mass[n - i]
        s += input_mass[n // 2] * n // 2
        massive[0] = s
        for i in range(1, n):
            massive[i] = massive[i - 1] + l_sum + input_mass[i - 1] - r_sum - input_mass[(i + n // 2 - 1) % n]
            r_sum = r_sum - input_mass[i] + input_mass[(i + n // 2 - 1) % n]
            l_sum = l_sum - input_mass[(i + n // 2) % n] + input_mass[i - 1]
        return min(massive) * 3


print(function("Input_files_45261/107_27_A.txt"))
print(function("Input_files_45261/107_27_B.txt"))
