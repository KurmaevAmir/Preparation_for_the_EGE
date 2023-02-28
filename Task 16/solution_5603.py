function_list = 12346 * [0]
for i in range(12345, 1, -1):
    if i > 10000:
        function_list[i] = i - 10000
    else:
        function_list[i] = function_list[i + 1] + function_list[i + 2]
print(function_list[12345] * (function_list[10] - function_list[12]) // function_list[11] + function_list[10101])
