function_list = [0] * 121
function2_list = [0] * 121
function_list[0], function2_list[0] = 1, 1
function_list[1], function2_list[1] = 1, 1
function_list[2], function2_list[2] = 1, 1
n = 4
while n < 122:
    function2_list[n] = function_list[n - 3] + function_list[n - 2]
    function_list[n - 1] = function_list[n - 3] - 2 * function2_list[n]
    function_list[n] = function2_list[n] + function_list[n - 1]
    function2_list[n - 1] = function_list[n] - function2_list[n - 2]
    n += 2
print(function2_list[120])
