function_list = [0] * 1000
function_list[1] = 1
for i in range(2, 1000):
    if i % 2 == 0:
        function_list[i] = function_list[i // 2] + 1
    else:
        function_list[i] = function_list[i - 1] + i
    if function_list[i] == 19:
        print(i)
        break
