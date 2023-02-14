function_list = [0] * 35
function_list[0] = 1
function_list[1] = 1
function_list[2] = 1
for i in range(3, 35):
    if i % 2 == 0:
        function_list[i] = function_list[i - 1] + i - 1
    else:
        function_list[i] = function_list[i - 2] + 2 * i - 2
print(function_list[34])
