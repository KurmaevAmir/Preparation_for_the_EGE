function_list = [0] * 10001
function_list[0] = 0
function_list[1] = 1
function_list[2] = 2
function_list[3] = 3
function_list[4] = 4
function_list[5] = 5
function_list[6] = 6
function_list[7] = 7
function_list[8] = 8
function_list[9] = 9
function_list[10] = 10
function_list[10000] = 1
for i in range(11, 5516, 2):
    function_list[i] = function_list[i - 2] - (i - 1) % 10
for i in range(9998, 11, -2):
    function_list[i] = i % 10 + function_list[i + 2]
print(function_list[4500] + function_list[5515])
