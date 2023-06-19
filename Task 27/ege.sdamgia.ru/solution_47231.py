import math


def function_a(file):
    with open(file, "r") as f:
        n = int(f.readline().strip())
        input_list = []
        number_biomaterials = 36
        for i in range(n):
            point, number = [int(i) for i in f.readline().strip().split()]
            number_container = int(math.ceil(number / number_biomaterials))
            input_list.append([point, number_container])
    massive = [0] * n
    for i in range(0, n):
        s = 0
        for j in range(n):
            if i != j:
                s += abs(input_list[j][0] - input_list[i][0]) * input_list[j][1]
        massive[i] = s
    return min(massive)


def function_b(file):
    with open(file, "r") as f:
        n = int(f.readline().strip())
        input_list = []
        for i in range(n):
            point, number = [int(i) for i in f.readline().strip().split()]
            input_list.append([point, int(math.ceil(number / 36))])
    massive = [0] * n
    s = 0
    r_sum = 0
    l_sum = 0
    for i in range(1, n):
        s += abs(input_list[i][0] - input_list[0][0]) * input_list[i][1]
        r_sum += input_list[i][1]
    massive[0] = s
    for i in range(1, n):
        massive[i] = massive[i - 1] - r_sum * (input_list[i][0] - input_list[i - 1][0]) + l_sum * (input_list[i][0] - input_list[i - 1][0]) + input_list[i - 1][1] * (input_list[i][0] - input_list[i - 1][0])
        r_sum = r_sum - input_list[i][1]
        l_sum = l_sum + input_list[i - 1][1]
    return min(massive)


print(function_a("Input_files_47231/27_A.txt"))
print(function_b("Input_files_47231/27_B.txt"))
