function_list = [0] * 101
function_list[0] = 1
function_list[1] = 1
function_list[2] = 1
for i in range(3, 101):
    str_i = [int(j) for j in str(i)]
    if sum(str_i) % 2 == 0:
        function_list[i] = function_list[i - 1] - function_list[i - 2]
    else:
        function_list[i] = function_list[i - 1] + function_list[i // 2]
print(function_list[100])
