function_list = [0] * 5515
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

for i in range(11, 5515):
    if i % 2 == 0:
        function_list[i] = i % 10 + function_list
