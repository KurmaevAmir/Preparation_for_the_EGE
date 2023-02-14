function_list = [0] * 2255
function_list[1] = 1
function_list[2] = 1
function_list[3] = 1
for i in range(4, 2255):
    if i % 2 != 0:
        function_list[i] = i
    else:
        function_list[i] = function_list[i - 1] + function_list[i - 2] + function_list[i - 3]
print(function_list[2254] - function_list[2252])
