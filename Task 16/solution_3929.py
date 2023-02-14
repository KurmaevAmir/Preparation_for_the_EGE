function1_list = [0] * 100
function2_list = [0] * 100
function1_list[0], function2_list[0] = 0, 0
function1_list[1], function2_list[1] = 1, 1
function1_list[2], function2_list[2] = 2, 2
function1_list[3], function2_list[3] = 3, 3
function1_list[4], function2_list[4] = 4, 4
function1_list[5], function2_list[5] = 5, 5
function1_list[6], function2_list[6] = 6, 6
function1_list[7], function2_list[7] = 7, 7
function1_list[8], function2_list[8] = 8, 8
function1_list[9], function2_list[9] = 9, 9
for i in range(10, 100):
    function1_list[i] = i % 10 + function1_list[i // 10]
    function2_list[i] = function2_list[function1_list[i]]
total_sum = 0
for i in function2_list[10:]:
    total_sum += i
print(total_sum)
